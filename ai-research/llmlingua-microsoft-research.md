---
url: https://www.microsoft.com/en-us/research/blog/llmlingua-innovating-llm-efficiency-with-prompt-compression/
fetched: 2026-04-16
summary: Microsoft Research blog on LLMLingua prompt compression framework achieving up to 20x compression with minimal performance loss
---

# LLMLingua: Innovating LLM efficiency with prompt compression

Published December 7, 2023

By Huiqiang Jiang, Research SDE 2; Qianhui Wu, Senior Researcher; Chin-Yew Lin, Senior Principal Research Manager; Yuqing Yang, Principal Research SDE Manager; Lili Qiu, Assistant Managing Director

This research paper was presented at the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023), the premier conference on natural language processing and artificial intelligence.

## The Problem

As large language models (LLMs) models advance and their potential becomes increasingly apparent, an understanding is emerging that the quality of their output is directly related to the nature of the prompt that is given to them. This has resulted in the rise of prompting technologies, such as chain-of-thought (CoT) and in-context-learning (ICL), which facilitate an increase in prompt length. In some instances, prompts now extend to tens of thousands of tokens, or units of text, and beyond.

While longer prompts hold considerable potential, they also introduce a host of issues:
- The need to exceed the chat window's maximum limit
- A reduced capacity for retaining contextual information
- An increase in API costs, both in monetary terms and computational resources

## LLMLingua's Solution

To address these challenges, we introduce a prompt-compression method in our paper, "LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models," presented at EMNLP 2023.

Using a well-trained small language model, such as GPT2-small or LLaMA-7B, LLMLingua identifies and removes unimportant tokens from prompts. This compression technique enables closed LLMs to make inferences from the compressed prompt. Although the token-level compressed prompts may be difficult for humans to understand, they prove highly effective for LLMs.

## LLMLingua's Method and Evaluation

To develop LLMLingua's framework, we employed:
- A budget controller to balance the sensitivities of different modules in the prompt, preserving the language's integrity
- A two-stage process involving coarse-grained prompt compression:
  1. First streamlined the prompt by eliminating certain sentences
  2. Then individually compressed the remaining tokens
- An iterative token-level compression approach, refining the individual relationships between tokens
- Fine-tuning the smaller model to capture the distribution information from different closed LLMs by aligning it with the patterns in the LLMs' generated data through instruction tuning

### Evaluation Results

To assess LLMLingua's performance, we tested compressed prompts on four different datasets:
- GSM8K
- BBH
- ShareGPT
- Arxiv-March23

These encompassed ICL, reasoning, summarization, and conversation tasks.

**Key Results:**
- Achieved up to **20x compression** while preserving the original prompt's capabilities, particularly in ICL and reasoning
- Significantly reduced system latency
- Used LLaMA-7B as the small language model and GPT-3.5-Turbo-0301 as the closed LLM

The results show that LLMLingua maintains the original reasoning, summarization, and dialogue capabilities of the prompt, even at a maximum compression ratio of 20x, as reflected in the evaluation metric (EM) columns. Other compression methods failed to retain key semantic information in prompts, especially in logical reasoning details.

## LLMLingua is Robust, Cost-effective, Efficient, and Recoverable

### Cross-model Performance

LLMLingua also showed impressive results across various small language models and different closed LLMs:
- When using GPT-2-small, LLMLingua achieved a strong performance score of 76.27 under the ¼-shot constraint, close to the LLaMA-7B's result of 77.33 and surpassing the standard prompt results of 74.9
- Even without aligning Claude-v1.3, LLMLingua's score was 82.61 under the ½-shot constraint, outperforming the standard prompt result of 81.8

### Latency Reduction

LLMLingua also proved effective in reducing response length, leading to significant reductions in latency in the LLM's generation process, with reductions ranging between **20 to 30 percent**.

### Recoverability Feature

When GPT-4 was used to restore the compressed prompts, it successfully recovered all key reasoning information from the full nine-step chain-of-thought (CoT) prompting. The recovered prompt was almost identical to the original, and its meaning was retained.

### Acceleration Results

LLMLingua can accelerate LLMs' end-to-end inference by a factor of **1.7–5.7x**. As the compression ratio increases, both the LLMLingua and end-to-end latency decrease, achieving up to a 5.7x acceleration with a 10x token compression rate.

## Practical Applications

LLMLingua has been integrated into:
- **LlamaIndex** - a widely adopted retrieval-augmented generation (RAG) framework
- Product teams to reduce the number of tokens required in LLM calls, particularly for tasks like multi-document question-answering

## LongLLMLingua: For Long-Context Scenarios

For the long-term, we have proposed **LongLLMLingua**, a prompt-compression technique designed for long-context scenarios, such as:
- Retrieval-augmented question-answering tasks in applications like chatbots (useful when information evolves dynamically over time)
- Summarizing online meetings

LongLLMLingua's primary objective is to enhance LLMs' ability to perceive key information, making it suitable for numerous real-world applications, notably information-based chatbots.

## Related Publications

- LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models
- LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression
