# Implementation Tasks

## 1. API Client Extension
- [ ] 1.1 Add `get_document(document_id: int)` method to PaperlessAPI class
- [ ] 1.2 Add `get_similar_documents(document_id: int, page: int, page_size: int)` method to PaperlessAPI class
- [ ] 1.3 Add `list_tags()` method to PaperlessAPI class
- [ ] 1.4 Add `autocomplete_search(term: str, limit: int)` method to PaperlessAPI class
- [ ] 1.5 Add error handling for document not found (404) and other API errors

## 2. Tool Implementation
- [ ] 2.1 Implement `get_document_tool(document_id: int)` in tools.py
- [ ] 2.2 Implement `format_single_document(api_response: dict)` helper function
- [ ] 2.3 Implement `get_similar_documents_tool(document_id: int, page: int, page_size: int)` in tools.py
- [ ] 2.4 Implement `list_tags_tool()` in tools.py
- [ ] 2.5 Implement `format_tags(api_response: dict)` helper function
- [ ] 2.6 Implement `autocomplete_search_tool(term: str, limit: int)` in tools.py
- [ ] 2.7 Add error handling for all tools

## 3. MCP Server Registration
- [ ] 3.1 Register `get_document` MCP tool in server.py
- [ ] 3.2 Register `get_similar_documents` MCP tool in server.py
- [ ] 3.3 Register `list_tags` MCP tool in server.py
- [ ] 3.4 Register `autocomplete_search` MCP tool in server.py
- [ ] 3.5 Add comprehensive docstrings for AI instructions on all tools

## 4. Documentation & Testing
- [ ] 4.1 Update README.md with all new tool examples
- [ ] 4.2 Test `get_document` with real Paperless instance
- [ ] 4.3 Test `get_similar_documents` with real Paperless instance
- [ ] 4.4 Test `list_tags` with real Paperless instance
- [ ] 4.5 Test `autocomplete_search` with real Paperless instance
- [ ] 4.6 Verify all tools work in VS Code MCP integration
- [ ] 4.7 Verify all tools work in LM Studio
