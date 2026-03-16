from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LLMResponse:
    text: str
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    elapsed: Optional[float] = field(default=None)
