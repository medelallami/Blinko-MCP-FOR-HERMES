# Blinko MCP Server Documentation

## Overview

This document provides documentation for the Blinko MCP (Model Context Protocol) server running at `http://<YOUR_SERVER_IP>:<PORT>/mcp`.

## Server Information

- **URL**: http://<YOUR_SERVER_IP>:<PORT>/mcp
- **Protocol**: MCP (Model Context Protocol)
- **Transport**: HTTP with JSON payloads
- **Authentication**: Bearer token via Authorization header

## Connection Details

To connect to this MCP server, clients should:

1. Send HTTP requests to `http://<YOUR_SERVER_IP>:<PORT>/mcp`
2. Include an Authorization header with a valid Bearer token
3. Use JSON-RPC 2.0 format for MCP messages

### Example Connection Header

```
Authorization: Bearer <YOUR_TOKEN>
Content-Type: application/json
Accept: application/json, text/event-stream
```

## Server Response (Verify Connection)

Upon successful initialization, the server responds with:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "tools": {
        "listChanged": true
      }
    },
    "serverInfo": {
      "name": "blinko-mcp-server",
      "version": "1.0.0"
    }
  }
}
```

## Available Tools

The Blinko MCP server provides 10 tools:

### 1. searchBlinko

**Description**: Search note or blinko from blinko api.
**Input Properties**:

- searchText (string): Text to search for
- page (number): Page number for pagination
- size (number): Number of results per page
- orderBy (string): Field to sort by
- type (string): Content type filter
- isArchived (boolean): Filter by archived status
- isRecycle (boolean): Filter by recycle bin status
- withoutTag (string): Exclude notes with this tag
- withFile (boolean): Filter notes with attachments
- withLink (boolean): Filter notes with links
- isUseAiQuery (boolean): Use AI-enhanced search
- days (number): Limit search to last N days
- hasTodo (boolean): Filter notes with todos
- token (string): Authentication token

### 2. upsertBlinko

**Description**: Create different types of content. "Blinko" means flash thoughts or sudden inspiration - those fleeting ideas that pop into mind.
**Input Properties**:

- content (string): The content to create
- type (string): Type of content (e.g., "note", "document", "article")
- token (string): Authentication token

### 3. updateBlinko

**Description**: Update blinko and save to database.
**Input Properties**:

- id (string): ID of the blinko to update
- content (string): New content
- type (string): Content type
- isArchived (boolean): Archive status
- isTop (boolean): Pin to top
- isShare (boolean): Share status
- isRecycle (boolean): Move to recycle bin
- token (string): Authentication token

### 4. deleteBlinko

**Description**: Delete blinko and save to database.
**Input Properties**:

- ids (string/array): ID(s) of blinko to delete
- token (string): Authentication token

### 5. createComment

**Description**: Create a comment on a note.
**Input Properties**:

- content (string): Comment content
- noteId (string): ID of the note to comment on
- guestName (string): Name of guest commenter
- token (string): Authentication token

### 6. webSearch

**Description**: Web search assistant.
**Input Properties**:

- query (string): Search query

### 7. webExtra

**Description**: Web scraping assistant who can use the Jina API to crawl and analyze web content.
**Input Properties**:

- urls (string/array): URLs to scrape

### 8. createScheduledTask

**Description**: Create a scheduled task that will run automatically at specified times.
**Input Properties**:

- name (string): Task name
- prompt (string): What the AI will execute when the task runs
- schedule (string): Cron format schedule
  - Examples:
    - "0 10 * * *" - Every day at 10:00 AM
    - "0 9 * * 1" - Every Monday at 9:00 AM
    - "0 */6 * * *" - Every 6 hours
    - "0 0 1 * *" - First day of every month at midnight
- token (string): Authentication token

### 9. deleteScheduledTask

**Description**: Delete an existing scheduled task by its ID or name.
**Input Properties**:

- taskId (string): Task ID
- taskName (string): Task name
- token (string): Authentication token

### 10. listScheduledTasks

**Description**: List all scheduled tasks for the current user.
**Input Properties**:

- token (string): Authentication token

## Example Usage

### Initializing Connection

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {
      "name": "hermes-agent",
      "version": "1.0.0"
    }
  }
}
```

### Listing Tools

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list"
}
```

### Calling a Tool (e.g., upsertBlinko to create a note)

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "upsertBlinko",
    "arguments": {
      "content": "# Your Note Title\n\nYour note content goes here...",
      "type": "note",
      "token": "<YOUR_TOKEN>"
    }
  }
}
```

## Authentication

This server requires Bearer token authentication. The token should be obtained through your Blinko account and provided in the Authorization header as shown in the examples above.

## Troubleshooting

- **Connection refused**: Ensure the server is running at http://<YOUR_SERVER_IP>:<PORT>
- **Unauthorized (401)**: Check that your Authorization header contains a valid Bearer token
- **Method not found**: Verify that the MCP method you're calling is implemented by the server
- **Invalid JSON**: Ensure all requests are valid JSON-RPC 2.0
- **406 Not Acceptable**: Client must accept both application/json and text/event-stream in the Accept header
- **Bad Request: Streamable HTTP sessions must start with initialize**: When using streamable HTTP transport, the first request must be an initialize request

## Notes

- This documentation was created by successfully connecting to the Blinko MCP server and discovering its capabilities via MCP protocol
- Actual capabilities confirmed via live MCP session
- For use with Hermes Agent MCP client and other MCP-compatible clients
- The upsertBlinko tool with type="note" is recommended for creating documentation notes

---

*Documentation generated: 2026-06-21 13:10:00 UTC*
*For use with Hermes Agent MCP client*
