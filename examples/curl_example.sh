#!/bin/bash

# Ensure you have set your token and server URL
TOKEN="<YOUR_TOKEN>"
URL="http://<YOUR_SERVER_IP>:<PORT>/mcp"

# Initialize
echo "Initializing..."
INIT_RESP=$(curl -i -s -X POST $URL \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2024-11-05",
      "capabilities": {},
      "clientInfo": {"name": "curl-test", "version": "1.0.0"}
    }
  }')

echo "$INIT_RESP"

# Extract session ID from headers
SESSION_ID=$(echo "$INIT_RESP" | grep -i 'mcp-session-id:' | awk '{print $2}' | tr -d '\r')

echo "Session ID: $SESSION_ID"

# Call upsertBlinko
echo "Calling upsertBlinko..."
curl -X POST $URL \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
      "name": "upsertBlinko",
      "arguments": {
        "content": "# Test Note\n\nCreated via curl",
        "type": "note",
        "token": "'$TOKEN'"
      }
    }
  }'
