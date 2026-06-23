import re

from . import jira

PREFIX_MAP = {
    jira.IssueType.BUG: "fix",
    jira.IssueType.INCIDENT: "fix",
    jira.IssueType.STORY: "feature",
    jira.IssueType.TASK: "feature",
    jira.IssueType.NEW_FEATURE: "feature",
    jira.IssueType.IMPROVEMENT: "refactor",
    jira.IssueType.REFACTOR: "refactor",
    jira.IssueType.SPIKE: "chore",
    jira.IssueType.CHORE: "chore",
}


def create_branch_slug(ticket: jira.JiraTicket) -> str:
    """Takes a Jira ticket object and transforms it into a safe, clean git branch slug."""

    # 1. Clean the title: lower casing, replace spaces/underscores with hyphens
    clean_title = ticket.summary.lower().strip()
    clean_title = re.sub(r"[\s_]+", "-", clean_title)

    # 2. Strip out characters that are illegal or annoying in Git branch names
    clean_title = re.sub(r"[^a-zA-Z0-9\-]", "", clean_title)

    # 3. Collapse consecutive hyphens and trim trailing/leading ones
    clean_title = re.sub(r"-+", "-", clean_title).strip("-")

    # 4. Determine branch prefix cleanly from the typed enum map
    # Falls back to "feature" if a weird custom corporate issue type is used
    branch_prefix = PREFIX_MAP.get(ticket.issue_type, "feature")

    # 5. Arrange the final slug (e.g. "refactor/kan-12-clean-kafka-consumers")
    return f"{branch_prefix}/{ticket.key.lower()}-{clean_title}"
