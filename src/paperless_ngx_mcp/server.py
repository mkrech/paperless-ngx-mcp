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
