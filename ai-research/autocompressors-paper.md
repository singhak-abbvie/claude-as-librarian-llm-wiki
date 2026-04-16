---
url: https://arxiv.org/abs/2305.14788
fetched: 2026-04-16
summary: AutoCompressors paper - adapting language models to compress contexts into compact summary vectors for extended context windows
---

# Adapting Language Models to Compress Contexts

**Authors:** Alexis Chevalier, Alexander Wettig, Anirudh Ajith, Danqi Chen

**Published:** arXiv:2305.14788 [cs.CL]

**Accepted at:** EMNLP 2023

## Abstract

Transformer-based language models (LMs) are powerful and widely-applicable tools, but their usefulness is constrained by:
- A finite context window
- The expensive computational cost of processing long text documents

## AutoCompressors Solution

The authors propose to adapt pre-trained LMs into **AutoCompressors**. These language models are capable of compressing long contexts into **compact summary vectors**, which are then accessible to the model as **soft prompts**.

## Key Concepts

### Summary Vectors

- Summary vectors are trained with an **unsupervised objective**
- Long documents are processed in segments
- Summary vectors from all previous segments are used in language modeling
- These vectors serve as a compressed representation of the context

### Training Approach

The authors fine-tune OPT and Llama-2 models on sequences of up to **30,720 tokens** and show that AutoCompressors can utilize long contexts to improve perplexity.

## Evaluation Results

### In-Context Learning

AutoCompressors are evaluated on in-context learning by compressing task demonstrations. Results show that summary vectors are **good substitutes for plain-text demonstrations**:
- Increase accuracy
- Reduce inference costs

### Pre-computed Summary Vectors

The benefits of pre-computing summary vectors for large corpora are explored through:
1. **Retrieval-augmented language modeling**
2. **Passage re-ranking tasks**

## Key Benefits

1. **Extended Context Window**: Simple and inexpensive solution to extend the context window of LMs
2. **Faster Inference**: Speeds up inference over long contexts
3. **Pre-computation**: Summary vectors can be pre-computed offline for large document collections
4. **Soft Prompts**: Compressed context is accessible as soft prompts, maintaining compatibility with the original model

## Technical Approach

### Segmented Processing

1. Documents are split into segments
2. Each segment is processed to produce summary vectors
3. Summary vectors are passed to subsequent segments as soft prompts
4. This creates a chain of compressed context representations

### Unsupervised Training

The model learns to compress context through standard language modeling objectives without explicit supervision about what information to retain.

## Applications

- **Document understanding**: Process long documents that exceed context limits
- **Retrieval-augmented generation**: Pre-compute summaries for document collections
- **Multi-document QA**: Compress multiple sources into summary vectors
- **Long conversations**: Maintain conversation history in compressed form

## Comparison with Prompt Compression

| Aspect | Prompt Compression (LLMLingua) | AutoCompressors |
|--------|-------------------------------|-----------------|
| Approach | Remove tokens | Compress to vectors |
| Output | Shorter text prompt | Soft prompt vectors |
| Interpretability | Human-readable (somewhat) | Not human-readable |
| Pre-computation | Limited | Strong support |
| Model modification | None (use as-is) | Fine-tuning required |

## Implications

AutoCompressors emerge as a complementary approach to prompt compression methods like LLMLingua. While prompt compression removes tokens to create shorter text prompts, AutoCompressors transform context into dense vector representations that can be reused across queries.

## Citation

```bibtex
@inproceedings{chevalier2023adapting,
    title={Adapting Language Models to Compress Contexts},
    author={Alexis Chevalier and Alexander Wettig and Anirudh Ajith and Danqi Chen},
    booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
    year={2023}
}
```
