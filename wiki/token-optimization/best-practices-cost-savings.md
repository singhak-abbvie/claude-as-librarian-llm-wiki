# Best Practices for Token Cost Savings

**Source:** ai-research/token-optimization-techniques-overview.md, ai-research/anthropic-prompt-caching.md, ai-research/openai-prompt-caching.md, ai-research/llmlingua-github-repo.md

A comprehensive guide to implementing token optimization strategies, combining provider caching, prompt compression, and context vectorization for maximum cost savings and performance improvements.

## Key Takeaways

- Combining techniques can achieve **97%+ cost savings** in optimal scenarios
- Provider caching offers immediate benefits with no code changes
- Prompt compression works independently of provider caching for multiplicative savings
- Structure prompts with static content first for maximum cache hits
- Match the optimization technique to your specific use case
- Monitor and iterate on your optimization strategy

## Implementation Tiers

### Tier 1: Quick Wins (< 1 hour setup)

1. **Enable provider prompt caching**
   - OpenAI: Automatic for prompts ≥1024 tokens
   - Anthropic: Add `cache_control` to request

2. **Restructure prompts**
   ```
   [Static: System instructions, tools, examples]
   [Semi-static: Context, documents]
   [Dynamic: User input, query]
   ```

3. **Add cache breakpoints** (Anthropic)
   - Mark end of system prompts
   - Mark end of tool definitions

### Tier 2: Medium Effort (1 day setup)

1. **Integrate LLMLingua-2**
   ```python
   from llmlingua import PromptCompressor
   
   compressor = PromptCompressor(
       model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",
       use_llmlingua2=True
   )
   ```

2. **Compress RAG context**
   - Apply compression to retrieved documents before LLM call
   - Target 30-50% compression for quality/cost balance

3. **Monitor cache performance**
   - Track `cached_tokens` in responses
   - Optimize prefix consistency

### Tier 3: High Effort (1 week+ setup)

1. **Fine-tune AutoCompressors** for your domain
2. **Build pre-computed summary vector indices**
3. **Implement hybrid pipeline**

## Technique Selection Guide

| Scenario | Recommended Approach |
|----------|---------------------|
| Multi-turn chat | Provider caching (automatic) |
| RAG with long documents | LongLLMLingua + caching |
| Static knowledge base | AutoCompressors + caching |
| Variable prompts | LLMLingua-2 + caching |
| Cost-critical applications | All techniques combined |
| Latency-critical applications | Provider caching + pre-compression |

## Cost Calculation Examples

### Example 1: Simple Chat (Anthropic)
```
System prompt: 2000 tokens
Conversation: 500 tokens

Without optimization:
  2500 × $3/MTok = $0.0075

With 90% cache read on system:
  2000 × $0.30/MTok + 500 × $3/MTok = $0.0021
  
Savings: 72%
```

### Example 2: RAG Application
```
Retrieved context: 8000 tokens
Query: 100 tokens

Without optimization:
  8100 × $3/MTok = $0.0243

With LLMLingua (4x compression) + caching:
  2000 × $0.30/MTok = $0.0006
  
Savings: 97.5%
```

### Example 3: Combined Approach
```
System: 5000 tokens (cached)
Context: 10000 tokens → 2500 with LLMLingua
Query: 200 tokens

Original: 15200 × $3/MTok = $0.0456

Optimized:
  5000 × $0.30 (cache read) = $0.0015
  2500 × $3.75 (cache write) = $0.009375
  200 × $3 (uncached) = $0.0006
  Total: $0.011475
  
Savings: 75%
```

## Architecture Patterns

### Pattern 1: RAG with Compression
```
Query → Retrieve Documents → Compress with LongLLMLingua → 
LLM (with cached system prompt) → Response
```

### Pattern 2: Multi-turn with Growing Context
```
System prompt (cached) + 
Compressed history (LLMLingua) + 
Recent turns (full text) → 
LLM → Response
```

### Pattern 3: Document Q&A
```
Pre-compute AutoCompressor vectors →
Query → Retrieve vectors → 
Combine with cached instructions → 
LLM → Response
```

## Monitoring Metrics

Track these metrics to optimize your strategy:

| Metric | Target | Action if Below |
|--------|--------|-----------------|
| Cache hit rate | >80% | Improve prefix consistency |
| Compression ratio | 2-5x | Adjust rate parameter |
| Quality degradation | <5% | Lower compression ratio |
| P95 latency | Baseline -50% | Add more caching |

## Common Pitfalls

### 1. Varying Prefixes
**Problem**: Cache misses due to timestamps or dynamic content in prefix
**Solution**: Move all dynamic content to end of prompt

### 2. Over-compression
**Problem**: Quality degradation at high compression ratios
**Solution**: Start conservative (50%), increase gradually

### 3. Ignoring Minimum Thresholds
**Problem**: Prompts below 1024 tokens don't cache
**Solution**: Pad prompts or combine requests

### 4. Inconsistent Tool Definitions
**Problem**: Cache invalidation on every request
**Solution**: Standardize tool schemas, use explicit breakpoints

## Provider-Specific Tips

### OpenAI
- Use `prompt_cache_key` for consistent routing
- Keep combinations below 15 req/min per prefix
- Consider 24-hour extended caching for stable prefixes

### Anthropic
- Use automatic caching for conversations
- Place explicit breakpoints on tool definitions
- Consider 1-hour TTL for infrequent but repeated queries
- Max 4 breakpoints per request

## Integration Code Example

```python
from llmlingua import PromptCompressor
import anthropic

# Initialize compressor
compressor = PromptCompressor(
    model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",
    use_llmlingua2=True
)

# Compress context (for RAG)
def compress_context(documents, rate=0.3):
    combined = "\n\n".join(documents)
    result = compressor.compress_prompt(combined, rate=rate)
    return result['compressed_prompt']

# Make API call with caching
client = anthropic.Client()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},  # Automatic caching
    system=[{
        "type": "text",
        "text": SYSTEM_PROMPT,
        "cache_control": {"type": "ephemeral"}  # Explicit breakpoint
    }],
    messages=[
        {"role": "user", "content": compress_context(retrieved_docs) + "\n\n" + query}
    ]
)
```

## Related

[[token-optimization/prompt-caching-overview|Prompt Caching Overview]]
[[token-optimization/llmlingua-prompt-compression|LLMLingua: Prompt Compression Framework]]
[[token-optimization/longllmlingua-long-context|LongLLMLingua: Long Context Compression]]
[[token-optimization/llmlingua2-task-agnostic|LLMLingua-2: Task-Agnostic Compression]]
[[token-optimization/autocompressors-summary-vectors|AutoCompressors: Context to Vectors]]
[[ai-business/_index|AI Business & Cost Optimization]]
