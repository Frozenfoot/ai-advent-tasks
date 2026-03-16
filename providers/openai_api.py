"""
Обёртка над OpenAI API.
Клиент берёт ключ из переменной окружения OPENAI_API_KEY (загружается из .env).
"""
import openai
from dotenv import load_dotenv
from providers.response import LLMResponse
from utils.timing import measure

load_dotenv()

MODELS = {
    "pro":  "gpt-5.4",
    "lite": "gpt-5-mini",
}
DEFAULT_MODEL = "pro"


@measure
def ask(prompt: str, model: str = DEFAULT_MODEL) -> LLMResponse:
    client = openai.OpenAI()
    response = client.chat.completions.create(
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
