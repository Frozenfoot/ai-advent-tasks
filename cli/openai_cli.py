"""
Минимальный пример: запрос к OpenAI API (CLI)
Запуск из корня проекта: python -m cli.openai_cli "Ваш вопрос"
                         python -m cli.openai_cli "Ваш вопрос" --model lite
"""
import argparse
from dotenv import load_dotenv
from providers import openai_api
from utils.formatting import format_stats


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Отправить запрос к OpenAI API")
    parser.add_argument("prompt", help="Текст запроса")
    parser.add_argument(
        "--model",
        choices=openai_api.MODELS.keys(),
        default=openai_api.DEFAULT_MODEL,
        help="Модель: pro (gpt-5.4) или lite (gpt-5-mini). По умолчанию: pro",
    )
    args = parser.parse_args()
    r = openai_api.ask(args.prompt, model=args.model)
    print(r.text)
    print(format_stats(r))


if __name__ == "__main__":
    main()
