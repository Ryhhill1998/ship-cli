import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class JiraConfig:
    jira_base_url: str
    jira_email: str
    jira_api_key: str


@dataclass
class GithubConfig:
    github_access_token: str


def load_jira_config() -> JiraConfig:
    try:
        jira_base_url = os.environ["JIRA_BASE_URL"]
        jira_email = os.environ["JIRA_EMAIL"]
        jira_api_key = os.environ["JIRA_API_KEY"]
    except KeyError as e:
        raise ValueError(f"Missing Jira environment variable: {e}")
    else:
        return JiraConfig(jira_base_url, jira_email, jira_api_key)


def load_github_config() -> GithubConfig:
    try:
        github_access_token = os.environ["GITHUB_ACCESS_TOKEN"]
    except KeyError as e:
        raise ValueError(f"Missing Github environment variable: {e}")
    else:
        return GithubConfig(github_access_token)
