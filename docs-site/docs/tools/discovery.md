---
id: discovery
title: Tool Discovery Mode
sidebar_position: 9
---

# Tool Discovery Mode

MatteMena supports two modes controlled by the `TOOL_DISCOVERY_MODE` environment variable.

## Modes

| Mode | Tools Exposed | Best For |
|------|--------------|---------|
| **Tool Discovery** (default) | 4 discovery meta-tools | Claude.ai, Claude Code — AI picks tools automatically |
| **Legacy** | 185+ individual tools | Direct programmatic access |

## The 4 Discovery Tools

### `search-tools`

Searches the tool registry by natural language query and returns a list of matching tools.

**When Claude uses it:** When you ask something like "show me Meta campaign performance" — Claude first searches for relevant tools and finds `get-campaigns`, `get-insights`, etc.

```
Input:  { "query": "meta campaign performance" }
Output: List of matching tool names with descriptions
```

---

### `multi-execute`

Executes multiple tools in parallel in a single call.

**When Claude uses it:** After finding the right tools via `search-tools`, Claude batches multiple calls into one `multi-execute` call for efficiency.

```
Input:  { "tools": [{ "name": "get-campaigns", "params": {...} }, { "name": "get-insights", "params": {...} }] }
Output: Combined results from all tool calls
```

---

### `get-tool-schemas`

Returns the full JSON Schema (parameter definitions) for one or more tools.

**When Claude uses it:** When Claude needs to know exactly what parameters a tool requires before calling it.

```
Input:  { "toolNames": ["create-meta-campaign"] }
Output: Full JSON Schema for each requested tool
```

---

### `check-connections`

Returns the list of platforms you have connected and the account IDs available.

**When Claude uses it:** At the start of a session to understand which platforms and accounts are available.

```
Input:  {}
Output: { "meta": ["act_123456"], "tiktok": ["advertiser_789"], ... }
```

---

## Why Discovery Mode?

With 185+ tools, Claude's context window would fill up just listing them all. Discovery Mode solves this:

1. **Less context usage** — only 4 tools in the system prompt instead of 185
2. **Parallel execution** — `multi-execute` runs multiple tools simultaneously
3. **Semantic search** — finds the right tool even with vague queries
4. **Platform-aware** — `check-connections` ensures Claude only calls tools for connected platforms

## Skill Tools

In discovery mode, **Skill Tools** (cross-platform workflows) are automatically included in the search index. You can discover and execute them with the same `search-tools` / `multi-execute` interface.

Example skill: "Run a cross-platform performance report comparing Meta, TikTok, and Google Ads for the last 30 days."
