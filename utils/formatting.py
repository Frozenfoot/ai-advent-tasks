from models.response import LLMResponse


def format_stats(r: LLMResponse) -> str:
    elapsed = f"{r.elapsed:.2f}s" if r.elapsed is not None else "n/a"
    return f"\n[{r.model}] in: {r.input_tokens} / out: {r.output_tokens} tokens | {elapsed}"
