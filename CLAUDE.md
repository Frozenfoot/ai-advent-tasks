# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Minimal demo project showing how to call Claude (Anthropic) and OpenAI APIs. Three entry points: two CLI scripts and one Flask web UI.

## Setup

```bash
uv sync
```

Keys go in `.env` (copy from `.env.example`). Loaded automatically via `python-dotenv`.

## Running

All commands run from the project root:

```bash
uv run python -m cli.claude_cli "prompt"   # one-shot Claude request
uv run python -m cli.openai_cli "prompt"   # one-shot OpenAI request
uv run python -m cli.openai_cli "prompt" --model lite
uv run python -m web.app                   # Flask web UI at http://localhost:5000
```

## Architecture

```
providers/          # shared API wrappers
cli/                # CLI entry points
web/                # Flask app
  templates/        # HTML/CSS/JS (index.html)
```

- **providers/claude_api.py** / **providers/openai_api.py**: Each exposes `ask(prompt: str) -> str`. Model name is a `MODEL` constant at the top. API keys are read from env automatically by the SDK client.
- **cli/**: Thin scripts that call the matching provider and print the result.
- **web/app.py**: Flask app with two routes — `GET /` renders `templates/index.html`, `POST /ask` delegates to `claude_api.ask()` or `openai_api.ask()` based on a `provider` field (`"claude"` or `"openai"`). Stateless — no conversation history.
- **web/templates/index.html**: Self-contained UI (HTML + CSS + JS). Sends `POST /ask` with `{prompt, provider}` and appends the response to the message list.

## Dependencies

| Package | Version |
|---------|---------|
| anthropic | >=0.40.0 |
| openai | >=1.50.0 |
| flask | >=3.0.0 |
