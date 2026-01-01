"""Paperless-NGX API client."""

from typing import Any

import httpx

from .config import get_config


class PaperlessAPI:
    """HTTP client for Paperless-NGX API."""

    def __init__(self):
        self.config = get_config()
        self.client = httpx.Client(
            base_url=self.config.api_url,
            headers=self.config.auth_header,
            timeout=30.0,
        )

    def search_documents(
        self, query: str = "", page: int = 1, page_size: int = 25
    ) -> dict[str, Any]:
        """
        Search Paperless-NGX documents.

        Args:
            query: Search query string
            page: Page number (1-indexed)
            page_size: Number of results per page

        Returns:
            API response with documents and pagination info

        Raises:
            httpx.HTTPError: If API request fails
        """
        params = {
            "query": query,
            "page": page,
            "page_size": page_size,
        }

        try:
            response = self.client.get("/api/documents/", params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise Exception(
                    f"Authentication failed. Check your PAPERLESS_API_TOKEN. "
                    f"Status: {e.response.status_code}"
                ) from e
            raise Exception(
                f"API request failed: {e.response.status_code} - {e.response.text}"
            ) from e
        except httpx.ConnectError as e:
            raise Exception(
                f"Cannot connect to Paperless-NGX at {self.config.api_url}. "
                f"Make sure the server is running."
            ) from e
        except httpx.TimeoutException as e:
            raise Exception(
                "Request to Paperless-NGX timed out after 30s."
            ) from e

    def close(self):
        """Close the HTTP client."""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
