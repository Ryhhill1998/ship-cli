import requests


def get_repo_info(repo_name: str, access_token: str) -> None:
    headers = {"Authorization": f"token {access_token}"}
    owner_name = "Ryhhill1998"
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}"

    response = requests.get(url=url, headers=headers)
    print(response.status_code)
    print(response.text)
