# LLMLingua: Prompt Compression Framework

**Source:** ai-research/llmlingua-microsoft-research.md, ai-research/llmlingua-github-repo.md

LLMLingua is Microsoft Research's groundbreaking prompt compression framework that uses small language models to identify and remove non-essential tokens from prompts, achieving up to 20x compression while maintaining LLM performance.

## Key Takeaways

- Achieves up to **20x prompt compression** with minimal performance loss
- Uses small models (GPT2-small, LLaMA-7B) to identify unimportant tokens
- Compressed prompts remain effective for LLMs even when less readable to humans
- GPT-4 can fully recover the original meaning from compressed prompts
- Reduces API costs proportionally to compression ratio
- Integrated into popular RAG frameworks: LangChain and LlamaIndex

## How It Works

LLMLingua employs a three-stage approach:

### 1. Budget Controller
Balances sensitivities of different modules in the prompt, preserving language integrity while allocating compression budgets.

### 2. Coarse-grained Compression
First pass eliminates entire sentences based on their importance to the overall meaning.

### 3. Token-level Compression
Iterative refinement that compresses individual tokens while maintaining relationships between remaining tokens.

## Performance Results

| Metric | Result |
|--------|--------|
| Maximum compression | 20x |
| End-to-end acceleration | 1.7-5.7x |
| Response length reduction | 20-30% |
| Latency with 10x compression | 5.7x faster |

### Benchmark Performance

Tested on GSM8K, BBH, ShareGPT, and Arxiv-March23 datasets:
- Maintains original reasoning capabilities at 20x compression
- Preserves ICL (in-context learning) performance
- Outperforms other compression methods in retaining semantic information

## Quick Start

```python
from llmlingua import PromptCompressor

llm_lingua = PromptCompressor()
result = llm_lingua.compress_prompt(
    prompt, 
    instruction="", 
    question="", 
    target_token=200
)

# Output includes:
# - compressed_prompt: The compressed text
# - origin_tokens: Original token count
# - compressed_tokens: Compressed token count
# - ratio: Compression ratio (e.g., "11.2x")
# - saving: Estimated cost savings
```

## Model Options

| Model | GPU Memory | Speed | Quality |
|-------|------------|-------|---------|
| GPT2-small | Minimal | Fast | Good |
| LLaMA-7B | ~14GB | Moderate | Best |
| Quantized (GPTQ) | <8GB | Fast | Good |
| phi-2 | ~5GB | Fast | Good |

## Use Cases

- **Chain-of-Thought prompts**: Compress multi-step reasoning examples
- **RAG applications**: Reduce retrieved context size
- **API cost optimization**: Direct cost savings from fewer tokens
- **Context window extension**: Fit more information in limited windows
- **Meeting transcription**: Compress long transcripts while retaining key information

## Robustness

LLMLingua demonstrates cross-model compatibility:
- Works with GPT-3.5-Turbo, GPT-4, Claude
- No additional training needed for target LLMs
- Performance maintains across different small model choices

## Related

[[token-optimization/longllmlingua-long-context|LongLLMLingua: Long Context Compression]]
[[token-optimization/llmlingua2-task-agnostic|LLMLingua-2: Task-Agnostic Compression]]
[[token-optimization/prompt-caching-overview|Prompt Caching Overview]]
[[llms/_index|Large Language Models]]
[[ai-architecture/_index|AI Architecture]]
