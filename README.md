# Минимальные примеры работы с LLM API

Код, который отправляет запрос в LLM через API и выводит ответ.
Варианты: **Claude (Anthropic)** и **OpenAI (GPT)** — CLI и Web-интерфейс.

## Структура

```
providers/        # обёртки над API (общие для CLI и Web)
cli/              # CLI-скрипты
web/              # Flask web-интерфейс
  templates/      # HTML/CSS/JS
```

## Установка

```bash
uv sync
```

Скопируйте `.env.example` в `.env` и вставьте ключи:

```
ANTHROPIC_API_KEY=sk-ant-api03-...
OPENAI_API_KEY=sk-proj-...

# Опционально — прокси
# HTTPS_PROXY=http://user:password@host:port
```

Получить ключи: [console.anthropic.com](https://console.anthropic.com) и [platform.openai.com/api-keys](https://platform.openai.com/api-keys).

## Запуск

```bash
# Claude
uv run python -m cli.claude_cli "Ваш вопрос"

# OpenAI (pro = gpt-5.4, lite = gpt-5-mini)
uv run python -m cli.openai_cli "Ваш вопрос"
uv run python -m cli.openai_cli "Ваш вопрос" --model lite

# Web-интерфейс → http://localhost:5000
uv run python -m web.app
```
