---
url: https://github.com/microsoft/LLMLingua
fetched: 2026-04-16
summary: Microsoft's LLMLingua GitHub repository - prompt compression library achieving up to 20x compression with minimal performance loss
---

# LLMLingua Series | Effectively Deliver Information to LLMs via Prompt Compression

GitHub Repository: microsoft/LLMLingua

## Overview

LLMLingua utilizes a compact, well-trained language model (e.g., GPT2-small, LLaMA-7B) to identify and remove non-essential tokens in prompts. This approach enables efficient inference with large language models (LLMs), achieving up to **20x compression** with minimal performance loss.

## The LLMLingua Family

### LLMLingua (EMNLP 2023)
Compressing Prompts for Accelerated Inference of Large Language Models
- Authors: Huiqiang Jiang, Qianhui Wu, Chin-Yew Lin, Yuqing Yang and Lili Qiu

### LongLLMLingua (ACL 2024)
Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression
- Mitigates the 'lost in the middle' issue in LLMs
- Enhances long-context information processing
- Reduces costs and boosts efficiency
- Improves RAG performance by up to **21.4%** using only **1/4 of the tokens**

### LLMLingua-2 (ACL 2024 Findings)
Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression
- Small-size yet powerful prompt compression method
- Trained via data distillation from GPT-4 for token classification
- Uses a BERT-level encoder (XLM-RoBERTa-large, mBERT)
- Excels in task-agnostic compression
- Surpasses LLMLingua in handling out-of-domain data
- **3x-6x faster** performance than LLMLingua

### SecurityLingua (CoLM 2025)
Efficient Defense of LLM Jailbreak Attacks via Security-Aware Prompt Compression
- Safety guardrail model using security-aware prompt compression
- Reveals malicious intentions behind jailbreak attacks
- Negligible overhead and **100x less token costs** compared to state-of-the-art LLM guardrails

## Key Benefits

- 💰 **Cost Savings**: Reduces both prompt and generation lengths with minimal overhead
- 📝 **Extended Context Support**: Enhances support for longer contexts, mitigates the "lost in the middle" issue
- ⚖️ **Robustness**: No additional training needed for LLMs
- 🕵️ **Knowledge Retention**: Maintains original prompt information like ICL and reasoning
- 📜 **KV-Cache Compression**: Accelerates inference process
- 🪃 **Comprehensive Recovery**: GPT-4 can recover all key information from compressed prompts

## Quick Start

### Installation

```bash
pip install llmlingua
```

### Basic Usage (LLMLingua)

```python
from llmlingua import PromptCompressor

llm_lingua = PromptCompressor()
compressed_prompt = llm_lingua.compress_prompt(
    prompt, 
    instruction="", 
    question="", 
    target_token=200
)
```

### Example Output

```python
{
    'compressed_prompt': 'Question: Sam bought a dozen boxes...',
    'origin_tokens': 2365,
    'compressed_tokens': 211,
    'ratio': '11.2x',
    'saving': ', Saving $0.1 in GPT-4.'
}
```

### Using Different Models

```python
# Using phi-2 model
llm_lingua = PromptCompressor("microsoft/phi-2")

# Using quantized model (requires <8GB GPU memory)
# pip install optimum auto-gptq
llm_lingua = PromptCompressor(
    "TheBloke/Llama-2-7b-Chat-GPTQ", 
    model_config={"revision": "main"}
)
```

### LongLLMLingua Usage

```python
from llmlingua import PromptCompressor

llm_lingua = PromptCompressor()
compressed_prompt = llm_lingua.compress_prompt(
    prompt_list,
    question=question,
    rate=0.55,
    # Special parameters for LongLLMLingua
    condition_in_question="after_condition",
    reorder_context="sort",
    dynamic_context_compression_ratio=0.3,  # or 0.4
    condition_compare=True,
    context_budget="+100",
    rank_method="longllmlingua",
)
```

### LLMLingua-2 Usage

```python
from llmlingua import PromptCompressor

llm_lingua = PromptCompressor(
    model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",
    use_llmlingua2=True,
)
compressed_prompt = llm_lingua.compress_prompt(
    prompt, 
    rate=0.33, 
    force_tokens=['\n', '?']
)
```

### LLMLingua-2 Small Model

```python
llm_lingua = PromptCompressor(
    model_name="microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank",
    use_llmlingua2=True,
)
```

### SecurityLingua Usage

```python
from llmlingua import PromptCompressor

securitylingua = PromptCompressor(
    model_name="SecurityLingua/securitylingua-xlm-s2s",
    use_slingua=True
)
intention = securitylingua.compress_prompt(malicious_prompt)
```

## Advanced Usage: Structured Prompt Compression

Split text into sections, decide on whether to compress and its rate. Use `<llmlingua></llmlingua>` tags for context segmentation:

```python
structured_prompt = """<llmlingua, compress=False>Speaker 4:</llmlingua>
<llmlingua, rate=0.4> Thank you. And can we do the functions for content?</llmlingua>
<llmlingua, compress=False>Speaker 0:</llmlingua>
<llmlingua, rate=0.4> Item 11 is a communication from Council...</llmlingua>
<llmlingua, compress=False>Speaker 4:</llmlingua>
<llmlingua, rate=0.6> We have a promotion and a second time...</llmlingua>"""

compressed_prompt = llm_lingua.structured_compress_prompt(
    structured_prompt, 
    instruction="", 
    question="", 
    rate=0.5
)
```

## Integrations

LLMLingua has been integrated into:
- **LangChain** - Popular RAG framework
- **LlamaIndex** - Widely adopted RAG framework
- **Prompt flow** - Microsoft's LLM-based AI applications framework

## Related Projects from Microsoft Research

- **SCBench**: KV cache-centric analysis evaluating long-context methods
- **RetrievalAttention**: KV cache offloading work accelerating long-context LLM inference via vector retrieval
- **MInference**: Speed up Long-context LLMs' inference, reduces inference latency by up to 10X for pre-filling on an A100 while maintaining accuracy in 1M tokens prompt

## Examples Available

- LLMLingua-2
- RAG (Retrieval-Augmented Generation)
- Online Meeting transcription
- Chain-of-Thought (CoT)
- Code compression
- RAG using LlamaIndex

## License

MIT License
