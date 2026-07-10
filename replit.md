# Lodi Bot

## Overview
Lodi Bot is a Discord bot for managing Basketball GM (BBGM) multiplayer leagues — drafts, trades, free agency, and stats tracking. Hobby project; see `CLAUDE.md` for full architecture/module notes.

**Stack:** Python 3.12, discord.py, Plotly/Kaleido for graphs, Dropbox API for file sharing, JSON files for data persistence.

## Running on Replit
- Workflow: `Lodi Bot` runs `python main.py` (console output, no port needed — it's a Discord bot, not a web server).
- Requires the `DISCORD_TOKEN` secret (already configured). The bot also supports `SENTRY_DSN`, `DROPBOX_REFRESH_TOKEN`, `DROPBOX_CLIENT_ID`, `DROPBOX_CLIENT_SECRET` as optional env vars; without them it falls back to local `.txt` files (dropbox.txt) or runs without those features.
- `servers.json` (per-server config, gitignored) is created automatically at runtime by `checks.py` if missing — a placeholder `{}` was seeded so the bot doesn't hang waiting for it.

## Recent changes
- 2026-07-10: Imported from GitHub and set up to run on Replit — installed Python deps from `requirements.txt`, configured the `Lodi Bot` workflow, added `DISCORD_TOKEN` secret, seeded empty `servers.json`, and fixed a `KeyError: 'offers'` crash in `basics.clean_priorities` that fired on every startup for servers without FA offers data.
