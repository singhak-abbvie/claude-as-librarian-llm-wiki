# LongLLMLingua: Long Context Compression

**Source:** ai-research/longllmlingua-paper.md, ai-research/llmlingua-github-repo.md

LongLLMLingua extends the LLMLingua framework specifically for long-context scenarios, addressing the "lost in the middle" problem while achieving significant cost reductions in RAG and document processing applications.

## Key Takeaways

- Addresses three main LLM challenges in long contexts: computational cost, performance reduction, and position bias
- Achieves up to **21.4% performance improvement** with **4x fewer tokens** on NaturalQuestions benchmark
- **94% cost reduction** demonstrated on LooGLE benchmark
- Accelerates end-to-end latency by **1.4x-2.6x** for prompts around 10k tokens
- Mitigates the "lost in the middle" problem where LLMs miss relevant information in mid-context

## The "Lost in the Middle" Problem

Research shows that LLM performance depends on:
- **Density** of key information in the input prompt
- **Position** of relevant information (beginning and end are favored)

Information appearing in the middle of long contexts is often overlooked or forgotten by LLMs. LongLLMLingua addresses this by:
1. Identifying key information regardless of position
2. Reorganizing and compressing context to improve information density
3. Placing critical information in optimal positions

## How It Works

LongLLMLingua enhances standard LLMLingua with:

### Question-Conditioned Compression
Compression is guided by the specific question or query, ensuring relevant information is preserved.

### Context Reordering
The `reorder_context="sort"` parameter reorganizes context based on relevance, addressing position bias.

### Dynamic Compression Ratios
`dynamic_context_compression_ratio` allows varying compression based on content importance.

## Usage

```python
from llmlingua import PromptCompressor

llm_lingua = PromptCompressor()
compressed_prompt = llm_lingua.compress_prompt(
    prompt_list,
    question=question,
    rate=0.55,
    # LongLLMLingua-specific parameters
    condition_in_question="after_condition",
    reorder_context="sort",
    dynamic_context_compression_ratio=0.3,
    condition_compare=True,
    context_budget="+100",
    rank_method="longllmlingua",
)
```

## Performance Results

| Benchmark | Improvement | Token Reduction |
|-----------|-------------|-----------------|
| NaturalQuestions | +21.4% | 4x fewer |
| LooGLE | N/A | 94% cost reduction |

### Latency Acceleration

| Compression Ratio | Latency Improvement |
|-------------------|---------------------|
| 2x | 1.4x faster |
| 6x | 2.6x faster |

## Ideal Use Cases

- **RAG Systems**: Compress retrieved documents before LLM processing
- **Meeting Transcription**: Summarize long meetings while preserving key points
- **Document Q&A**: Answer questions over lengthy documents
- **Chatbots with Context**: Maintain conversation history efficiently
- **Multi-document Analysis**: Process multiple sources simultaneously

## Key Parameters

| Parameter | Purpose |
|-----------|---------|
| `rate` | Overall compression target (e.g., 0.55 = 55% of original) |
| `condition_in_question` | How to use the question for conditioning |
| `reorder_context` | Whether to reorganize context ("sort" or None) |
| `dynamic_context_compression_ratio` | Varying compression for different chunks |
| `context_budget` | Additional token budget for important context |
| `rank_method` | Method for ranking context importance |

## Comparison with Standard LLMLingua

| Aspect | LLMLingua | LongLLMLingua |
|--------|-----------|---------------|
| Target | General prompts | Long contexts (10k+ tokens) |
| Focus | Token removal | Position bias mitigation |
| Context handling | Sequential | Question-conditioned |
| Best for | ICL, CoT | RAG, documents |

## Related

[[token-optimization/llmlingua-prompt-compression|LLMLingua: Prompt Compression Framework]]
[[token-optimization/llmlingua2-task-agnostic|LLMLingua-2: Task-Agnostic Compression]]
[[token-optimization/best-practices-cost-savings|Best Practices for Token Cost Savings]]
[[ai-agents/_index|AI Agents]]
[[ai-architecture/_index|AI Architecture]]
