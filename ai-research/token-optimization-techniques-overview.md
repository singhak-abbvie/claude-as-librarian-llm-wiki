---
url: synthesized from multiple sources
fetched: 2026-04-16
summary: Comprehensive overview of all token cost saving and memory compression techniques for LLMs
---

# Token Cost Saving and Memory Compression Techniques: A Comprehensive Guide

This document synthesizes research and documentation from multiple sources to provide a comprehensive overview of effective techniques for reducing token costs and compressing context memory in LLM applications.

## Categories of Techniques

Token cost and memory optimization techniques fall into three main categories:

### 1. Provider-Level Caching (Automatic)
Built-in caching offered by LLM providers that requires minimal code changes.

### 2. Prompt Compression
Algorithmic approaches to reduce prompt length while preserving information.

### 3. Context Vectorization
Converting text context into dense vector representations.

---

## 1. Provider-Level Prompt Caching

### OpenAI Prompt Caching

**How it works:**
- Automatic for prompts ≥1024 tokens
- Routes requests to servers with cached prompts
- No code changes required

**Benefits:**
- Up to 80% latency reduction
- Up to 90% cost reduction (50% discount on cached tokens)
- Cache lasts 5-10 minutes (up to 1 hour off-peak)
- Extended caching available for 24 hours

**Best practices:**
- Place static content at prompt beginning
- Put variable content at the end
- Use `prompt_cache_key` for consistent routing

### Anthropic (Claude) Prompt Caching

**How it works:**
- Two modes: Automatic and Explicit
- Caches prompt prefixes
- 5-minute default TTL (1-hour option available)

**Benefits:**
- Cache reads cost 10% of base input price (90% savings!)
- 1.25x cost for cache writes (5-min TTL)
- Up to 4 cache breakpoints for fine-grained control

**Best practices:**
- Use automatic caching for multi-turn conversations
- Use explicit breakpoints for different change frequencies
- Place cache breakpoint on last stable block
- Minimum: 1024-4096 tokens depending on model

---

## 2. Prompt Compression Techniques

### LLMLingua (Microsoft Research)

**Approach:** Token-level removal using small language models

**Key features:**
- Uses GPT2-small or LLaMA-7B to identify unimportant tokens
- Achieves up to 20x compression
- Maintains reasoning and ICL capabilities
- GPT-4 can recover compressed prompts

**Performance:**
- 1.7-5.7x end-to-end acceleration
- 20-30% response length reduction
- Works across different LLMs (GPT-3.5, GPT-4, Claude)

### LongLLMLingua

**Focus:** Long context scenarios (RAG, meetings)

**Key innovation:** Addresses "lost in the middle" problem

**Results:**
- 21.4% performance boost with 4x fewer tokens
- 94% cost reduction on LooGLE benchmark
- 1.4-2.6x latency acceleration at 2-6x compression

### LLMLingua-2

**Approach:** Token classification with data distillation from GPT-4

**Key improvements over LLMLingua:**
- 3-6x faster
- Bidirectional context (vs unidirectional)
- BERT-level models (smaller than LLaMA-7B)
- Better out-of-domain generalization

**Results:**
- 1.6-2.9x latency acceleration
- 2-5x compression ratios
- Task-agnostic compression

---

## 3. Context Vectorization

### AutoCompressors

**Approach:** Compress context into soft prompt vectors

**How it works:**
1. Split documents into segments
2. Process each segment to produce summary vectors
3. Pass vectors to subsequent segments as soft prompts

**Benefits:**
- Extends effective context window (tested up to 30,720 tokens)
- Pre-compute vectors offline for document collections
- Vectors are reusable across queries

**Trade-offs:**
- Requires fine-tuning the base model
- Compressed representation is not human-readable
- Good for retrieval-augmented scenarios

---

## Comparison Matrix

| Technique | Compression | Latency | Cost Savings | Setup Effort | Best For |
|-----------|-------------|---------|--------------|--------------|----------|
| OpenAI Caching | N/A | Up to 80% | Up to 50% | None | All use cases |
| Anthropic Caching | N/A | Significant | Up to 90% | Minimal | Multi-turn, RAG |
| LLMLingua | Up to 20x | 1.7-5.7x | Proportional | pip install | Reasoning, ICL |
| LongLLMLingua | 4x+ | 1.4-2.6x | Up to 94% | pip install | Long context, RAG |
| LLMLingua-2 | 2-5x | 1.6-2.9x | Proportional | pip install | Task-agnostic |
| AutoCompressors | Variable | Faster inference | High pre-compute | Fine-tuning | Document collections |

---

## Best Practices Summary

### For API Users

1. **Enable caching first** - Free/low-cost with immediate benefits
2. **Structure prompts correctly** - Static content first, variable last
3. **Use consistent prefixes** - Maximize cache hits
4. **Monitor cache performance** - Track `cached_tokens` in responses

### For High-Volume Applications

1. **Combine techniques** - Use caching + compression together
2. **Consider LLMLingua-2** for general-purpose compression
3. **Use LongLLMLingua** for RAG and long documents
4. **Pre-compute summaries** for static document collections

### For RAG Systems

1. **Compress retrieved chunks** before sending to LLM
2. **Use LongLLMLingua's reordering** to address position bias
3. **Cache system prompts and tool definitions**
4. **Pre-compute document vectors** with AutoCompressors

### For Multi-Turn Conversations

1. **Use automatic prompt caching** (Anthropic/OpenAI)
2. **Summarize older turns** to reduce context growth
3. **Set appropriate cache TTLs** (1-hour for infrequent users)

---

## Implementation Recommendations

### Quick Wins (< 1 hour setup)
1. Enable OpenAI/Anthropic prompt caching
2. Restructure prompts (static first)
3. Add cache breakpoints for system prompts

### Medium Effort (1 day setup)
1. Integrate LLMLingua-2 for prompt compression
2. Compress RAG context before LLM calls
3. Monitor and optimize cache hit rates

### High Effort (1 week+ setup)
1. Fine-tune AutoCompressors for your domain
2. Build pre-computed summary vector indices
3. Implement hybrid caching + compression pipeline

---

## Cost Calculation Examples

### Example 1: Simple Chat Application
- 2000 token system prompt, 500 token conversation
- Without caching: 2500 tokens × $3/MTok = $0.0075
- With 90% cache read: 2000×$0.30 + 500×$3 = $0.0021 (72% savings)

### Example 2: RAG Application
- 8000 token context, compressed to 2000 with LLMLingua
- Original: 8000 × $3/MTok = $0.024
- Compressed: 2000 × $3/MTok = $0.006 (75% savings)
- Plus faster response time

### Example 3: Combined Approach
- 10000 token prompt → 3000 with LLMLingua → cached
- Original: 10000 × $3/MTok = $0.03
- Optimized: 3000 × $0.30/MTok = $0.0009 (97% savings!)
