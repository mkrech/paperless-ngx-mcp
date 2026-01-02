# document-search Specification

## Purpose
TBD - created by archiving change add-paperless-mcp-server. Update Purpose after archive.
## Requirements
### Requirement: Document Search Tool
The system SHALL provide an MCP tool that searches Paperless-NGX documents by query string.

#### Scenario: Basic search
- **WHEN** search_documents is called with query="invoice"
- **THEN** it SHALL query the Paperless-NGX API with the search term
- **AND** it SHALL return matching documents with id, title, content preview
- **AND** it SHALL include correspondent, document_type, tags, and created date
- **AND** it SHALL format results as a readable JSON string

#### Scenario: Paginated results
- **WHEN** search_documents is called with page=2 and page_size=10
- **THEN** it SHALL request the specified page from the API
- **AND** it SHALL include pagination metadata (total count, next/previous)
- **AND** it SHALL indicate current page and total pages in the response

#### Scenario: Empty results
- **WHEN** search_documents is called with a query that matches no documents
- **THEN** it SHALL return a response indicating 0 results found
- **AND** it SHALL not raise an error for empty results

#### Scenario: Default pagination
- **WHEN** search_documents is called without page or page_size parameters
- **THEN** it SHALL use page=1 and page_size=25 as defaults
- **AND** it SHALL return up to 25 results from the first page

### Requirement: Response Formatting
The system SHALL format search results in a structured, readable manner for AI consumption.

#### Scenario: Document information
- **WHEN** documents are returned from search
- **THEN** each document SHALL include: id, title, content (preview), correspondent, document_type, tags, created_date, original_file_name
- **AND** content previews SHALL be truncated to first 200 characters if longer
- **AND** null fields SHALL be represented as "None" or omitted

#### Scenario: Metadata inclusion
- **WHEN** search results are formatted
- **THEN** the response SHALL include total document count
- **AND** it SHALL indicate if more pages are available
- **AND** it SHALL show current page number and page size

### Requirement: Get Document by ID
The system SHALL provide an MCP tool that retrieves a single document's complete details by its ID.

#### Scenario: Retrieve existing document
- **WHEN** get_document is called with a valid document_id
- **THEN** it SHALL fetch the document from Paperless-NGX API endpoint `/api/documents/{id}/`
- **AND** it SHALL return complete document information including full content
- **AND** it SHALL include all metadata: title, correspondent, document_type, tags, storage_path, custom fields
- **AND** it SHALL format the result as a readable JSON string

#### Scenario: Document not found
- **WHEN** get_document is called with a non-existent document_id
- **THEN** it SHALL return an error message indicating the document was not found
- **AND** it SHALL include the requested document_id in the error response
- **AND** it SHALL not raise an unhandled exception

#### Scenario: Complete metadata retrieval
- **WHEN** a document is retrieved successfully
- **THEN** it SHALL include: id, title, content (full text), correspondent, document_type, tags, created_date, modified_date, added_date
- **AND** it SHALL include storage_path, archive_serial_number, original_file_name
- **AND** it SHALL include custom_fields if present
- **AND** it SHALL include notes if present

### Requirement: Find Similar Documents
The system SHALL provide an MCP tool that finds documents similar to a given document using Paperless-NGX's similarity algorithm.

#### Scenario: Find similar documents
- **WHEN** get_similar_documents is called with a valid document_id
- **THEN** it SHALL query the Paperless-NGX API with `more_like_id` parameter
- **AND** it SHALL return documents similar to the reference document
- **AND** it SHALL format results in the same structure as search_documents
- **AND** it SHALL include pagination support (page, page_size)

#### Scenario: No similar documents found
- **WHEN** get_similar_documents is called and no similar documents exist
- **THEN** it SHALL return a response indicating 0 similar documents found
- **AND** it SHALL include the reference document_id in the response
- **AND** it SHALL not raise an error for empty results

#### Scenario: Similar documents pagination
- **WHEN** get_similar_documents is called with page=2 and page_size=10
- **THEN** it SHALL request the specified page from the API
- **AND** it SHALL include pagination metadata (total count, next/previous)
- **AND** it SHALL use default values page=1 and page_size=25 if not specified

#### Scenario: Reference document not found
- **WHEN** get_similar_documents is called with a non-existent document_id
- **THEN** it SHALL return an error message indicating the reference document was not found
- **AND** it SHALL include the requested document_id in the error response

### Requirement: List Tags
The system SHALL provide an MCP tool that retrieves all available tags from Paperless-NGX.

#### Scenario: Retrieve all tags
- **WHEN** list_tags is called
- **THEN** it SHALL fetch all tags from Paperless-NGX API endpoint `/api/tags/`
- **AND** it SHALL return tags with id, name, color, and document_count
- **AND** it SHALL format the result as a readable JSON array

#### Scenario: No tags available
- **WHEN** list_tags is called and no tags exist in Paperless
- **THEN** it SHALL return an empty array
- **AND** it SHALL indicate that 0 tags were found
- **AND** it SHALL not raise an error

#### Scenario: Tag metadata inclusion
- **WHEN** tags are retrieved
- **THEN** each tag SHALL include: id, name, color (hex color code), text_color
- **AND** it SHALL include the count of documents associated with each tag
- **AND** it SHALL return tags in the order provided by the API

### Requirement: Autocomplete Search
The system SHALL provide an MCP tool that suggests search terms based on the document index.

#### Scenario: Get search suggestions
- **WHEN** autocomplete_search is called with term="tel"
- **THEN** it SHALL query the Paperless-NGX API endpoint `/api/search/autocomplete/`
- **AND** it SHALL return search term suggestions based on TF/IDF scoring
- **AND** it SHALL return results ordered by relevance (highest score first)
- **AND** it SHALL format results as a JSON array of suggested terms

#### Scenario: Limit suggestions
- **WHEN** autocomplete_search is called with limit=5
- **THEN** it SHALL request only 5 suggestions from the API
- **AND** it SHALL return at most 5 suggested terms
- **AND** it SHALL use default limit=10 if not specified

#### Scenario: No suggestions found
- **WHEN** autocomplete_search is called with a term that has no matches
- **THEN** it SHALL return an empty array
- **AND** it SHALL indicate that 0 suggestions were found
- **AND** it SHALL not raise an error

#### Scenario: Empty term handling
- **WHEN** autocomplete_search is called with an empty or very short term
- **THEN** it SHALL pass the term to the API without modification
- **AND** it SHALL return whatever suggestions the API provides
- **AND** it SHALL handle the response gracefully

