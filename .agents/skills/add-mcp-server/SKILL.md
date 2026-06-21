---
name: add-mcp-server
description: Add an MCP server to Hermes configuration (URL only) due to security restrictions on headers.
category: hermes
---

## Overview
This skill adds an MCP (Model Context Protocol) server entry to Hermes configuration. Because Hermes redacts Authorization header values in the configuration file for security, only the URL can be stored directly. Authentication must be handled via external secure means (e.g., environment variables, Hermes credential store).

## Steps
1. **Locate the Hermes configuration file** 
   Typically found at `~/.hermes/config.yaml` (or `/opt/data/config.yaml` in some deployments).

2. **Add the MCP server entry** 
   Under the top-level `mcpServers` key, add a block for your server:
   ```yaml
   mcpServers:
     <server-name>:
       url: <http://host:port/path>
   ```
   Replace `<server-name>` with a unique identifier (e.g., `blinko`) and `<url>` with the MCP server endpoint.

3. **Handle authentication securely** 
   If the MCP server requires an Authorization header or other credentials:
   - Store the token or credential in Hermes' credential store (`~/.hermes/.env`) using secure methods outside of this skill.
   - Alternatively, set an environment variable that the MCP server or Hermes can read.
   - Do **not** attempt to write `headers:` with Authorization directly into the config file; it will be redacted to `***`.

4. **Verify the configuration** 
   After saving, check that the entry appears correctly:
   ```sh
   grep -A2 "<server-name>:" ~/.hermes/config.yaml
   ```

5. **Test the MCP connection** (if applicable)
   Some MCP servers require specific headers or handling:
   - For Streamable HTTP transports, ensure your client accepts both `application/json` and `text/event-stream`
   - The first request must be an `initialize` method call
   - Subsequent requests should include the `Mcp-Session-Id` header if provided by the server
   - Refer to the server's documentation for specific requirements

6. **Restart Hermes (if required)** 
   Depending on your deployment, restart the Hermes service or reload its configuration for changes to take effect.

## Notes
- This skill intentionally omits handling of headers due to Hermes' security redaction.
- For troubleshooting authentication, consult Hermes logs or the MCP server's documentation.
- The skill does not modify any existing `headers:` sections; it only adds new server entries.
- See `references/blinko-mcp-details.md` for specific details about connecting to a Blinko MCP server.
- See `scripts/verify_mcp_connection.py` for a script to verify MCP server connections.
- For Blinko-specific MCP handling procedures (session management, dual token requirement, event-stream parsing), see the "Blinko-Specific MCP Handling Notes" section below.

---

## Blinko-Specific MCP Handling Notes
Based on successful verification with the Blinko MCP server at http://<YOUR_SERVER_IP>:<PORT>/mcp:

### Authentication Requirements
- The Authorization header **must** contain: `Authorization: Bearer <YOUR_TOKEN>`
- Additionally, many Blinko MCP tools require a `token` parameter in the tool arguments
- Both are required for successful tool calls

### Session Management
- After initialization, the server responds with `Mcp-Session-Id` header
- This header **must** be included in all subsequent requests as `Mcp-Session-Id: <session-id>`
- The session ID remains valid for the duration of the MCP connection

### Response Format
- Responses are delivered as `text/event-stream` (Server-Sent Events)
- Each event contains a `data:` line with JSON-RPC 2.0 formatted data
- Example response format:
  ```
  event: message
  data: {"jsonrpc":"2.0","result":{...},"id":2}
  ```

### Tool-Specific Notes for Blinko
- **upsertBlinko**: Use `type: "note"` for documentation/content
- **searchBlinko**: Returns results in a structured format with `content` array
- All tools require the `token` parameter in addition to header authentication

### Verification Steps That Worked
1. Initialize session with proper headers (including Accept: application/json, text/event-stream)
2. Extract Mcp-Session-Id from response headers
3. Call tools/call with:
   - Proper Authorization header
   - Mcp-Session-Id header (if received)
   - JSON-RPC 2.0 payload with tool name and arguments
   - Token included in both header and tool arguments
4. Parse event-stream response to extract JSON-RPC result

These details are documented in the Blinko-specific reference file: references/blinko-mcp-details.md
