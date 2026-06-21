# Blinko MCP Server Documentation

Welcome to the Blinko Model Context Protocol (MCP) Server documentation repository! This repository contains documentation, examples, and best practices for connecting to and interacting with the Blinko MCP server, especially via the Hermes Agent.

## Table of Contents

- [Overview](#overview)
- [Server Information](#server-information)
- [Available Tools](#available-tools)
- [Documentation & Guides](#documentation--guides)
- [Code Examples](#code-examples)

---

## Overview

The Blinko MCP server enables AI agents (like Hermes) to seamlessly interact with your Blinko instance. It provides tools for creating, updating, and searching notes, managing scheduled tasks, and interacting with the web.

## Server Information

- **URL**: `http://<YOUR_SERVER_IP>:<PORT>/mcp`
- **Protocol**: MCP (Model Context Protocol) v2024-11-05
- **Transport**: HTTP with JSON payloads
- **Authentication**: Bearer token via Authorization header

## Available Tools

The Blinko MCP server provides the following capabilities:

1. **`searchBlinko`**: Search for notes using filters or AI queries.
2. **`upsertBlinko`**: Create new content (notes, documents, articles).
3. **`updateBlinko`**: Update existing content or change its status (e.g., archive, pin).
4. **`deleteBlinko`**: Move content to the recycle bin.
5. **`createComment`**: Add comments to notes.
6. **`webSearch`**: Web search assistant.
7. **`webExtra`**: Web scraping and content analysis via Jina API.
8. **`createScheduledTask`**: Create automated, scheduled tasks using cron syntax.
9. **`deleteScheduledTask`**: Remove scheduled tasks.
10. **`listScheduledTasks`**: List your active scheduled tasks.

For detailed input properties of each tool, refer to our [API Reference](./docs/examples.md).

## Documentation & Guides

To help you get started securely and configure your clients, check out our guides:

- 🛡️ **[Secure Credential Storage](./docs/secure_credentials.md)**: Best practices for handling and storing your Bearer tokens.
- ⚙️ **[Hermes Configuration](./docs/hermes_configuration.md)**: How to configure the Hermes Agent to connect to Blinko MCP.

## Code Examples

We provide code examples to help you build custom integrations with the Blinko MCP Server:

- **[Python Example](./examples/python_example.py)**: A complete script using `httpx` and `asyncio` to connect and create a note.
- **[cURL Example](./examples/curl_example.sh)**: A shell script demonstrating raw HTTP requests to the MCP server.
- **[Example Usage Guide](./docs/examples.md)**: A walkthrough of the initialization and tool calling process.

---

*For use with Hermes Agent MCP client and other MCP-compatible clients.*
