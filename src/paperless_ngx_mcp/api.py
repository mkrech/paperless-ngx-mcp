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

    def get_document(self, document_id: int) -> dict[str, Any]:
        """
        Get a single document by ID.

        Args:
            document_id: Document ID to retrieve

        Returns:
            API response with complete document details

        Raises:
            Exception: If document not found or API request fails
        """
        try:
            response = self.client.get(f"/api/documents/{document_id}/")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise Exception(
                    f"Document with ID {document_id} not found."
                ) from e
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

    def get_similar_documents(
        self, document_id: int, page: int = 1, page_size: int = 25
    ) -> dict[str, Any]:
        """
        Find documents similar to a given document.

        Args:
            document_id: Reference document ID
            page: Page number (1-indexed)
            page_size: Number of results per page

        Returns:
            API response with similar documents and pagination info

        Raises:
            Exception: If reference document not found or API request fails
        """
        params = {
            "more_like_id": document_id,
            "page": page,
            "page_size": page_size,
        }

        try:
            response = self.client.get("/api/documents/", params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise Exception(
                    f"Reference document with ID {document_id} not found."
                ) from e
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

    def list_tags(self) -> dict[str, Any]:
        """
        Get all tags from Paperless-NGX.

        Returns:
            API response with all tags

        Raises:
            httpx.HTTPError: If API request fails
        """
        try:
            response = self.client.get("/api/tags/")
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

    def autocomplete_search(self, term: str, limit: int = 10) -> list[str]:
        """
        Get search term autocomplete suggestions.

        Args:
            term: Partial search term
            limit: Maximum number of suggestions (default: 10)

        Returns:
            List of suggested search terms

        Raises:
            httpx.HTTPError: If API request fails
        """
        params = {
            "term": term,
            "limit": limit,
        }

        try:
            response = self.client.get("/api/search/autocomplete/", params=params)
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
