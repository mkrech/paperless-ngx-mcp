"""MCP Server implementation for Paperless-NGX."""

import sys

from fastmcp import FastMCP

from .tools import search_documents_tool

# Create FastMCP server
mcp = FastMCP("Paperless-NGX MCP Server")


# Register tools
@mcp.tool()
def search_documents(query: str = "", page: int = 1, page_size: int = 25) -> str:
    """
    Search Paperless-NGX documents.

    Args:
        query: Search query string (searches across title, content, tags, correspondent, etc.)
        page: Page number for pagination (default: 1)
        page_size: Number of results per page (default: 25, max: 100)

    Returns:
        JSON string containing:
        - total_count: Total number of matching documents
        - page_size: Number of documents in current page
        - has_next_page: Whether more pages are available
        - documents: List of matching documents with id, title, content preview, etc.
    """
    return search_documents_tool(query=query, page=page, page_size=page_size)


def main(port: int | None = None):
    """
    Start the MCP server.

    Args:
        port: If provided, start HTTP server on this port (Streamable HTTP).
              If None, use stdio transport (default).
    """
    if port:
        # Streamable HTTP mode for OpenWebUI
        print(f"Starting Paperless-NGX MCP server on port {port}...", file=sys.stderr)
        mcp.run(transport="streamable-http", port=port)
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
