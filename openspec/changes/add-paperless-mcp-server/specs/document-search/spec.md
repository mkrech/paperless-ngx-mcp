## ADDED Requirements

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
