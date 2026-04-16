# AutoCompressors: Context to Vectors

**Source:** ai-research/autocompressors-paper.md

AutoCompressors represent a different approach to context compression: instead of removing tokens from text, they transform long contexts into compact dense vector representations (soft prompts) that can be reused across queries.

## Key Takeaways

- Compresses context into **summary vectors** rather than shortened text
- Summary vectors serve as **soft prompts** accessible to the model
- Enables processing sequences up to **30,720 tokens** with fine-tuned OPT and Llama-2
- Particularly effective for **pre-computing** summaries of large document collections
- Good for retrieval-augmented language modeling and passage re-ranking
- Requires fine-tuning the base model (unlike LLMLingua approaches)

## How It Works

### Segmented Processing

1. Long documents are split into manageable segments
2. Each segment is processed to produce summary vectors
3. Summary vectors from previous segments are passed as soft prompts to subsequent segments
4. This creates a chain of compressed context representations

### Unsupervised Training

The model learns compression through standard language modeling:
- No explicit labels about what to compress
- The model learns to retain information needed for next-token prediction
- Results in summary vectors that capture essential context

## Comparison with Text Compression

| Aspect | Text Compression (LLMLingua) | Vector Compression (AutoCompressors) |
|--------|------------------------------|--------------------------------------|
| Output | Shorter text | Dense vectors |
| Human readable | Somewhat | No |
| Pre-computation | Limited | Excellent |
| Model changes | None required | Fine-tuning required |
| Inference speed | Proportional to compression | Very fast (vectors pre-computed) |
| Flexibility | Per-query | Pre-computed, reusable |

## Key Benefits

### 1. Extended Context Window
Models can effectively handle much longer contexts than their native window allows by compressing earlier context into summary vectors.

### 2. Pre-computation
Summary vectors can be computed offline for large document collections:
- Compute once, use many times
- Ideal for static knowledge bases
- Reduces inference-time computation

### 3. Fast Inference
Once summary vectors are computed:
- No real-time compression needed
- Just retrieve and concatenate vectors
- Significantly faster than processing full text

## Use Cases

- **Document Collections**: Pre-compute summaries for knowledge bases
- **Retrieval-Augmented Generation**: Compress retrieved passages
- **Multi-Document QA**: Combine summaries from multiple sources
- **Long Conversations**: Compress conversation history into vectors
- **Passage Re-ranking**: Efficient comparison of many documents

## Technical Details

### Summary Vector Properties

- Serve as soft prompts to the model
- Capture semantic content of compressed text
- Can be concatenated with new prompts
- Learned through unsupervised training

### Training Configuration

Fine-tuned models tested on:
- OPT (various sizes)
- Llama-2 (various sizes)
- Sequences up to 30,720 tokens

## Limitations

1. **Requires fine-tuning**: Cannot use off-the-shelf models
2. **Not human interpretable**: Summary vectors are opaque
3. **Less flexible**: Pre-computed summaries may not capture query-specific relevance
4. **Model-specific**: Vectors are tied to the fine-tuned model

## When to Use

**AutoCompressors excel when:**
- You have large static document collections
- The same documents are queried repeatedly
- Pre-computation time is available
- Maximum inference speed is required

**Text compression (LLMLingua) may be better when:**
- Content changes frequently
- You need interpretable compression
- You want to use any LLM without fine-tuning
- Query-specific compression is important

## Combining Approaches

AutoCompressors and LLMLingua are complementary:

1. **Pre-compute** summary vectors for static knowledge bases
2. **Use LLMLingua** for dynamic, query-specific content
3. **Cache** frequently used compressed prompts at the provider level

## Related

[[token-optimization/llmlingua-prompt-compression|LLMLingua: Prompt Compression Framework]]
[[token-optimization/prompt-caching-overview|Prompt Caching Overview]]
[[token-optimization/best-practices-cost-savings|Best Practices for Token Cost Savings]]
[[llms/_index|Large Language Models]]
[[ai-architecture/_index|AI Architecture]]
