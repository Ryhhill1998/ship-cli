import typer

import config
import jira
import git
import utils


def main(ticket_id: str):
    settings: config.Settings = config.load_settings()
    jira_config = settings.jira

    if jira_config is None:
        raise ValueError("Jira configuration is missing.")

    ticket: jira.JiraTicket = jira.get_ticket(
        base_url=jira_config.base_url,
        ticket_key=ticket_id,
        email=jira_config.email,
        api_key=jira_config.api_key,
    )
    branch_name = utils.create_branch_slug(ticket)
    git.create_and_checkout_branch(branch_name)


if __name__ == "__main__":
    typer.run(main)
