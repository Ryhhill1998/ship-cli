import contextlib
import subprocess
from enum import StrEnum


class DefaultBaseBranchName(StrEnum):
    MAIN = "main"
    MASTER = "master"


def deduce_base_branch_name() -> str:
    """Attempts to deduce the name of the base branch by looking at the remote tracking HEAD."""

    with contextlib.suppress(subprocess.CalledProcessError):
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "origin/HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )

        remote_head = result.stdout.replace("origin/", "").strip()

        if remote_head == "main":
            return DefaultBaseBranchName.MAIN

        if remote_head == "master":
            return DefaultBaseBranchName.MASTER

    raise ValueError("Could not deduce the base branch name. Please specify it manually.")


def sync_base_branch(branch_name: str) -> None:
    """Safely updates the base branch (the branch being branched off of) before work begins."""

    subprocess.run(["git", "checkout", branch_name], check=True)
    subprocess.run(["git", "pull"], check=True)


def create_and_checkout_branch(new_branch_name: str, base_branch_name: str | None = None) -> None:
    """Syncs the base workspace and initialises the new local tracking branch."""

    # 1. Try switching to the new branch first
    try:
        subprocess.run(["git", "checkout", new_branch_name], check=True)  # This will fail if the branch doesn't exist
    except subprocess.CalledProcessError:
        # 2. If no base branch is specified, deduce it from the current workspace
        base_branch: str = base_branch_name or deduce_base_branch_name()

        # 3. Updates your local base tracking branch first
        sync_base_branch(base_branch)

        # 4. Spins up the new feature branch cleanly off the freshly updated base branch
        subprocess.run(["git", "checkout", "-b", new_branch_name], check=True)
