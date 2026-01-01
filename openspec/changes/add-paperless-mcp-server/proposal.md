# Change: Add Paperless-NGX MCP Server

## Why
Enable AI assistants to search and interact with Paperless-NGX documents through the Model Context Protocol (MCP). This provides a standardized interface for document retrieval and management within AI workflows, starting with document search functionality.

## What Changes
- Create MCP server using fastmcp framework with Python
- Support both stdio and HTTP streaming transports
- Implement document search tool that queries Paperless-NGX API
- Set up VS Code MCP configuration for local testing
- Use uv for dependency management and ruff for code quality
- Configure API authentication with token-based auth

## Impact
- Affected specs: 
  - `mcp-server` (new) - Core MCP server implementation
  - `document-search` (new) - Document search capability
  - `vscode-integration` (new) - VS Code testing configuration
- Affected code:
  - `main.py` - Replace with MCP server entry point
  - `pyproject.toml` - Add dependencies (fastmcp, httpx, ruff)
  - `.vscode/mcp-server.json` - New VS Code MCP configuration
  - New module structure for server implementation
