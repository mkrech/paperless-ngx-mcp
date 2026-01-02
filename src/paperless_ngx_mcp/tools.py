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


def format_single_document(api_response: dict[str, Any]) -> str:
    """
    Format a single document's complete details into readable JSON string.

    Args:
        api_response: Raw API response for a single document

    Returns:
        Formatted JSON string with complete document information
    """
    formatted_doc = {
        "id": api_response.get("id"),
        "title": api_response.get("title"),
        "content": api_response.get("content", ""),
        "correspondent": api_response.get("correspondent"),
        "document_type": api_response.get("document_type"),
        "storage_path": api_response.get("storage_path"),
        "tags": api_response.get("tags", []),
        "created_date": api_response.get("created_date"),
        "modified_date": api_response.get("modified"),
        "added_date": api_response.get("added"),
        "archive_serial_number": api_response.get("archive_serial_number"),
        "original_file_name": api_response.get("original_file_name"),
        "custom_fields": api_response.get("custom_fields", []),
        "notes": api_response.get("notes", []),
    }

    return json.dumps(formatted_doc, indent=2)


def get_document_tool(document_id: int) -> str:
    """
    Get complete details for a single document by ID.

    Args:
        document_id: ID of the document to retrieve

    Returns:
        JSON string with complete document details
    """
    try:
        with PaperlessAPI() as api:
            response = api.get_document(document_id)
            return format_single_document(response)
    except Exception as e:
        error_result = {
            "error": str(e),
            "document_id": document_id,
        }
        return json.dumps(error_result, indent=2)


def get_similar_documents_tool(
    document_id: int, page: int = 1, page_size: int = 25
) -> str:
    """
    Find documents similar to a given document.

    Args:
        document_id: Reference document ID
        page: Page number (default: 1)
        page_size: Number of results per page (default: 25)

    Returns:
        JSON string with similar documents and pagination info
    """
    try:
        with PaperlessAPI() as api:
            response = api.get_similar_documents(
                document_id=document_id, page=page, page_size=page_size
            )
            return format_document_results(response)
    except Exception as e:
        error_result = {
            "error": str(e),
            "reference_document_id": document_id,
            "page": page,
            "page_size": page_size,
        }
        return json.dumps(error_result, indent=2)


def format_tags(api_response: dict[str, Any]) -> str:
    """
    Format tags API response into readable JSON string.

    Args:
        api_response: Raw API response with tags

    Returns:
        Formatted JSON string with tag information
    """
    results = api_response.get("results", [])
    count = api_response.get("count", 0)

    formatted_tags = []
    for tag in results:
        formatted_tag = {
            "id": tag.get("id"),
            "name": tag.get("name"),
            "color": tag.get("color"),
            "text_color": tag.get("text_color"),
            "document_count": tag.get("document_count", 0),
        }
        formatted_tags.append(formatted_tag)

    result = {
        "total_count": count,
        "tags": formatted_tags,
    }

    return json.dumps(result, indent=2)


def list_tags_tool() -> str:
    """
    Get all available tags from Paperless-NGX.

    Returns:
        JSON string with all tags and their metadata
    """
    try:
        with PaperlessAPI() as api:
            response = api.list_tags()
            return format_tags(response)
    except Exception as e:
        error_result = {
            "error": str(e),
        }
        return json.dumps(error_result, indent=2)


def autocomplete_search_tool(term: str, limit: int = 10) -> str:
    """
    Get search term autocomplete suggestions.

    Args:
        term: Partial search term
        limit: Maximum number of suggestions (default: 10)

    Returns:
        JSON string with suggested search terms
    """
    try:
        with PaperlessAPI() as api:
            suggestions = api.autocomplete_search(term=term, limit=limit)
            result = {
                "term": term,
                "suggestions": suggestions,
                "count": len(suggestions),
            }
            return json.dumps(result, indent=2)
    except Exception as e:
        error_result = {
            "error": str(e),
            "term": term,
            "limit": limit,
        }
        return json.dumps(error_result, indent=2)
