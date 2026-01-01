## ADDED Requirements

### Requirement: OpenWebUI MCP Server Configuration
The system SHALL provide configuration for OpenWebUI to connect to the Paperless-NGX MCP server via Streamable HTTP.

#### Scenario: Server registration in OpenWebUI
- **WHEN** the MCP server is added to OpenWebUI
- **THEN** it SHALL be configured with Type "MCP (Streamable HTTP)"
- **AND** it SHALL specify the HTTP endpoint URL
- **AND** it SHALL receive environment variables for PAPERLESS_API_URL and PAPERLESS_API_TOKEN

#### Scenario: HTTP endpoint accessibility
- **WHEN** OpenWebUI connects to the MCP server
- **THEN** the server SHALL be accessible via HTTP on the configured port
- **AND** it SHALL support MCP's Streamable HTTP protocol
- **AND** it SHALL respond to MCP protocol handshake over HTTP

### Requirement: Tool Discovery in OpenWebUI
The system SHALL allow OpenWebUI to discover and invoke available MCP tools.

#### Scenario: Tool listing
- **WHEN** OpenWebUI queries available tools
- **THEN** the server SHALL return search_documents tool
- **AND** it SHALL include tool description and parameter schema
- **AND** OpenWebUI SHALL display the tool to users

#### Scenario: Tool invocation from OpenWebUI
- **WHEN** a user in OpenWebUI invokes search_documents
- **THEN** the server SHALL receive the tool call via HTTP
- **AND** it SHALL execute the search against Paperless-NGX API
- **AND** it SHALL stream results back to OpenWebUI
- **AND** OpenWebUI SHALL display the formatted results

### Requirement: Configuration Documentation
The system SHALL document how to configure the MCP server in OpenWebUI.

#### Scenario: Setup instructions
- **WHEN** a user reads the documentation
- **THEN** it SHALL explain how to add MCP server to OpenWebUI settings
- **AND** it SHALL provide example server URL (e.g., http://localhost:8080)
- **AND** it SHALL document required environment variables
- **AND** it SHALL explain how to start the server in HTTP mode

#### Scenario: Troubleshooting guide
- **WHEN** OpenWebUI cannot connect to the server
- **THEN** documentation SHALL provide debugging steps
- **AND** it SHALL explain how to verify the server is running
- **AND** it SHALL document common connection issues
