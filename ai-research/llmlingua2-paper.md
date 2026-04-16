---
url: https://arxiv.org/abs/2403.12968
fetched: 2026-04-16
summary: LLMLingua-2 paper - task-agnostic prompt compression using data distillation from GPT-4, 3x-6x faster than LLMLingua
---

# LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression

**Authors:** Zhuoshi Pan, Qianhui Wu, Huiqiang Jiang, Menglin Xia, Xufang Luo, Jue Zhang, Qingwei Lin, Victor Rühle, Yuqing Yang, Chin-Yew Lin, H. Vicky Zhao, Lili Qiu, Dongmei Zhang

**Published:** arXiv:2403.12968 [cs.CL]

**Accepted at:** Findings of ACL 2024

## Abstract

This paper focuses on task-agnostic prompt compression for better generalizability and efficiency.

### The Problem with Existing Approaches

Considering the redundancy in natural language, existing approaches compress prompts by removing tokens or lexical units according to their information entropy obtained from a causal language model such as LLaMa-7B.

The challenge is that information entropy may be a **suboptimal compression metric**:
1. It only leverages unidirectional context and may fail to capture all essential information needed for prompt compression
2. It is not aligned with the prompt compression objective

## LLMLingua-2 Solution

### Data Distillation Procedure

The authors propose a data distillation procedure to derive knowledge from an LLM to compress prompts without losing crucial information, while introducing an extractive text compression dataset.

### Token Classification Approach

Prompt compression is formulated as a **token classification problem** to guarantee the faithfulness of the compressed prompt to the original one.

### Bidirectional Context

Uses a **Transformer encoder** as the base architecture to capture all essential information for prompt compression from the full bidirectional context (unlike unidirectional causal language models).

### Lower Latency

The approach leads to lower latency by explicitly learning the compression objective with smaller models such as:
- XLM-RoBERTa-large
- mBERT (multilingual BERT)

## Evaluation Results

Evaluated on both in-domain and out-of-domain datasets:
- MeetingBank
- LongBench
- ZeroScrolls
- GSM8K
- BBH

### Key Results

Despite its small size, the model shows:
- **Significant performance gains** over strong baselines
- **Robust generalization ability** across different LLMs
- **3x-6x faster** than existing prompt compression methods
- Accelerates end-to-end latency by **1.6x-2.9x** with compression ratios of 2x-5x

## Technical Approach

1. **Data Collection**: Create training data by having GPT-4 identify which tokens are essential vs. removable
2. **Token Classification**: Train a small encoder model to predict token importance
3. **Compression**: Remove tokens classified as non-essential
4. **Faithfulness**: Ensure compressed prompt retains original meaning through the classification formulation

## Advantages over LLMLingua

| Aspect | LLMLingua | LLMLingua-2 |
|--------|-----------|-------------|
| Context | Unidirectional | Bidirectional |
| Model Size | LLaMA-7B | BERT-level |
| Speed | Baseline | 3x-6x faster |
| Task-agnostic | Limited | Better generalization |
| Out-of-domain | Good | Better |

## Models Available

- `microsoft/llmlingua-2-xlm-roberta-large-meetingbank` (larger, more accurate)
- `microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank` (smaller, faster)

## Code

Available at: https://aka.ms/LLMLingua-2

## Citation

```bibtex
@inproceedings{pan-etal-2024-llmlingua,
    title = "{LLML}ingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression",
    author = "Zhuoshi Pan and Qianhui Wu and Huiqiang Jiang and Menglin Xia and Xufang Luo and Jue Zhang and Qingwei Lin and Victor Ruhle and Yuqing Yang and Chin-Yew Lin and H. Vicky Zhao and Lili Qiu and Dongmei Zhang",
    booktitle = "Findings of the Association for Computational Linguistics ACL 2024",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand and virtual meeting",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-acl.57",
    pages = "963--981",
}
```
