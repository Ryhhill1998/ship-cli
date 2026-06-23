import json
from pathlib import Path
from pydantic import BaseModel, ValidationError

CONFIG_FILE = Path.home() / ".ship" / "config.json"


class JiraConfig(BaseModel):
    base_url: str
    email: str
    api_key: str


class Settings(BaseModel):
    jira: JiraConfig | None = None


def load_settings() -> Settings:
    try:
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

        return Settings.model_validate(data)
    except FileNotFoundError:
        raise SystemExit(
            f"No configuration file found. Please create one at {CONFIG_FILE}"
        )
    except json.JSONDecodeError:
        raise ValueError(f"Config file at {CONFIG_FILE} is not valid JSON.")
    except ValidationError as e:
        raise ValueError(f"Invalid configuration settings in {CONFIG_FILE}:\n{e}")
