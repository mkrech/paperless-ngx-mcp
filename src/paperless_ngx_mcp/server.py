"""MCP Server implementation for Paperless-NGX."""

import sys

from fastmcp import FastMCP

from .tools import (
    autocomplete_search_tool,
    get_document_tool,
    get_similar_documents_tool,
    list_tags_tool,
    search_documents_tool,
)

# Create FastMCP server
mcp = FastMCP("Paperless-NGX MCP Server")


# Register tools
@mcp.tool()
def search_documents(query: str = "", page: int = 1, page_size: int = 25) -> str:
    """
    Search Paperless-NGX documents and return results that should be presented to the user in a readable format.

    Use this tool to find documents by searching across titles, content, tags, correspondents, and other metadata.

    Args:
        query: Search query string (searches across title, content, tags, correspondent, etc.)
        page: Page number for pagination (default: 1)
        page_size: Number of results per page (default: 25, max: 100)

    Returns:
        JSON string containing search results. Parse and present the results to the user in a clear, readable format.
        Include key information like document titles, dates, and relevant content previews.
        
        The JSON structure includes:
        - total_count: Total number of matching documents
        - has_next_page: Whether more results are available
        - documents: Array with id, title, content_preview, correspondent, tags, created_date, original_file_name
    """
    return search_documents_tool(query=query, page=page, page_size=page_size)


@mcp.tool()
def get_document(document_id: int) -> str:
    """
    Get complete details for a single Paperless-NGX document by its ID.

    Use this tool when you need full information about a specific document, such as after finding it with search_documents.

    Args:
        document_id: The unique ID of the document to retrieve

    Returns:
        JSON string with complete document details. Parse and present the information to the user clearly.
        
        The JSON structure includes:
        - id, title, content (full text)
        - correspondent, document_type, storage_path
        - tags (array of tag IDs)
        - created_date, modified_date, added_date
        - archive_serial_number, original_file_name
        - custom_fields, notes
        
        If the document is not found, returns an error message with the document_id.
    """
    return get_document_tool(document_id=document_id)


@mcp.tool()
def get_similar_documents(
    document_id: int, page: int = 1, page_size: int = 25
) -> str:
    """
    Find documents similar to a given document using Paperless-NGX's similarity algorithm.

    Use this tool to discover related documents based on content similarity. Useful for research and finding related materials.

    Args:
        document_id: The ID of the reference document to find similar documents for
        page: Page number for pagination (default: 1)
        page_size: Number of results per page (default: 25, max: 100)

    Returns:
        JSON string with similar documents. Format matches search_documents output.
        
        The JSON structure includes:
        - total_count: Total number of similar documents found
        - has_next_page: Whether more results are available
        - documents: Array with id, title, content_preview, correspondent, tags, created_date, original_file_name
        
        If the reference document is not found, returns an error message with the document_id.
    """
    return get_similar_documents_tool(
        document_id=document_id, page=page, page_size=page_size
    )


@mcp.tool()
def list_tags() -> str:
    """
    Get all available tags from Paperless-NGX.

    Use this tool to see what tags exist in the system. Helpful for understanding categorization and filtering options.

    Returns:
        JSON string with all tags and their metadata. Present the tags to the user in a clear format.
        
        The JSON structure includes:
        - total_count: Total number of tags
        - tags: Array of tag objects with:
          - id: Tag ID
          - name: Tag name
          - color: Hex color code (e.g., "#a6cee3")
          - text_color: Text color for the tag (black or white)
          - document_count: Number of documents with this tag
    """
    return list_tags_tool()


@mcp.tool()
def autocomplete_search(term: str, limit: int = 10) -> str:
    """
    Get search term suggestions based on the Paperless-NGX document index.

    Use this tool to help users discover relevant search terms or to suggest better queries.
    Suggestions are ranked by TF/IDF score (term frequency-inverse document frequency).

    Args:
        term: Partial search term to get suggestions for
        limit: Maximum number of suggestions to return (default: 10)

    Returns:
        JSON string with suggested search terms ordered by relevance.
        
        The JSON structure includes:
        - term: The original search term
        - suggestions: Array of suggested complete terms (ordered by relevance)
        - count: Number of suggestions returned
    """
    return autocomplete_search_tool(term=term, limit=limit)


def main(port: int | None = None, host: str = "127.0.0.1"):
    """
    Start the MCP server.

    Args:
        port: If provided, start HTTP server on this port (Streamable HTTP).
              If None, use stdio transport (default).
        host: Host to bind to (default: 127.0.0.1). Use 0.0.0.0 for Docker access.
    """
    if port:
        # Streamable HTTP mode for OpenWebUI
        print(f"Starting Paperless-NGX MCP server on {host}:{port}...", file=sys.stderr)
        mcp.run(transport="streamable-http", port=port, host=host)
    else:
        # stdio mode for VS Code and Claude Desktop
        mcp.run(transport="stdio")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Paperless-NGX MCP Server")
    parser.add_argument(
        "--port",
        type=int,
        help="Port for HTTP server (Streamable HTTP). If not specified, uses stdio.",
    )

    args = parser.parse_args()
    main(port=args.port)
