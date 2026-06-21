# Blinko MCP Hermes Configuration

## Configuration File Location
- `~/.hermes/config.yaml` (or `/opt/data/config.yaml` in some deployments)

## Minimal MCP Server Entry (Due to Security Redaction)
Because Hermes redacts Authorization header values in config files, only store the URL:

```yaml
mcpServers:
  blinko:
    url: http://<YOUR_SERVER_IP>:<PORT>/mcp
```

## Secure Token Storage
Store the Bearer token outside the config file, using:
- Hermes credential store (`~/.hermes/.env`) 
- Or environment variable `BLINKO_TOKEN`

Example `.env` entry:
```
BLINKO_TOKEN=<YOUR_TOKEN>
```

## Verification
After configuration, you can test the connection via Hermes MCP client or directly using the code examples above.

## Notes
- Do NOT attempt to add `headers:` with Authorization directly in config.yaml; it will be redacted to `***`
- The MCP client (Hermes or custom) must add the Authorization header at runtime from secure storage
- Ensure your MCP client accepts both `application/json` and `text/event-stream` in the Accept header
- Handle Mcp-Session-Id from initialization response for subsequent requests
