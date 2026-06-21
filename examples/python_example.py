import asyncio, json, re
import httpx

TOKEN="<YOUR_TOKEN>"
URL = "http://<YOUR_SERVER_IP>:<PORT>/mcp"

async def call_blinko():
    async with httpx.AsyncClient(timeout=30.0) as client:
        # Initialize
        init_resp = await client.post(
            URL,
            json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {"name": "test-client", "version": "1.0.0"}
                }
            },
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream"
            }
        )
        # Extract session ID
        session_id = init_resp.headers.get('mcp-session-id')
        print(f"Session ID: {session_id}")
        
        # Call upsertBlinko to create a note
        upsert_resp = await client.post(
            URL,
            json={
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {
                    "name": "upsertBlinko",
                    "arguments": {
                        "content": "# Test Note\n\nThis is a test note created via MCP.",
                        "type": "note",
                        "token": TOKEN
                    }
                }
            },
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
                **({'Mcp-Session-Id': session_id} if session_id else {})
            }
        )
        print(f"Upsert status: {upsert_resp.status_code}")
        # Parse event-stream response
        if upsert_resp.headers.get('content-type', '').startswith('text/event-stream'):
            text = upsert_resp.text
            match = re.search(r'data: (\{.*\})', text, re.DOTALL)
            if match:
                result = json.loads(match.group(1))
                print(json.dumps(result, indent=2))

if __name__ == "__main__":
    asyncio.run(call_blinko())
