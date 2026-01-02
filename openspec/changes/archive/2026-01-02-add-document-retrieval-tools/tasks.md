# Implementation Tasks

## 1. API Client Extension
- [x] 1.1 Add `get_document(document_id: int)` method to PaperlessAPI class
- [x] 1.2 Add `get_similar_documents(document_id: int, page: int, page_size: int)` method to PaperlessAPI class
- [x] 1.3 Add `list_tags()` method to PaperlessAPI class
- [x] 1.4 Add `autocomplete_search(term: str, limit: int)` method to PaperlessAPI class
- [x] 1.5 Add error handling for document not found (404) and other API errors

## 2. Tool Implementation
- [x] 2.1 Implement `get_document_tool(document_id: int)` in tools.py
- [x] 2.2 Implement `format_single_document(api_response: dict)` helper function
- [x] 2.3 Implement `get_similar_documents_tool(document_id: int, page: int, page_size: int)` in tools.py
- [x] 2.4 Implement `list_tags_tool()` in tools.py
- [x] 2.5 Implement `format_tags(api_response: dict)` helper function
- [x] 2.6 Implement `autocomplete_search_tool(term: str, limit: int)` in tools.py
- [x] 2.7 Add error handling for all tools

## 3. MCP Server Registration
- [x] 3.1 Register `get_document` MCP tool in server.py
- [x] 3.2 Register `get_similar_documents` MCP tool in server.py
- [x] 3.3 Register `list_tags` MCP tool in server.py
- [x] 3.4 Register `autocomplete_search` MCP tool in server.py
- [x] 3.5 Add comprehensive docstrings for AI instructions on all tools

## 4. Documentation & Testing
- [x] 4.1 Update README.md with all new tool examples
- [x] 4.2 Test `get_document` with real Paperless instance ✅ (Document 1 with 24,787 chars content)
- [x] 4.3 Test `get_similar_documents` with real Paperless instance ✅ (9 similar documents found)
- [x] 4.4 Test `list_tags` with real Paperless instance ✅ (9 tags retrieved)
- [x] 4.5 Test `autocomplete_search` with real Paperless instance ✅ (10 suggestions for "tel")
- [x] 4.6 Verify all tools work in VS Code MCP integration ✅ (All 5 tools tested successfully on 2026-01-02)
- [x] 4.7 LM Studio testing skipped (stdio transport already validated in VS Code)
