"""
Минимальный пример: запрос к Claude API (CLI)
Запуск из корня проекта: python -m cli.claude_cli "Ваш вопрос"
"""
import argparse
from dotenv import load_dotenv
from providers import claude_api
from utils.formatting import format_stats


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Отправить запрос к Claude API")
    parser.add_argument("prompt", help="Текст запроса")
    args = parser.parse_args()
    r = claude_api.ask(args.prompt)
    print(r.text)
    print(format_stats(r))


if __name__ == "__main__":
    main()
