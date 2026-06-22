from dataclasses import dataclass
from enum import StrEnum

import requests
from requests.auth import HTTPBasicAuth


class IssueType(StrEnum):
    BUG = "Bug"
    INCIDENT = "Incident"
    STORY = "Story"
    TASK = "Task"
    NEW_FEATURE = "New Feature"
    IMPROVEMENT = "Improvement"
    REFACTOR = "Refactor"
    SPIKE = "Spike"
    CHORE = "Chore"


@dataclass
class JiraTicket:
    key: str
    summary: str
    issue_type: IssueType


def get_ticket(base_url: str, ticket_key: str, email: str, api_key: str) -> JiraTicket:
    url = f"{base_url}/issue/{ticket_key}"
    auth = HTTPBasicAuth(username=email, password=api_key)
    headers = {"Accept": "application/json"}

    response = requests.get(url, auth=auth, headers=headers)
    response.raise_for_status()
    data = response.json()

    return JiraTicket(
        key=data["key"],
        issue_type=data["fields"]["issuetype"]["name"],
        summary=data["fields"]["summary"],
    )
