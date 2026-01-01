# VS Code MCP Testing Guide

This guide explains how to test the Paperless-NGX MCP server in VS Code.

## Prerequisites

- VS Code with MCP support
- Paperless-NGX instance running (default: http://localhost:8000)
- Valid Paperless-NGX API token

## Configuration

The MCP server is configured in `.vscode/mcp-server.json`:

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

**Credentials are loaded from `.env` file automatically.** No need to configure them in mcp-server.json.

## Setup Steps

1. **Get your API token** from Paperless-NGX:
   - Open Paperless-NGX web interface
   - Go to Settings → API Tokens
   - Create a new token or copy existing one

2. **Configure the MCP server**:
   - Open `.vscode/mcp-server.json`
   - Replace `your-token-here` with your actual token
   - Adjust `PAPERLESS_API_URL` if needed
your credentials** in `.env`:
   - Copy `.env.example` to `.env` (if not already done)
   - Edit `.env` and set your `PAPERLESS_API_TOKEN`
   - Adjust `PAPERLESS_API_URL` if your instance is not at localhost:8000

## Testing the Server

### Using the MCP Tool

Once configured, you can use the `search_documents` tool in VS Code:

**Example queries:**

1. Search for invoices:
   ```
   Search paperless documents for "invoice"
   ```

2. Search with pagination:
   ```
   Search paperless documents for "tax" on page 2 with 10 results per page
   ```

3. List recent documents:
   ```
   Search all paperless documents
   ```

### Expected Response

The tool returns JSON with:
- `total_count`: Total matching documents
- `page_size`: Documents in current page
- `has_next_page`: Whether more pages available
- `documents`: Array of matching documents with:
  - `id`, `title`, `content_preview`
  - `correspondent`, `document_type`, `tags`
  - `created_date`, `original_file_name`

## Troubleshooting

### "PAPERLESS_API_TOKEN environment variable is required"
- Check that `.env` file exists in project root
- Verify your token is set in `.env`
- Ensure the token is not empty or placeholder text

### "Cannot connect to Paperless-NGX"
- Verify Paperless-NGX is running at the configured URL
- Check `PAPERLESS_API_URL` in `.env`
- Test with: `curl -H "Authorization: Token YOUR_TOKEN" http://localhost:8000/api/documents/`

### "Authentication failed"
- Check that your API token in `.env` is valid
- Generate a new token in Paperless-NGX settings

### Server not appearing in VS Code
- Verify `.vscode/mcp-server.json` has valid JSON syntax
- Reload VS Code window
- Check VS Code output panel for MCP errors

## Configuration File Location

All credentials are stored in `.env` in the project root:

```env
PAPERLESS_API_URL=http://localhost:8000
PAPERLESS_API_TOKEN=your-actual-token-here
```

**Important:** The `.env` file is gitignored and will not be committed to version control.
