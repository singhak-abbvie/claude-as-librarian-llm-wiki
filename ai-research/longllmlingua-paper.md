---
url: https://arxiv.org/abs/2310.06839
fetched: 2026-04-16
summary: LongLLMLingua paper - prompt compression for long context scenarios, achieving 21.4% performance boost with 4x fewer tokens
---

# LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression

**Authors:** Huiqiang Jiang, Qianhui Wu, Xufang Luo, Dongsheng Li, Chin-Yew Lin, Yuqing Yang, Lili Qiu

**Published:** arXiv:2310.06839 [cs.CL]

**Accepted at:** ACL 2024

## Abstract

In long context scenarios, large language models (LLMs) face three main challenges:
1. Higher computational cost
2. Performance reduction
3. Position bias

Research indicates that LLM performance hinges on the density and position of key information in the input prompt.

## LongLLMLingua Solution

Inspired by these findings, the authors propose LongLLMLingua for prompt compression towards improving LLMs' perception of the key information to simultaneously address the three challenges.

## Key Results

### Performance Improvements

- **NaturalQuestions benchmark**: Boosts performance by up to **21.4%** with around **4x fewer tokens** in GPT-3.5-Turbo, leading to substantial cost savings

### Cost Reduction

- Achieves a **94.0% cost reduction** in the LooGLE benchmark

### Latency Acceleration

When compressing prompts of about 10k tokens at ratios of 2x-6x:
- Accelerates end-to-end latency by **1.4x-2.6x**

## Applications

LongLLMLingua is designed for long-context scenarios such as:
- Retrieval-augmented question-answering tasks
- Chatbots with dynamically evolving information
- Summarizing online meetings

## Primary Objective

Enhance LLMs' ability to perceive key information, making it suitable for numerous real-world applications, notably information-based chatbots.

## Addressing "Lost in the Middle"

A key innovation of LongLLMLingua is mitigating the "lost in the middle" phenomenon - where LLMs tend to lose track of relevant information that appears in the middle of long contexts. By compressing and reorganizing the prompt, LongLLMLingua helps LLMs focus on the most relevant information regardless of its original position.

## Code

Available at: https://aka.ms/LongLLMLingua

## Citation

```bibtex
@inproceedings{jiang-etal-2024-longllmlingua,
    title = "{L}ong{LLML}ingua: Accelerating and Enhancing {LLM}s in Long Context Scenarios via Prompt Compression",
    author = "Huiqiang Jiang and Qianhui Wu and Xufang Luo and Dongsheng Li and Chin-Yew Lin and Yuqing Yang and Lili Qiu",
    booktitle = "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.acl-long.91",
    pages = "1658--1677",
}
```
