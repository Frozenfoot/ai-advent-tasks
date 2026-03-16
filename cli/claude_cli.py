"""
Минимальный пример: запрос к Claude API (CLI)
Запуск из корня проекта: python -m cli.claude_cli "Ваш вопрос"
"""
import argparse
from providers import claude_api


def main():
    parser = argparse.ArgumentParser(description="Отправить запрос к Claude API")
    parser.add_argument("prompt", help="Текст запроса")
    args = parser.parse_args()
    r = claude_api.ask(args.prompt)
    print(r.text)
    print(f"\n[{r.model}] in: {r.input_tokens} / out: {r.output_tokens} tokens")


if __name__ == "__main__":
    main()
