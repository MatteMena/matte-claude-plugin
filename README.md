# matte-claude-plugin

Claude Code plugin that connects Claude to your Meta, TikTok, Google Ads, and GA4 advertising data via [MatteMena](https://www.mattemena.com/).

This repo contains only the plugin packaging (`.claude-plugin/`) and the plugin's skills (`skills/`). The actual MCP server source lives in a separate, private repo.

The plugin declares one MCP server connector:

- **`mattemena-remote`** (hosted): connects to `https://mcp.nerve.mattemena.com/mcp`, a remote HTTP MCP server with a full OAuth 2.0 + PKCE flow. No API key in config — authenticate via the connector's own login page when prompted.

> The bundled local connector (`mattemena-local`) has been removed, along with `dist/stdio.bundle.cjs`. Both remain in git history.

## Install

1. Sign up at [nerve.mattemena.com](https://nerve.mattemena.com/) and connect your Meta / TikTok / Google Ads / GA4 accounts.
2. In Claude Code: **Add marketplace → Add from a repository** → `https://github.com/MatteMena/matte-claude-plugin`
3. Install the `mattemena-nerve` plugin and authenticate via the `mattemena-remote` connector's login page when prompted.

## Releasing an update

Whenever the plugin's manifests or skills change:

1. Bump `version` in `.claude-plugin/plugin.json`.
2. Commit, tag, and push:
   ```
   git add -A
   git commit -m "release: vX.Y.Z"
   git tag vX.Y.Z
   git push origin main --tags
   ```

Don't commit binaries, bundles, or build output to `main`: every push is re-scanned by the Claude plugin directory, and files it can't read hold the version back.

## License

MIT
