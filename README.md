# matte-claude-plugin

Claude Code plugin that connects Claude to your Meta, TikTok, Google Ads, and GA4 advertising data via [MatteMena](https://www.mattemena.com/).

This repo contains only the plugin packaging (`.claude-plugin/`) and the built MCP server bundle (`dist/stdio.bundle.cjs`). The actual MCP server source lives in a separate, private repo.

The plugin declares two MCP server connectors — pick whichever fits:

- **`mattemena-local`** (local): runs the bundled `dist/stdio.bundle.cjs` directly. Prompts for your API key at install (`userConfig.api_key`).
- **`mattemena-remote`** (hosted): connects to `https://test-mcp.nerve.mattemena.com/mcp`, a remote HTTP MCP server with a full OAuth 2.0 + PKCE flow. No API key in config — authenticate via the connector's own login page when prompted.

## Install

1. Sign up at [nerve.mattemena.com](https://nerve.mattemena.com/) and connect your Meta / TikTok / Google Ads / GA4 accounts.
2. Copy your MatteMena API key from the dashboard (only needed for the local `mattemena-local` connector).
3. In Claude Code: **Add marketplace → Add from a repository** → `https://github.com/MatteMena/matte-claude-plugin`
4. Install the `mattemena-connect` plugin, then enable whichever connector you prefer from the plugin's detail page.

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
