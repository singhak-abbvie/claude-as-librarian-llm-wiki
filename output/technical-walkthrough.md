# Building an LLM-Wiki: Complete Technical Walkthrough

A step-by-step guide to creating a personal knowledge base with Claude as your AI librarian

---

## Table of Contents

1. [Introduction](#introduction)
2. [Directory Structure](#directory-structure)
3. [The CLAUDE.md Schema](#the-claudemd-schema)
4. [Step-by-Step Implementation](#step-by-step-implementation)
5. [PDF Extraction Script](#pdf-extraction-script)
6. [Wiki Article Templates](#wiki-article-templates)
7. [Operations Reference](#operations-reference)
8. [Real-World Results](#real-world-results)

---

## Introduction

This document provides a complete technical walkthrough of building an LLM-Wiki — a personal knowledge base where Claude acts as an intelligent librarian that ingests, organizes, and maintains your knowledge.

### What We Built

- **Input**: 54 SuperDataScience podcast transcript PDFs
- **Output**: A fully cross-linked wiki with:
  - 222 wiki articles across 12 topic categories
  - 28 guest profile pages
  - 7 web-researched sources on token optimization
  - 6 synthesized research articles
  - Master index and compilation logs

### Time Investment

| Task | Time | Human Effort |
|------|------|--------------|
| Initial compile | ~5 min | "compile" |
| Web research | ~3 min | One sentence request |
| Wiki creation | Automatic | None |

---

## Directory Structure

### Complete Tree

```
superdatascience_podcasts/
│
├── CLAUDE.md                    # Vault schema - the "constitution"
├── Welcome.md                   # Optional human-readable intro
│
├── raw/                         # Human-curated source material (immutable)
│   └── podcasts_AI/            
│       ├── PT907-Transcript.pdf
│       ├── PT908-Transcript.pdf
│       ├── ... (54 PDF files)
│       └── PT982-Transcript.pdf
│
├── ai-research/                 # AI-discovered sources (immutable once created)
│   ├── llmlingua-microsoft-research.md
│   ├── anthropic-prompt-caching.md
│   ├── openai-prompt-caching.md
│   ├── llmlingua-github-repo.md
│   ├── longllmlingua-paper.md
│   ├── llmlingua2-paper.md
│   ├── autocompressors-paper.md
│   └── token-optimization-techniques-overview.md
│
├── wiki/                        # AI's workspace - organized knowledge
│   ├── _master-index.md        # Top-level navigation
│   ├── log.md                   # All operations logged
│   │
│   ├── agi-future/             # Topic folder
│   │   ├── _index.md           # Topic index
│   │   └── sds-919-hopes-and-fears-of-agi-with-all-time-bestsell.md
│   │
│   ├── ai-agents/              # Topic folder
│   │   ├── _index.md
│   │   ├── sds-908-ai-agents-blackmail-humans-96-of-the-time-age.md
│   │   └── ... (15 articles)
│   │
│   ├── ai-architecture/        
│   ├── ai-business/            
│   ├── ai-careers/             
│   ├── ai-ethics-society/      
│   ├── ai-industry/            
│   ├── ai-products-tools/      
│   ├── ai-science/             
│   ├── icymi-roundups/         
│   ├── llms/                   
│   │
│   ├── token-optimization/     # Research-derived topic
│   │   ├── _index.md
│   │   ├── prompt-caching-overview.md
│   │   ├── llmlingua-prompt-compression.md
│   │   ├── longllmlingua-long-context.md
│   │   ├── llmlingua2-task-agnostic.md
│   │   ├── autocompressors-summary-vectors.md
│   │   └── best-practices-cost-savings.md
│   │
│   └── people/                 # Guest profiles
│       ├── _index.md
│       ├── dr-zohar-bronfman.md
│       └── ... (28 profiles)
│
└── output/                      # Generated artifacts
    ├── medium-blog-llm-wiki-concept.md
    └── technical-walkthrough.md
```

### Directory Purposes

| Directory | Owner | Purpose | Mutability |
|-----------|-------|---------|------------|
| `raw/` | Human | Drop source files | Append-only, immutable |
| `ai-research/` | AI | Save web research | Append-only, immutable |
| `wiki/` | AI | Organized knowledge | AI maintains |
| `output/` | Both | Reports, exports | Temporary/promotable |

---

## The CLAUDE.md Schema

This is the complete schema file that governs the vault:

```markdown
# Vault Schema

You are the librarian of this vault. The `wiki/` folder is your domain. 
You write and maintain every file in `wiki/`. The human rarely edits wiki files directly.

Read this file at the start of every session. Follow the rules below for every operation.

## Layers

- `raw/` is the inbox. The human drops source material here (articles, papers, 
  transcripts, pasted notes, images). You read from `raw/`. You never write to `raw/`. 
  Raw files are immutable.

- `ai-research/` is your research folder. When you conduct autonomous web research, 
  save the full cleaned source content here as markdown files. You CAN write to this folder. 
  Files here are immutable once saved (do not overwrite, create new files). 
  This separates human-curated sources (`raw/`) from AI-discovered sources (`ai-research/`).

- `wiki/` is your workspace. You write topics, people, research, tools, topic indexes, 
  and the master index here. Everything in `wiki/` is organized by topic folder. 
  You compile from BOTH `raw/` and `ai-research/` into `wiki/`.

- `output/` is for query results, reports, slide decks, and generated artifacts that 
  are not part of the permanent wiki. You promote valuable outputs into `wiki/` as 
  new articles when the human asks.

- `CLAUDE.md` (this file) is the schema. It defines every operation you perform. 
  Co-evolve it with the human over time.

## Operations

### Ingest

Triggered when the human says "compile" or drops new files in `raw/`.

For each new raw file:

1. Read the raw file in full.
2. Identify the core concept or topics the file covers.
3. Check `wiki/_master-index.md` to see if a matching topic folder already exists.
4. If the topic exists, read the topic's `_index.md` and any related articles, 
   then write or update a wiki article covering the new source. Add backlinks 
   from any articles it touches.
5. If the topic does not exist, create a new folder under `wiki/` with a lowercase 
   hyphenated name. Create an `_index.md` inside it. Write the first wiki article 
   for this topic.
6. Every wiki article must include:
   - A top-level `# Title`.
   - A `**Source:** path/to/raw/file.md` line immediately under the title.
   - A short intro paragraph (2 to 4 sentences) summarizing the article.
   - A `## Key Takeaways` section with bullet points.
   - A `## Related` section with `[[wikilinks]]` to 3 to 8 related pages elsewhere in the wiki.
7. Update the topic's `_index.md` to list the new article.
8. Update `wiki/_master-index.md` if a new topic was created or an existing topic 
   changed meaningfully.
9. Append one line to `wiki/log.md` in this format:
   ```
   ## [YYYY-MM-DD HH:MM] ingest | Source title | topic/article.md
   ```
10. If the source spans multiple topics, create articles in both topics and cross-link them.

One raw file typically touches 10 to 15 wiki files in a single ingest pass. 
That is expected. Do all the updates in one run.

### Research

Triggered when the human asks you to research a topic, or when a query reveals 
gaps the wiki cannot answer from existing sources.

1. Search the web for relevant, high-quality sources on the topic.
2. **One source, one file.** For EACH URL or source you find, save it as its OWN 
   separate markdown file in `ai-research/`. Do NOT combine multiple sources into 
   one file. If you found 4 URLs, that is 4 files. Use this format for each:
   ```
   ---
   url: https://example.com/article
   fetched: YYYY-MM-DD
   summary: One-line description of what this source covers
   ---

   [Full article content in markdown, cleaned, not summarized]
   ```
3. File names should be descriptive and lowercase hyphenated: 
   `ai-research/qmd-github-readme.md`, `ai-research/qmd-hackernews-discussion.md`.
4. Save the FULL cleaned content from each source, not a summary. The wiki article 
   is where summarization happens, not here. These files are the source of truth 
   for citation verification.
5. Do NOT overwrite existing files in `ai-research/`. Always create new files.
6. After saving ALL sources, run the standard Ingest procedure to compile them 
   into `wiki/`. A single wiki article can cite multiple `ai-research/` files 
   in its `**Source:**` line.
7. In the wiki article's `**Source:**` line, list every `ai-research/` file used 
   so the lint pass can verify each claim back to its original source.

The human can review `ai-research/` at any time to see what you found. 
These files are immutable once saved.

### Query

Triggered when the human asks a question about the wiki.

1. Read `wiki/_master-index.md` first to identify which topic folder is relevant.
2. Read the matching topic's `_index.md` to identify which articles to load.
3. Read 1 to 3 specific articles in full.
4. If the question spans multiple topics, repeat steps 1 to 3 for each topic.
5. Synthesize the answer. Cite every claim with the wiki article it came from 
   using `[[wikilinks]]` and include the raw source file path each article cites.
6. If the answer is substantial and would be useful later, ask the human whether 
   to file it as a new wiki article. If yes, write it in the appropriate topic 
   folder and cross-link.

Default to 3 to 4 file reads. Do not grep the entire vault. 
The index files are your retrieval layer.

### Lint

Triggered when the human says "lint" or "audit the wiki".

Read every file in `wiki/` and produce a report covering:

1. **Contradictions.** Pages that make conflicting claims. Include the file paths 
   and the conflicting statements.
2. **Stale claims.** Statements in older articles that newer raw sources have 
   updated or superseded.
3. **Orphan pages.** Articles with zero inbound wikilinks from other articles.
4. **Missing concepts.** Concepts mentioned in 3 or more articles that do not 
   have their own page yet.
5. **Missing cross-links.** Pairs of articles that reference related ideas but 
   do not link to each other.
6. **Unsourced claims.** Statements in wiki articles that do not trace back to 
   a `**Source:**` raw file, or claims that do not appear in the cited source.
7. **Suggested new articles.** 3 to 5 concrete article ideas that would strengthen 
   the wiki based on gaps you found.

Output the report to `output/lint-report-YYYY-MM-DD.md`. Do not make changes 
during the lint pass. Wait for the human to approve fixes.

When the human approves specific fixes, apply them one at a time and log 
each one in `wiki/log.md`.

### Log

Every operation appends one line to `wiki/log.md`.
```

### Key Design Principles

1. **Separation of concerns**: Human sources (`raw/`) vs AI sources (`ai-research/`)
2. **Immutability**: Source folders are append-only, never modified
3. **Transparency**: Every claim traces back to a source
4. **Auditability**: All operations are logged with timestamps
5. **Co-evolution**: The schema itself can be updated collaboratively

---

## Step-by-Step Implementation

### Step 1: Create the Directory Structure

```bash
mkdir superdatascience_podcasts
cd superdatascience_podcasts
mkdir raw ai-research wiki output
mkdir wiki/people
```

### Step 2: Create CLAUDE.md

Copy the schema above into `superdatascience_podcasts/CLAUDE.md`.

### Step 3: Add Your Raw Sources

```bash
# Copy your PDFs/files to raw/
cp ~/Downloads/*.pdf raw/podcasts_AI/
```

### Step 4: Trigger the Compile

Open VS Code with GitHub Copilot (using Claude) and simply say:

> **"compile"**

Claude will:
1. Read CLAUDE.md to understand the schema
2. Process all files in `raw/`
3. Create the wiki structure

### Step 5: Research New Topics

> **"research effective ways to save token cost or token memory compression"**

Claude will:
1. Search for authoritative sources
2. Save each to `ai-research/` with full content
3. Create wiki articles synthesizing the research
4. Cross-link with existing wiki content

### Step 6: Query Your Knowledge Base

> **"What do the podcasts say about the future of AI agents?"**

Claude will:
1. Consult the master index
2. Read relevant topic indexes
3. Synthesize an answer with citations

### Step 7: Audit for Quality

> **"lint"**

Generates a comprehensive audit report.

---

## PDF Extraction Script

For bulk PDF processing, we used this Python script:

```python
"""
Extract PDF transcripts and compile wiki structure.
"""
from pypdf import PdfReader
import os
import re
from pathlib import Path
from datetime import datetime

RAW_DIR = Path('raw/podcasts_AI')
WIKI_DIR = Path('wiki')

# Topic classification based on keywords
TOPIC_KEYWORDS = {
    'ai-agents': ['agent', 'agentic', 'multi-agent', 'automating'],
    'llms': ['llm', 'gpt', 'pre-training', 'transformer', 'language model'],
    'agi-future': ['agi', 'superintelligence', 'future of ai'],
    'ai-architecture': ['causal ai', 'data lake', 'mixture-of-expert'],
    'ai-industry': ['journalism', 'legal', 'manufacturing', 'enterprise'],
    'ai-careers': ['career', 'engineer', 'hired', 'work'],
    'ai-ethics-society': ['global issues', 'phishing', 'misalignment'],
    'ai-products-tools': ['notebook', 'code review', 'product'],
    'ai-business': ['profit', 'optimization', 'bubble', 'strategy'],
    'ai-science': ['physics', 'music', 'art', 'creative', 'neuroscience'],
    'icymi-roundups': ['in case you missed it', 'icymi']
}


def extract_pdf_content(pdf_path):
    """Extract full text from PDF."""
    reader = PdfReader(pdf_path)
    return '\n\n'.join(page.extract_text() for page in reader.pages)


def parse_transcript(content, filename):
    """Parse transcript to extract metadata."""
    clean = ' '.join(content.split()[:200])
    
    # Extract episode number and title
    match = re.search(r'EPISODE\s+(\d+):\s*(.+?)\s*Show Notes', clean, re.IGNORECASE)
    if match:
        ep_num, title = match.group(1), match.group(2)
    else:
        ep_num = re.search(r'PT(\d+)', filename).group(1)
        title = "Unknown Title"
    
    # Extract guest name
    guest_match = re.search(r'WITH\s+(.+?)(?:\s*$|,)', title, re.IGNORECASE)
    guest = guest_match.group(1).strip() if guest_match else None
    
    return {
        'episode': ep_num,
        'title': title,
        'guest': guest,
        'content': content,
        'filename': filename
    }


def classify_topics(title, content):
    """Classify episode into topics based on keywords."""
    topics = []
    text = (title + ' ' + content[:5000]).lower()
    
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(kw.lower() in text for kw in keywords):
            topics.append(topic)
    
    return topics or ['ai-industry']


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'\s+', '-', text)[:50]


def main():
    WIKI_DIR.mkdir(exist_ok=True)
    
    # Process all PDFs
    episodes = []
    for pdf in sorted(RAW_DIR.glob('*.pdf')):
        content = extract_pdf_content(pdf)
        parsed = parse_transcript(content, pdf.name)
        parsed['topics'] = classify_topics(parsed['title'], content)
        episodes.append(parsed)
    
    # Create topic folders and articles
    # ... (full implementation in repository)

if __name__ == '__main__':
    main()
```

### Required Dependencies

```bash
pip install pypdf
```

---

## Wiki Article Templates

### Topic Index (`_index.md`)

```markdown
# Topic Name

Description of what this topic covers.

## Articles

- [[topic/article-slug|SDS 907: Article Title]]
- [[topic/article-slug|SDS 908: Article Title]]
```

### Individual Article

```markdown
# SDS 907: Episode Title

**Source:** raw/podcasts_AI/PT907-Transcript.pdf

Brief 2-4 sentence summary of what this episode covers and why it's valuable.

## Key Takeaways

- Key point extracted from the content
- Another important insight
- Actionable recommendation

## Related

[[other-topic/_index|Related Topic]]
[[people/guest-name|Guest Name]]
[[same-topic/related-article|Related Episode]]
```

### Master Index (`_master-index.md`)

```markdown
# SuperDataScience Podcast Wiki

A knowledge base compiled from podcast transcripts.

## Topics

- [[agi-future/_index|AGI & Future]] (10 episodes)
- [[ai-agents/_index|AI Agents]] (15 episodes)
- [[llms/_index|Large Language Models]] (19 episodes)

## People

- [[people/_index|Featured Guests]] (28 guests)

## Statistics

- Total Episodes: 54
- Topic Categories: 12
- Unique Guests: 28

---
*Last compiled: 2026-04-16*
```

### Research Source (`ai-research/*.md`)

```markdown
---
url: https://example.com/source-article
fetched: 2026-04-16
summary: One-line description of the source
---

# Article Title

[Full content preserved from the source, cleaned and formatted as markdown]

## Section Headings Preserved

All original content kept intact for citation verification.
```

---

## Operations Reference

| Command | Trigger | Input | Output |
|---------|---------|-------|--------|
| **Compile** | "compile" | Files in `raw/` | Wiki articles, indexes, log entries |
| **Research** | "research [topic]" | Web search | `ai-research/` files + wiki articles |
| **Query** | Any question | Wiki content | Synthesized answer with citations |
| **Lint** | "lint" | Entire wiki | `output/lint-report.md` |

### Operation Flow

```
┌─────────────────────────────────────────────────────────────┐
│                      Human Actions                          │
├─────────────────────────────────────────────────────────────┤
│  Drop files in raw/  │  Ask questions  │  Say "compile"    │
└──────────┬────────────┴────────┬────────┴────────┬──────────┘
           │                     │                 │
           ▼                     ▼                 ▼
┌──────────────────────────────────────────────────────────────┐
│                    CLAUDE.md Schema                          │
│                 (Reads at session start)                     │
└──────────────────────────────────────────────────────────────┘
           │                     │                 │
           ▼                     ▼                 ▼
┌──────────────────┐   ┌─────────────────┐   ┌────────────────┐
│   Read raw/      │   │  Query wiki/    │   │  Process +     │
│   files          │   │  synthesize     │   │  create wiki   │
└────────┬─────────┘   └────────┬────────┘   └───────┬────────┘
         │                      │                    │
         ▼                      ▼                    ▼
┌──────────────────────────────────────────────────────────────┐
│                        wiki/                                 │
│  ├── _master-index.md                                        │
│  ├── topic-folders/_index.md + articles                      │
│  ├── people/                                                 │
│  └── log.md                                                  │
└──────────────────────────────────────────────────────────────┘
```

---

## Real-World Results

### Before

```
raw/podcasts_AI/
├── PT907-Transcript.pdf   (unread)
├── PT908-Transcript.pdf   (unread)
├── ... 
└── PT982-Transcript.pdf   (unread)

Total: 54 PDFs, ~500 pages of valuable content, effectively inaccessible
```

### After

```
wiki/
├── _master-index.md                    # Navigation hub
├── log.md                               # 230+ logged operations
├── 12 topic folders/                    # Organized by theme
│   └── 222 cross-linked articles        # Searchable, discoverable
├── people/                              # 28 guest profiles
└── token-optimization/                  # Research-derived content
    └── 6 synthesized articles           # From web research

ai-research/
└── 7 complete source files              # Full citations preserved
```

### Statistics

| Metric | Value |
|--------|-------|
| Source PDFs | 54 |
| Wiki articles created | 222 |
| Topic categories | 12 |
| Guest profiles | 28 |
| Cross-links generated | ~1,500+ |
| Research sources saved | 7 |
| Time to compile | ~5 minutes |
| Human effort | "compile" |

---

## Conclusion

The LLM-Wiki pattern transforms how we manage personal knowledge:

1. **Minimal cognitive load** — Just drop files and ask questions
2. **Automatic organization** — Topics emerge from content
3. **Full traceability** — Every claim cites its source
4. **Living knowledge** — Grows and improves over time
5. **AI-native** — Leverages LLM capabilities for synthesis

The entire system is governed by a single markdown file (`CLAUDE.md`) that any LLM can read and follow. No special tools. No new apps to learn. Just structured knowledge, automatically maintained.

---

*This walkthrough accompanies the blog post "The LLM-Wiki: How I Built a Personal Knowledge Base with Claude as My Librarian"*
