import config
import jira
import git


def main():
    jira_config: config.JiraConfig = config.load_jira_config()
    # github_config: config.GithubConfig = config.load_github_config()

    ticket: jira.JiraTicket = jira.get_ticket(
        base_url=jira_config.jira_base_url,
        ticket_key="KAN-1",
        email=jira_config.jira_email,
        api_key=jira_config.jira_api_key,
    )
    print(ticket)

    branch_name = f"{ticket.issue_type}/{ticket.key}".lower()
    git.create_and_checkout_branch(branch_name)


if __name__ == "__main__":
    main()
