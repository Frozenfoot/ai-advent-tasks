"""
Обёртка над Claude API (Anthropic).
Клиент берёт ключ из переменной окружения ANTHROPIC_API_KEY.
"""
import anthropic
from functools import lru_cache
from models.response import LLMResponse
from utils.timing import measure

MODEL = "claude-sonnet-4-20250514"


@lru_cache(maxsize=1)
def _client() -> anthropic.Anthropic:
    return anthropic.Anthropic()


@measure
def ask(prompt: str, max_tokens: int = 1024) -> LLMResponse:
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    response = _client().messages.create(
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
