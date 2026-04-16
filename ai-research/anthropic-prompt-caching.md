---
url: https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching
fetched: 2026-04-16
summary: Anthropic's comprehensive documentation on prompt caching for Claude API, including automatic and explicit caching strategies
---

# Anthropic Prompt Caching Documentation

Prompt caching optimizes your API usage by allowing resuming from specific prefixes in your prompts. This significantly reduces processing time and costs for repetitive tasks or prompts with consistent elements.

This feature is eligible for Zero Data Retention (ZDR). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

## Two Ways to Enable Prompt Caching

1. **Automatic caching**: Add a single `cache_control` field at the top level of your request. The system automatically applies the cache breakpoint to the last cacheable block and moves it forward as conversations grow. Best for multi-turn conversations.

2. **Explicit cache breakpoints**: Place `cache_control` directly on individual content blocks for fine-grained control over exactly what gets cached.

## How Prompt Caching Works

When you send a request with prompt caching enabled:

1. The system checks if a prompt prefix, up to a specified cache breakpoint, is already cached from a recent query
2. If found, it uses the cached version, reducing processing time and costs
3. Otherwise, it processes the full prompt and caches the prefix once the response begins

This is especially useful for:
- Prompts with many examples
- Large amounts of context or background information
- Repetitive tasks with consistent instructions
- Long multi-turn conversations

### Cache Lifetime

By default, the cache has a **5-minute lifetime**. The cache is refreshed for no additional cost each time the cached content is used.

Anthropic also offers a **1-hour cache duration** at additional cost.

## Pricing

Prompt caching introduces a new pricing structure:

### Pricing Multipliers

- 5-minute cache write tokens: **1.25x** base input tokens price
- 1-hour cache write tokens: **2x** base input tokens price  
- Cache read tokens: **0.1x** base input tokens price (90% savings!)

### Example Pricing (Claude Sonnet 4.5)

| Category | Price per MTok |
|----------|---------------|
| Base input | $3 |
| 5-min cache write | $3.75 |
| 1-hour cache write | $6 |
| Cache read | $0.30 |
| Output | $15 |

## Cache Limitations

The minimum cacheable prompt length varies by model:
- Claude Opus 4.6/4.5: 4096 tokens
- Claude Sonnet 4.6: 2048 tokens
- Claude Sonnet 4.5/4.1/4: 1024 tokens
- Claude Haiku 4.5: 4096 tokens
- Claude Haiku 3.5/3: 2048 tokens

Shorter prompts cannot be cached, even if marked with `cache_control`.

## Automatic Caching

The simplest way to enable prompt caching. Add a single `cache_control` field at the top level of your request body:

```json
{
  "model": "claude-opus-4-6",
  "max_tokens": 1024,
  "cache_control": {"type": "ephemeral"},
  "system": "You are a helpful assistant.",
  "messages": [...]
}
```

### How Automatic Caching Works in Multi-turn Conversations

| Request | Content | Cache Behavior |
|---------|---------|----------------|
| Request 1 | System + User(1) + Asst(1) + User(2) | Everything written to cache |
| Request 2 | +Asst(2) + User(3) | Previous content read from cache; new content written |
| Request 3 | +Asst(3) + User(4) | Previous content read from cache; new content written |

The cache breakpoint automatically moves to the last cacheable block in each request.

## Explicit Cache Breakpoints

For more control over caching, place `cache_control` directly on individual content blocks.

### Structuring Your Prompt

Place static content (tool definitions, system instructions, context, examples) at the beginning of your prompt. Mark the end of the reusable content for caching using the `cache_control` parameter.

Cache prefixes are created in this order: `tools`, `system`, then `messages`.

### Key Takeaway

Place `cache_control` on the last block whose prefix is identical across the requests you want to share a cache. In a growing conversation, the final block works as long as each turn adds fewer than 20 blocks.

For a prompt with a varying suffix (timestamps, per-request context), place the breakpoint at the end of the static prefix, not on the varying block.

### When to Use Multiple Breakpoints

You can define up to 4 cache breakpoints to:
- Cache different sections that change at different frequencies
- Have more control over exactly what gets cached
- Ensure a cache hit when a growing conversation pushes your breakpoint 20+ blocks past the last cache write

## What Can Be Cached

- **Tools**: Tool definitions in the `tools` array
- **System messages**: Content blocks in the `system` array
- **Text messages**: Content blocks in the `messages.content` array
- **Images & Documents**: Content blocks in user turns
- **Tool use and tool results**: Content blocks in both user and assistant turns

## What Cannot Be Cached

- Thinking blocks (directly with `cache_control`)
- Sub-content blocks like citations
- Empty text blocks

## What Invalidates the Cache

| Change Type | Tools Cache | System Cache | Messages Cache |
|-------------|-------------|--------------|----------------|
| Tool definitions | ✘ | ✘ | ✘ |
| Web search toggle | ✓ | ✘ | ✘ |
| Citations toggle | ✓ | ✘ | ✘ |
| Tool choice | ✓ | ✓ | ✘ |
| Images | ✓ | ✓ | ✘ |
| Thinking parameters | ✓ | ✓ | ✘ |

## Tracking Cache Performance

Monitor cache performance using these API response fields in `usage`:

- `cache_creation_input_tokens`: Tokens written to the cache
- `cache_read_input_tokens`: Tokens retrieved from cache
- `input_tokens`: Tokens after the last cache breakpoint (uncached)

**Total input tokens** = cache_read + cache_creation + input_tokens

## Best Practices for Effective Caching

1. Start with automatic caching for multi-turn conversations
2. Use explicit block-level breakpoints when caching sections with different change frequencies
3. Cache stable, reusable content at the prompt's beginning
4. Place the breakpoint on the last block that stays identical across requests
5. Regularly analyze cache hit rates and adjust strategy

## Optimizing for Different Use Cases

- **Conversational agents**: Reduce cost/latency for extended conversations with long instructions or uploaded documents
- **Coding assistants**: Keep relevant codebase sections in the prompt
- **Large document processing**: Include complete long-form material without increasing latency
- **Detailed instruction sets**: Include 20+ diverse examples for better performance
- **Agentic tool use**: Enhance performance for scenarios with multiple tool calls
- **Talk to documents/podcasts**: Embed entire documents and let users query them

## 1-Hour Cache Duration

For prompts used less frequently than every 5 minutes but more than every hour:

```json
"cache_control": {
  "type": "ephemeral",
  "ttl": "1h"
}
```

Best for:
- Agentic side-agents taking longer than 5 minutes
- Long chat conversations where users may not respond within 5 minutes
- Latency-critical applications
- Improving rate limit utilization (cache hits don't count against rate limits)

## Cache Storage and Sharing

- **Organization Isolation**: Caches are isolated between organizations
- **Exact Matching**: Cache hits require 100% identical prompt segments
- **Output Token Generation**: Caching has no effect on output generation - responses are identical
