"""Entry point for Paperless-NGX MCP Server."""

import argparse

from paperless_ngx_mcp.server import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Paperless-NGX MCP Server")
    parser.add_argument(
        "--port",
        type=int,
        help="Port for HTTP server (Streamable HTTP). If not specified, uses stdio.",
    )
    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host to bind to (default: 127.0.0.1). Use 0.0.0.0 for Docker access.",
    )

    args = parser.parse_args()
    main(port=args.port, host=args.host)

