# matte-claude-plugin

Claude Code plugin that connects Claude to your Meta, TikTok, Google Ads, and GA4 advertising data via [MatteMena](https://www.mattemena.com/).

This repo contains only the plugin packaging (`.claude-plugin/`) and the built MCP server bundle (`dist/stdio.bundle.cjs`). The actual MCP server source lives in a separate, private repo.

## Install

1. Sign up at [nerve.mattemena.com](https://nerve.mattemena.com/) and connect your Meta / TikTok / Google Ads / GA4 accounts.
2. Copy your MatteMena API key from the dashboard.
3. In Claude Code: **Add marketplace → Add from a repository** → `https://github.com/MatteMena/matte-claude-plugin`
4. Install the `mattemena-connect` plugin and paste your API key when prompted.

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
