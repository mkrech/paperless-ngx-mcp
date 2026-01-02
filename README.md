# Paperless-NGX MCP Server

A Model Context Protocol (MCP) server for [Paperless-NGX](https://github.com/paperless-ngx/paperless-ngx), enabling AI assistants to search and interact with your documents.

## Features

- 🔍 **Document Search** - Search across titles, content, tags, correspondents, and more
- 🔌 **Dual Transport** - Supports both stdio (VS Code, Claude Desktop, LM Studio) and Streamable HTTP (OpenWebUI)
- ⚡ **Fast & Simple** - Built with [fastmcp](https://github.com/jlowin/fastmcp) for minimal overhead
- 🔐 **Secure** - Token-based authentication via environment variables
- 📄 **Pagination** - Efficient handling of large document collections
- ✅ **Production Ready** - Tested with VS Code and LM Studio

## Installation

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- Running Paperless-NGX instance
- Paperless-NGX API token

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd paperless-ngx-mcp
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Configure credentials**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and set your credentials:
   ```env
   PAPERLESS_API_URL=http://localhost:8000
   PAPERLESS_API_TOKEN=your-api-token-here
   ```
   
   Get your API token from Paperless-NGX: Settings → API Tokens

4. **Install in editable mode** (for VS Code integration)
   ```bash
   uv pip install -e .
   ```

## Usage

### VS Code / Claude Desktop (stdio mode)

The server runs in stdio mode by default, which is required for VS Code and Claude Desktop.

**VS Code Setup:**

1. The server is pre-configured in `.vscode/mcp.json`:
   ```json
   {
     "servers": {
       "paperless-ngx": {
         "command": "uv",
         "args": ["run", "python", "main.py"]
       }
     }
   }
   ```

2. Restart VS Code or reload the MCP servers

3. Use the available tools in your chat

**Available Tools:**
- `search_documents` - Search for documents by query
- `get_document` - Get complete details for a specific document by ID
- `get_similar_documents` - Find documents similar to a given document
- `list_tags` - Get all available tags
- `autocomplete_search` - Get search term suggestions

**Example queries:**
- "Search my Paperless documents for 'invoice'"
- "Find documents from Telekom"
- "Show me all documents tagged with 'tax'"
- "Search paperless documents for 'tax' on page 2 with 10 results per page"
- "Get details for document 123"
- "Find documents similar to document 456"
- "What tags are available in my Paperless system?"
- "Suggest search terms for 'tel'"
- "Search all paperless documents" (empty query returns all documents)

**Testing Results** ✅

All tools have been tested and verified in VS Code (January 2, 2026):

1. **`list_tags`** - Retrieved 9 tags with metadata
   - Example result: 9 tags including "chris" (2 docs), "congstar" (0 docs), "deutschlandticket" (1 doc), "hardware" (2 docs), "michael" (9 docs), "mobilephone" (5 docs), "tax" (0 docs), "telekom" (2 docs), "versicherungen" (0 docs)
   - Each tag includes: id, name, color (#hex), text_color, document_count

2. **`get_document`** - Retrieved complete document details for ID 1
   - Example: "AGB_congstar_Mobilfunktarife"
   - Full content: 24,787 characters
   - Metadata: correspondent, document_type, storage_path, tags
   - Dates: created, modified, added
   - All custom fields and notes included

3. **`autocomplete_search`** - Generated search suggestions for "tel"
   - Result: 10 suggestions ordered by TF/IDF relevance
   - Examples: "tel", "telekom", "telefon", "telefonisch", "telefonische", "telefonieren", "telekommunikationsverträge", "teln", "tele", "telefonbucheintrag"
   - Helps users discover relevant search terms from document index

4. **`get_similar_documents`** - Found 9 documents similar to document ID 1
   - Most similar results: Other congstar contracts (Leistungsbeschreibung, Preisliste)
   - Related documents: Telekom contract, insurance documents, Deutschlandticket
   - Uses Paperless-NGX's similarity algorithm based on content analysis

5. **`search_documents`** - Previously tested and working
   - Searches across titles, content, tags, correspondents
   - Pagination support (page, page_size)
   - Returns document previews with metadata

**Getting your API Token:**
1. Open Paperless-NGX web interface
2. Go to Settings → API Tokens
3. Create a new token or copy existing one
4. Add it to your `.env` file

**Testing the integration:**
1. Make sure your `.env` file is configured with valid credentials
2. Restart VS Code or reload the MCP servers
3. Check the VS Code Output panel for MCP logs
4. Look for "Starting MCP server 'Paperless-NGX MCP Server'" message
5. The server should discover 5 tools: `search_documents`, `get_document`, `get_similar_documents`, `list_tags`, `autocomplete_search`

### LM Studio (stdio mode) ✅ RECOMMENDED

LM Studio supports MCP servers via stdio transport and has **full working MCP tool support**!

**Setup:**

1. Open LM Studio → **Developer** → **MCP Servers**

2. Add this configuration:
   ```json
   {
     "mcpServers": {
       "paperless-ngx": {
         "command": "uv",
         "args": ["run", "python", "main.py"],
         "cwd": "/Users/dobby/_work/paperless-ngx-mcp",
         "env": {
           "PAPERLESS_API_URL": "http://localhost:8000",
           "PAPERLESS_API_TOKEN": "your-token-here"
         }
       }
     }
   }
   ```

3. Replace the paths and credentials:
   - `cwd`: Path to your paperless-ngx-mcp directory
   - `PAPERLESS_API_URL`: Your Paperless-NGX API URL
   - `PAPERLESS_API_TOKEN`: Your Paperless-NGX API token

4. Save and reload MCP servers in LM Studio

**✅ Fully verified and working** - LM Studio correctly invokes the search_documents tool and returns results!

### OpenWebUI ⚠️ EXPERIMENTAL (Limited Support)

**Status:** Connection test works, but tools are **NOT invoked during chat**. OpenWebUI's MCP/OpenAPI integration is experimental and incomplete.

**For OpenWebUI users, we recommend using LM Studio instead** which has full working MCP support.

<details>
<summary>OpenWebUI Configuration (for reference)</summary>

For OpenWebUI, start the server in HTTP mode:

```bash
uv run python main.py --port 8100 --host 0.0.0.0
```

The server will start on `http://0.0.0.0:8100/mcp` with Streamable HTTP transport.

**OpenWebUI Configuration:**

1. Open OpenWebUI → Settings → Connections
2. Add new MCP Server:
   - **Type**: MCP (Streamable HTTP)
   - **Name**: Paperless-NGX
   - **URL**: `http://host.docker.internal:8100/mcp` (if OpenWebUI in Docker)
   - Or: `http://localhost:8100/mcp` (if OpenWebUI on host)
3. Save and test the connection

**Result:** Connection test passes ✅, but tools are not invoked in chat ❌

**Docker Note:** If OpenWebUI runs in Docker and the MCP server on your host, use `host.docker.internal` instead of `localhost`.

</details>

**Recommendation:** Use **LM Studio** (stdio mode) or **VS Code** for full MCP support with tool invocation!

### Command Line Testing

The Streamable HTTP transport uses session-based communication. Here's a basic test:

```bash
# Start server
uv run python main.py --port 8100

# In another terminal, initialize a session
curl -X POST http://localhost:8100/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "method": "initialize",
    "params": {
      "protocolVersion": "2024-11-05",
      "capabilities": {},
      "clientInfo": {"name": "test", "version": "1.0"}
    },
    "id": 1
  }'
```

**Note:** For production use, OpenWebUI handles session management automatically. Manual curl testing is limited to initialization and basic connectivity verification.

## Available Tools

### `search_documents`

Search Paperless-NGX documents by query string.

**Parameters:**
- `query` (string, optional): Search query (searches across title, content, tags, correspondent, etc.)
- `page` (int, default: 1): Page number for pagination
- `page_size` (int, default: 25, max: 100): Number of results per page

**Returns:**
- `total_count`: Total number of matching documents
- `page_size`: Number of documents in current page
- `has_next_page`: Whether more pages are available
- `documents`: List of matching documents with:
  - `id`, `title`, `content_preview`
  - `correspondent`, `document_type`, `tags`
  - `created_date`, `original_file_name`

## Development

### Code Quality

The project uses [ruff](https://github.com/astral-sh/ruff) for linting and formatting:

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check

# Auto-fix issues
uv run ruff check --fix
```

### Project Structure

```
paperless-ngx-mcp/
├── src/paperless_ngx_mcp/
│   ├── __init__.py
│   ├── server.py       # MCP server setup
│   ├── api.py          # Paperless API client
│   ├── config.py       # Configuration management
│   └── tools.py        # MCP tools (search_documents)
├── main.py             # Entry point
├── pyproject.toml      # Dependencies
└── .env                # Configuration (gitignored)
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'paperless_ngx_mcp'"

Install the package in editable mode:
```bash
uv pip install -e .
```

### "PAPERLESS_API_TOKEN environment variable is required"

1. Check that `.env` file exists in project root
2. Verify your token is set in `.env` (not just the placeholder text)
3. Ensure the token value has no extra spaces or quotes
4. The `.env` file is gitignored and will not be committed

### "Authentication failed. Check your PAPERLESS_API_TOKEN"

1. Verify your `.env` file exists and contains `PAPERLESS_API_TOKEN`
2. Get a valid token from Paperless-NGX: Settings → API Tokens
3. Generate a new token if the current one expired
4. Test manually: `curl -H "Authorization: Token YOUR_TOKEN" http://localhost:8000/api/documents/`

### "Cannot connect to Paperless-NGX"

1. Check if Paperless-NGX is running
2. Verify `PAPERLESS_API_URL` in `.env` matches your instance
3. Test API access: `curl http://localhost:8000/api/documents/`
4. Check firewall settings if using remote instance

### Server not appearing in VS Code

1. Verify `.vscode/mcp.json` has valid JSON syntax
2. Make sure you installed the package: `uv pip install -e .`
3. Reload VS Code window (Cmd+Shift+P → "Developer: Reload Window")
4. Check VS Code Output panel → "MCP" for error messages
5. Ensure your `.env` file exists and has valid credentials

### HTTP Server Connection Issues

**"Connection refused" when testing HTTP mode:**
1. Verify server is running: `lsof -i :8100` should show the Python process
2. Check server logs for "Starting MCP server...with transport 'streamable-http'"
3. Ensure you're using the correct URL: `http://127.0.0.1:8100/mcp`

**OpenWebUI can't connect (Docker):**
1. Use `http://host.docker.internal:8100/mcp` instead of `localhost`
2. Check if port 8100 is exposed/accessible from Docker
3. Verify no firewall blocking the connection

### Expected Response Format

The `search_documents` tool returns JSON with:
- `total_count`: Total matching documents
- `page_size`: Documents in current page
- `has_next_page`: Whether more pages available
- `has_previous_page`: Whether previous pages available
- `documents`: Array of matching documents with:
  - `id`, `title`, `content_preview` (truncated to 200 chars)
  - `correspondent`, `document_type`, `tags`
  - `created_date`, `original_file_name`

## Contributing

Contributions welcome! Please:
1. Follow the existing code style (ruff)
2. Add tests for new features
3. Update documentation

## License

MIT License - see LICENSE file for details

## Credits

Built with:
- [fastmcp](https://github.com/jlowin/fastmcp) - FastAPI-like MCP framework
- [Paperless-NGX](https://github.com/paperless-ngx/paperless-ngx) - Document management system
- [httpx](https://www.python-httpx.org/) - Modern HTTP client
