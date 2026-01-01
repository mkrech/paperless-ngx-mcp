## ADDED Requirements

### Requirement: VS Code MCP Configuration
The system SHALL provide VS Code MCP server configuration for local testing.

#### Scenario: MCP server registration for stdio
- **WHEN** VS Code loads the workspace
- **THEN** the .vscode/mcp-server.json file SHALL define the paperless-ngx-mcp server
- **AND** it SHALL specify the command to start the server using uv run (stdio mode)
- **AND** it SHALL pass necessary environment variables
- **AND** it SHALL NOT specify a port (defaults to stdio)

#### Scenario: Environment variable configuration
- **WHEN** the MCP server is started from VS Code
- **THEN** it SHALL receive PAPERLESS_API_URL from the configuration
- **AND** it SHALL receive PAPERLESS_API_TOKEN from the configuration
- **AND** these values SHALL be configurable per developer environment

### Requirement: Development Documentation
The system SHALL document how to test and use the MCP server in VS Code.

#### Scenario: Setup instructions
- **WHEN** a developer reads the README
- **THEN** it SHALL explain how to configure .vscode/mcp-server.json
- **AND** it SHALL document the required environment variables
- **AND** it SHALL provide an example configuration

#### Scenario: Testing guidance
- **WHEN** a developer wants to test the MCP server (stdio)
- **AND** it SHALL provide example queries for search_documents
- **AND** it SHALL explain how to verify the server is working
- **AND** it SHALL document how to test HTTP streaming mode with --port flats
- **AND** it SHALL explain how to verify the server is working
