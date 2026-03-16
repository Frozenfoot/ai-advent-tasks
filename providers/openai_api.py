"""
Обёртка над OpenAI API.
Клиент берёт ключ из переменной окружения OPENAI_API_KEY.
"""
import openai
from functools import lru_cache
from models.response import LLMResponse
from utils.timing import measure

MODELS = {
    "pro":  "gpt-5.4",
    "lite": "gpt-5-mini",
}
DEFAULT_MODEL = "pro"


@lru_cache(maxsize=1)
def _client() -> openai.OpenAI:
    return openai.OpenAI()


@measure
def ask(prompt: str, model: str = DEFAULT_MODEL) -> LLMResponse:
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    response = _client().chat.completions.create(
        model=MODELS[model],
        messages=[{"role": "user", "content": prompt}],
    )
    return LLMResponse(
        text=response.choices[0].message.content,
        model=response.model,
        provider="openai",
        input_tokens=response.usage.prompt_tokens,
        output_tokens=response.usage.completion_tokens,
    )
