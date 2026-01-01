"""Configuration for Paperless-NGX MCP Server."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env file from project root
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class Config:
    """Configuration loaded from environment variables."""

    def __init__(self):
        self.api_url = os.getenv("PAPERLESS_API_URL", "http://localhost:8000")
        self.api_token = os.getenv("PAPERLESS_API_TOKEN")

        if not self.api_token:
            raise ValueError(
                "PAPERLESS_API_TOKEN environment variable is required. "
                "Set it to your Paperless-NGX API token."
            )

    @property
    def auth_header(self) -> dict[str, str]:
        """Return the authorization header for API requests."""
        return {"Authorization": f"Token {self.api_token}"}


# Global config instance
config: Config | None = None


def get_config() -> Config:
    """Get or create the global config instance."""
    global config
    if config is None:
        config = Config()
    return config
