# Change: Add Document Retrieval and Metadata Tools

## Why
Currently the MCP server only provides document search functionality. Users need to retrieve full document details, discover similar documents, explore available tags for filtering, and get search suggestions for better queries. This enhances the AI's ability to work with Paperless-NGX documents by providing complete document information, metadata discovery, and improved search capabilities.

## What Changes
- Add `get_document` tool to retrieve complete document details by ID
- Add `get_similar_documents` tool to find documents similar to a given document (using Paperless API's `more_like_id` feature)
- Add `list_tags` tool to retrieve all available tags with their metadata (ID, name, color)
- Add `autocomplete_search` tool to get search term suggestions based on document index
- Extend API client to support new endpoints (`/api/documents/{id}/`, `/api/tags/`, `/api/search/autocomplete/`)
- Update documentation with new tool examples

## Impact
- Affected specs: `document-search` (MODIFIED - extend with retrieval and metadata capabilities)
- Affected code: 
  - `src/paperless_ngx_mcp/api.py` - Add new API methods for documents, tags, and autocomplete
  - `src/paperless_ngx_mcp/tools.py` - Add 4 new tool implementations
  - `src/paperless_ngx_mcp/server.py` - Register 4 new MCP tools
  - `README.md` - Document new tools and usage examples
