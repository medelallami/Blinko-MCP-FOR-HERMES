# Blinko MCP Server Documentation (Enterprise Edition)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![MCP Protocol](https://img.shields.io/badge/MCP-v2024--11--05-orange.svg)](https://modelcontextprotocol.io)

Welcome to the enterprise-grade **Blinko Model Context Protocol (MCP) Server** documentation repository. This project provides secure, scalable integration patterns, code examples, and deployment best practices for connecting AI agents—such as the Hermes Agent—to your Blinko infrastructure.

## 📑 Table of Contents

- [Overview](#overview)
- [Architecture & Server Information](#architecture--server-information)
- [Available Tools](#available-tools)
- [Enterprise Documentation & Guides](#enterprise-documentation--guides)
- [Code Examples](#code-examples)

---

## 🚀 Overview

The Blinko MCP server creates a secure, standardized bridge between advanced AI agents and your internal Blinko instance. It provides fine-grained tools for comprehensive workspace management, including creating, updating, and searching notes, managing automated scheduled tasks, and executing web content analysis.

## 🏗️ Architecture & Server Information

- **URL Endpoint**: `http://<YOUR_SERVER_IP>:<PORT>/mcp`
- **Protocol**: MCP (Model Context Protocol) `v2024-11-05`
- **Transport**: Standardized HTTP bridging with JSON-RPC 2.0 payloads
- **Authentication**: Enterprise Bearer token validation via `Authorization` headers
- **Session Management**: Native tracking via `Mcp-Session-Id` headers

## 🛠️ Available Tools

The Blinko MCP server empowers agents with the following suite of tools:

1. **`searchBlinko`**: Search for notes using filters or AI-enhanced semantic queries.
2. **`upsertBlinko`**: Provision new content entities (notes, documents, articles).
3. **`updateBlinko`**: Mutate existing content or transition state (e.g., archive, pin).
4. **`deleteBlinko`**: Soft-delete content to the recycle bin.
5. **`createComment`**: Append nested comments to active notes.
6. **`webSearch`**: Trigger agentic web searches.
7. **`webExtra`**: Execute web scraping and unstructured content analysis via Jina API.
8. **`createScheduledTask`**: Provision CRON-based automated agents tasks.
9. **`deleteScheduledTask`**: Teardown scheduled automation tasks.
10. **`listScheduledTasks`**: Audit active scheduled operations.

For a comprehensive data dictionary and input schema reference, see our [Examples Guide](./docs/examples.md).

## 📚 Enterprise Documentation & Guides

Security and scalability are at the core of this repository. Please review the following technical guides before deploying your integration:

- 🛡️ **[Secure Credential Storage](./docs/secure_credentials.md)**: Enterprise best practices for Vault/Secrets-manager token injection and avoiding leakage.
- ⚙️ **[Hermes Configuration](./docs/hermes_configuration.md)**: Guidelines for configuring the Hermes Agent safely within corporate deployments.
- 🔒 **[Security Policy](./SECURITY.md)**: Vulnerability disclosure policies.

## 💻 Code Examples

To accelerate developer onboarding, we supply production-ready code examples:

- **[Python (httpx + asyncio)](./examples/python_example.py)**: A robust asynchronous connection pattern.
- **[cURL (Raw HTTP)](./examples/curl_example.sh)**: Low-level reference architecture for shell automation.

---

*Engineered for scale. Powered by the Model Context Protocol.*
