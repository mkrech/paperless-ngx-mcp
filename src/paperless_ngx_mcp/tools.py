"""MCP tools for Paperless-NGX."""

import json
from typing import Any

from .api import PaperlessAPI


def format_document_results(api_response: dict[str, Any]) -> str:
    """
    Format Paperless-NGX API response into readable JSON string.

    Args:
        api_response: Raw API response from Paperless-NGX

    Returns:
        Formatted JSON string for AI consumption
    """
    results = api_response.get("results", [])
    count = api_response.get("count", 0)
    next_page = api_response.get("next")
    previous_page = api_response.get("previous")

    formatted_docs = []
    for doc in results:
        # Truncate content preview to 200 characters
        content = doc.get("content", "")
        content_preview = (
            content[:200] + "..." if len(content) > 200 else content
        )

        formatted_doc = {
            "id": doc.get("id"),
            "title": doc.get("title"),
            "content_preview": content_preview,
            "correspondent": doc.get("correspondent"),
            "document_type": doc.get("document_type"),
            "tags": doc.get("tags", []),
            "created_date": doc.get("created_date"),
            "original_file_name": doc.get("original_file_name"),
        }
        formatted_docs.append(formatted_doc)

    result = {
        "total_count": count,
        "page_size": len(results),
        "has_next_page": next_page is not None,
        "has_previous_page": previous_page is not None,
        "documents": formatted_docs,
    }

    return json.dumps(result, indent=2)


def search_documents_tool(query: str = "", page: int = 1, page_size: int = 25) -> str:
    """
    Search Paperless-NGX documents by query string.

    Args:
        query: Search query (searches across title, content, tags, etc.)
        page: Page number (default: 1)
        page_size: Number of results per page (default: 25)

    Returns:
        JSON string with matching documents and pagination info
    """
    try:
        with PaperlessAPI() as api:
            response = api.search_documents(
                query=query, page=page, page_size=page_size
            )
            return format_document_results(response)
    except Exception as e:
        error_result = {
            "error": str(e),
            "query": query,
            "page": page,
            "page_size": page_size,
        }
        return json.dumps(error_result, indent=2)
