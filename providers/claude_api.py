"""
Обёртка над Claude API (Anthropic).
Клиент берёт ключ из переменной окружения ANTHROPIC_API_KEY (загружается из .env).
"""
import anthropic
from dotenv import load_dotenv
from providers.response import LLMResponse
from utils.timing import measure

load_dotenv()

MODEL = "claude-sonnet-4-20250514"


@measure
def ask(prompt: str, max_tokens: int = 1024) -> LLMResponse:
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return LLMResponse(
        text=response.content[0].text,
        model=response.model,
        provider="claude",
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
    )
