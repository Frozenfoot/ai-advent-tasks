from dataclasses import dataclass, field


@dataclass
class LLMResponse:
    text: str
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    elapsed: float = field(default=0.0)
