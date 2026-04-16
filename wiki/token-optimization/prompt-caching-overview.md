# Prompt Caching Overview

**Source:** ai-research/anthropic-prompt-caching.md, ai-research/openai-prompt-caching.md

Prompt caching is a provider-level optimization that allows LLMs to reuse previously processed prompt prefixes, dramatically reducing both latency and costs for API calls with repetitive content.

## Key Takeaways

- OpenAI and Anthropic both offer automatic prompt caching with no code changes required
- Cache hits can reduce costs by 50-90% depending on the provider
- Caching works by storing processed prompt prefixes and reusing them for subsequent identical prefixes
- Effective caching requires structuring prompts with static content first and variable content last
- Minimum token thresholds apply (typically 1024+ tokens) before caching activates
- Cache lifetime is typically 5-10 minutes, with extended options up to 24 hours available

## How It Works

1. **Request routing**: Requests are routed to servers that recently processed the same prompt prefix
2. **Cache lookup**: The system checks if the prompt prefix exists in cache
3. **Cache hit**: If found, the cached computation is reused, saving processing time and cost
4. **Cache miss**: If not found, the full prompt is processed and the prefix is cached for future requests

## Provider Comparison

| Feature | OpenAI | Anthropic (Claude) |
|---------|--------|-------------------|
| Activation | Automatic (≥1024 tokens) | Automatic or Explicit |
| Cost savings | 50% on cached tokens | 90% on cached reads |
| Cache write cost | None | 25% premium (5-min), 100% premium (1-hour) |
| Default TTL | 5-10 minutes | 5 minutes |
| Extended TTL | 24 hours (select models) | 1 hour |
| Max breakpoints | N/A | 4 explicit breakpoints |

## Best Practices

1. **Structure prompts correctly**: Place system instructions, tool definitions, and examples at the beginning
2. **Minimize prefix variation**: Keep the cacheable prefix identical across requests
3. **Use consistent tool definitions**: Changes to tools invalidate the cache
4. **Monitor cache performance**: Track `cached_tokens` (OpenAI) or `cache_read_input_tokens` (Anthropic)
5. **Consider extended TTL**: For infrequent but repeated queries, use 1-hour or 24-hour caching

## When to Use

- Multi-turn conversations with consistent system prompts
- RAG applications with large static context
- Agentic systems with multiple tool calls
- Batch processing with shared instructions
- Applications with long instruction sets or examples

## Related

[[token-optimization/llmlingua-prompt-compression|LLMLingua: Prompt Compression]]
[[token-optimization/best-practices-cost-savings|Best Practices for Token Cost Savings]]
[[llms/_index|Large Language Models]]
[[ai-agents/_index|AI Agents]]
[[ai-architecture/_index|AI Architecture]]
