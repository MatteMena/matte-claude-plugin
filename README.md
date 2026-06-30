# matte-claude-plugin

Claude Code plugin that connects Claude to your Meta, TikTok, Google Ads, and GA4 advertising data via [MatteMena](https://www.mattemena.com/).

This repo contains only the plugin packaging (`.claude-plugin/`) and the built MCP server bundle (`dist/stdio.bundle.cjs`). The actual MCP server source lives in a separate, private repo.

The plugin declares one MCP server connector:

- **`mattemena-remote`** (hosted): connects to `https://test-mcp.nerve.mattemena.com/mcp`, a remote HTTP MCP server with a full OAuth 2.0 + PKCE flow. No API key in config — authenticate via the connector's own login page when prompted.

> The bundled local connector (`mattemena-local`, running `dist/stdio.bundle.cjs` directly via `userConfig.api_key`) is temporarily disabled. To re-enable it, restore this block under `mcpServers` in `.claude-plugin/plugin.json` (and the matching `userConfig.api_key` block) — see git history for the exact config.
> ```json
> "mattemena-local": {
>   "command": "node",
>   "args": ["${CLAUDE_PLUGIN_ROOT}/dist/stdio.bundle.cjs"],
>   "env": {
>     "MCP_API_KEY": "${user_config.api_key}",
>     "API_BASE_URL": "https://ap-southeast-1-test-api.connect.platformance.io",
>     "TOOL_DISCOVERY_MODE": "true"
>   }
> }
> ```

## Install

1. Sign up at [nerve.mattemena.com](https://nerve.mattemena.com/) and connect your Meta / TikTok / Google Ads / GA4 accounts.
2. In Claude Code: **Add marketplace → Add from a repository** → `https://github.com/MatteMena/matte-claude-plugin`
3. Install the `mattemena-nerve` plugin and authenticate via the `mattemena-remote` connector's login page when prompted.

## Releasing an update

Whenever the MCP server source changes (in the private `pf-mcp-server` repo):

1. In `pf-mcp-server`, run `npm run bundle:stdio` to rebuild `dist/stdio.bundle.cjs`.
2. Copy the rebuilt `dist/stdio.bundle.cjs` into this repo's `dist/`.
3. Bump `version` in `.claude-plugin/plugin.json`.
4. Commit, tag, and push:
   ```
   git add -A
   git commit -m "release: vX.Y.Z"
   git tag vX.Y.Z
   git push origin main --tags
   ```

## License

MIT
