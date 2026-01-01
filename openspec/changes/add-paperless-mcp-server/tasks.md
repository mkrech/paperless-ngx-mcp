# Implementation Tasks

## 1. Project Setup
- [x] 1.1 Update pyproject.toml with fastmcp, httpx, ruff, python-dotenv dependencies
- [x] 1.2 Configure ruff for code formatting and linting
- [x] 1.3 Add uv.lock if needed
- [x] 1.4 Create .env and .env.example files
- [x] 1.5 Add .env to .gitignore

## 2. MCP Server Core
- [x] 2.1 Create src/paperless_ngx_mcp/ module structure
- [x] 2.2 Implement main MCP server with fastmcp
- [x] 2.3 Add support for stdio transport (default)
- [x] 2.4 Add support for Streamable HTTP transport with --port flag
- [x] 2.5 Add configuration for API URL and token (environment variables)
- [x] 2.6 Update main.py to serve MCP server with transport selection

## 3. Document Search Tool
- [x] 3.1 Implement HTTP client for Paperless-NGX API
- [x] 3.2 Create search_documents MCP tool
- [x] 3.3 Handle pagination and result formatting
- [x] 3.4 Add error handling for API failures

## 4. VS Code Integration
- [x] 4.1 Create .vscode/mcp-server.json configuration
- [x] 4.2 Document how to test in VS Code
- [x] 4.3 Add sample environment configuration

## 5. Documentation & Testing
- [ ] 5.1 Update README.md with setup instructions
- [ ] 5.2 Add example usage documentation for both transports
- [ ] 5.3 Test search_documents with real Paperless-NGX instance
- [ ] 5.4 Verify VS Code MCP integration works (stdio)
- [ ] 5.5 Test Streamable HTTP mode with curl or web client
- [ ] 5.6 Verify OpenWebUI MCP server integration (Type: MCP Streamable HTTP)
- [ ] 5.7 Document OpenWebUI configuration steps
