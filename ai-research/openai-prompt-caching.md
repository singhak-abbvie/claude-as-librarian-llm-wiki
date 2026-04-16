---
url: https://developers.openai.com/api/docs/guides/prompt-caching
fetched: 2026-04-16
summary: OpenAI's documentation on automatic prompt caching, reducing latency by up to 80% and costs by up to 90% for API requests
---

# OpenAI Prompt Caching Documentation

Model prompts often contain repetitive content, like system prompts and common instructions. OpenAI routes API requests to servers that recently processed the same prompt, making it cheaper and faster than processing a prompt from scratch.

## Key Benefits

- Reduce latency by up to **80%**
- Reduce input token costs by up to **90%**
- Works automatically on all API requests (no code changes required)
- No additional fees associated with it
- Available for all recent models (gpt-4o and newer)

## How It Works

Caching is enabled automatically for prompts containing **1024 tokens or more**. When you make an API request:

### 1. Cache Routing
- Requests are routed to a machine based on a hash of the initial prefix of the prompt (typically first 256 tokens)
- If you provide the `prompt_cache_key` parameter, it is combined with the prefix hash, allowing you to influence routing and improve cache hit rates
- If requests for the same prefix and `prompt_cache_key` combination exceed ~15 requests per minute, some may overflow to additional machines, reducing cache effectiveness

### 2. Cache Lookup
The system checks if the initial portion (prefix) of your prompt exists in the cache on the selected machine.

### 3. Cache Hit
If a matching prefix is found, the system uses the cached result. This significantly decreases latency and reduces costs.

### 4. Cache Miss
If no matching prefix is found, the system processes your full prompt, caching the prefix afterward on that machine for future requests.

## Prompt Cache Retention

### In-memory Prompt Cache Retention

Available for all models that support Prompt Caching:
- Cached prefixes generally remain active for **5 to 10 minutes** of inactivity
- Maximum retention: **one hour**
- Only held within volatile GPU memory

### Extended Prompt Cache Retention

Available for select models (gpt-5.4, gpt-5.2, gpt-5.1, gpt-5, gpt-4.1):
- Keeps cached prefixes active for up to **24 hours**
- Works by offloading key/value tensors to GPU-local storage when memory is full
- Key/value tensors are the intermediate representation from the model's attention layers produced during prefill

### Configure Per Request

```json
{
  "model": "gpt-5.1",
  "input": "Your prompt goes here...",
  "prompt_cache_retention": "24h"
}
```

Default is `in_memory`. Allowed values: `in_memory` and `24h`.

## Structuring Prompts for Optimal Caching

Cache hits are only possible for **exact prefix matches** within a prompt.

### Best Structure

1. Place **static content** (instructions, examples) at the **beginning** of your prompt
2. Put **variable content** (user-specific information) at the **end**
3. This also applies to images and tools, which must be identical between requests

## Requirements

### Minimum Token Requirement
Caching is available for prompts containing **1024 tokens or more**.

### Checking Cache Usage
All requests will display a `cached_tokens` field in `usage.prompt_tokens_details`:

```json
"usage": {
  "prompt_tokens": 2006,
  "completion_tokens": 300,
  "total_tokens": 2306,
  "prompt_tokens_details": {
    "cached_tokens": 1920
  },
  "completion_tokens_details": {
    "reasoning_tokens": 0,
    "accepted_prediction_tokens": 0,
    "rejected_prediction_tokens": 0
  }
}
```

## What Can Be Cached

- **Messages**: The complete messages array (system, user, and assistant interactions)
- **Images**: Images in user messages (as links or base64-encoded data) - ensure the `detail` parameter is set identically
- **Tool use**: Both the messages array and the list of available `tools`
- **Structured outputs**: The structured output schema serves as a prefix to the system message

## Best Practices

1. **Structure prompts** with static or repeated content at the beginning, dynamic content at the end
2. **Use `prompt_cache_key`** consistently across requests that share common prefixes - keep each unique combination below 15 requests per minute
3. **Monitor cache performance** metrics including cache hit rates, latency, and proportion of tokens cached
4. **Maintain a steady stream** of requests with identical prompt prefixes to minimize cache evictions

## Pricing (October 2024)

| Model | Uncached Input | Cached Input | Output |
|-------|---------------|--------------|--------|
| GPT-4o | $2.50/MTok | $1.25/MTok | $10.00/MTok |
| GPT-4o fine-tuning | $3.75/MTok | $1.875/MTok | $15.00/MTok |
| GPT-4o mini | $0.15/MTok | $0.075/MTok | $0.60/MTok |
| GPT-4o mini fine-tuning | $0.30/MTok | $0.15/MTok | $1.20/MTok |
| o1-preview | $15.00/MTok | $7.50/MTok | $60.00/MTok |
| o1 mini | $3.00/MTok | $1.50/MTok | $12.00/MTok |

**Cached input tokens are 50% cheaper than uncached.**

## Frequently Asked Questions

### How is data privacy maintained?
Prompt caches are not shared between organizations. Only members of the same organization can access caches of identical prompts.

### Does caching affect output generation?
No. Prompt Caching does not influence the generation of output tokens or the final response. Output will be identical whether caching is used or not.

### Can I manually clear the cache?
Manual cache clearing is not currently available. Prompts are automatically cleared after 5-10 minutes of inactivity, up to one hour during off-peak periods.

### Do cached prompts contribute to TPM rate limits?
Yes, caching does not affect rate limits.

### Does Prompt Caching work with Zero Data Retention?
In-memory cache retention does not save any data to disk. Extended caching may store key/value tensors in GPU-local storage but these are not retained beyond cache expiration.
