# The LLM-Wiki: How I Built a Personal Knowledge Base with Claude as My Librarian

*Inspired by Andrej Karpathy's vision of AI agents that live on your computer*

---

## The Problem with Personal Knowledge Management

We're drowning in information. Articles saved to Pocket that we'll never read. Bookmarks organized into folders we'll never open. Notes scattered across Notion, Obsidian, Apple Notes, and random text files. Podcast episodes with brilliant insights that evaporate the moment we finish listening.

I had 54 SuperDataScience podcast transcripts sitting in a folder. PDFs full of conversations with AI researchers, entrepreneurs, and thought leaders discussing agents, LLMs, the future of work, AGI timelines, and more. Thousands of pages of potentially transformative knowledge... collecting digital dust.

**The problem isn't capturing information. It's *doing* something with it.**

## Enter the LLM-Wiki Concept

Andrej Karpathy, in his [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/), highlighted a paradigm shift with Claude Code: *"LLMs that live on your computer."* Not just websites you visit like Google, but *"a little spirit/ghost that lives on your computer"* — an AI that understands your context, your files, your environment.

This sparked an idea: **What if the LLM wasn't just a chatbot, but the *librarian* of my personal knowledge base?**

Not a passive system that waits for me to organize things. Not another tool I need to learn. But an active agent that:
- Ingests raw material I throw at it
- Synthesizes information across sources
- Maintains a structured wiki automatically
- Surfaces connections I'd never see
- Keeps everything cross-linked and discoverable

I call this the **LLM-Wiki** — a personal knowledge base where the AI isn't just a query interface, it's the *curator*.

## The Architecture: Layers, Not Chaos

The structure is deliberately simple — inspired by Karpathy's [append-and-review note](https://karpathy.bearblog.dev/the-append-and-review-note/) philosophy of "one text note ftw" but adapted for collaborative human-AI knowledge management:

```
superdatascience_podcasts/
├── CLAUDE.md           # The vault's "constitution"
├── raw/                # Human drops material here
├── ai-research/        # AI saves researched sources here
├── wiki/               # AI's workspace — organized knowledge
│   ├── _master-index.md
│   ├── topic-folders/
│   └── log.md
└── output/             # Reports, artifacts, exports
```

### Layer 1: `raw/` — The Inbox

The human simply drops files here. PDFs, transcripts, articles, pasted notes. No organization required. No tagging. No thinking about "where does this go?"

The cognitive load is near-zero: *"I found something interesting"* → drop it in `raw/`.

### Layer 2: `ai-research/` — AI's Discovery Zone

When I ask Claude to research a topic, it fetches sources from the web and saves them here. Each file is a complete, cleaned source with metadata:

```markdown
---
url: https://example.com/article
fetched: 2026-04-16
summary: One-line description
---

[Full article content, not summarized]
```

This separation is crucial: I can always distinguish between *my* curated sources (`raw/`) and *AI-discovered* sources (`ai-research/`). Trust but verify.

### Layer 3: `wiki/` — The Knowledge Graph

This is Claude's workspace. It reads from `raw/` and `ai-research/`, then writes:
- Topic indexes (`wiki/topic-name/_index.md`)
- Individual articles with source citations
- Cross-links to related concepts
- A master index for navigation
- A log of all operations

Every wiki article follows a consistent structure:
```markdown
# Title

**Source:** path/to/raw/file.md

Short intro paragraph summarizing the content.

## Key Takeaways
- Bullet point insights

## Related
[[wikilinks]] to related pages
```

### Layer 4: `output/` — Deliverables

Reports, presentations, synthesized analyses. When I need to produce something from the wiki, it goes here. These can be "promoted" back into the wiki when valuable.

## The Magic: CLAUDE.md

The entire system is governed by a single markdown file: `CLAUDE.md`. This is the vault's "constitution" — a document Claude reads at the start of every session that defines:

1. **The territory** — what each folder is for
2. **Operations** — exactly how to ingest, research, query, and lint
3. **Output formatting** — wiki article structure, wikilinks, source citations
4. **Evolution** — the schema itself can be updated collaboratively

Here's the key insight: **CLAUDE.md isn't just documentation. It's the prompt.**

By codifying the rules in a structured markdown file that lives *in* the vault, Claude can:
- Reference it for any operation
- Understand its boundaries and responsibilities
- Maintain consistency across sessions
- Co-evolve the schema with the human over time

This is what "AI that lives on your computer" actually looks like. Not a cloud service. Not a new app to learn. Just a markdown file that turns any LLM into a domain-specific agent.

## The Workflow in Action

### Compile Operation

I dropped 54 podcast PDFs in `raw/podcasts_AI/`. One word to Claude:

> **"compile"**

What happened:
1. Claude read all 54 PDFs using `pypdf`
2. Extracted titles, guests, topics
3. Classified each into 11 topic categories (agents, LLMs, careers, ethics, etc.)
4. Created 222 wiki articles (episodes touch multiple topics)
5. Built 28 guest profiles with linked episodes
6. Generated a master index with statistics
7. Logged every operation with timestamps

**Time: ~5 minutes. Human effort: One word.**

### Research Operation

I wanted to learn about token cost optimization. One request:

> **"research effective ways to save token cost or token memory compression"**

Claude:
1. Searched for authoritative sources
2. Saved 7 complete articles to `ai-research/`
3. Created a new `wiki/token-optimization/` topic
4. Wrote 6 interconnected articles covering:
   - Prompt caching (OpenAI, Anthropic)
   - LLMLingua compression (20x reduction!)
   - LongLLMLingua for RAG
   - LLMLingua-2 for faster compression
   - AutoCompressors for vector-based context
   - Best practices with cost calculations

Every article cites its sources. Every claim is traceable.

### Query Operation

When I need information, Claude:
1. Reads the master index
2. Identifies relevant topic folders
3. Reads specific articles
4. Synthesizes an answer with citations

No grep. No CTRL+F. No remembering where I put things.

## Why This Works

### 1. Cognitive Offloading Done Right

Traditional PKM systems require you to:
- Decide where to file things
- Remember your taxonomy
- Maintain links manually
- Review and prune regularly

The LLM-Wiki inverts this. The human only needs to:
- Drop interesting things in `raw/`
- Ask questions
- Occasionally say "compile" or "lint"

The AI handles organization, linking, and maintenance.

### 2. Structure Emerges from Content

I didn't pre-define "11 topic categories." Claude analyzed the content and *discovered* the natural clusters: AI agents, LLMs, careers, ethics, business, architecture...

The wiki structure reflects the *actual* landscape of the information, not my preconceived notions.

### 3. Sources Stay Sacred

Every wiki article links back to its source. The `raw/` folder is immutable. The `ai-research/` folder timestamps everything.

When I read a claim in the wiki, I can always verify it. The knowledge base is *auditable*.

### 4. The AI is Constrained

Claude doesn't just "do whatever." It follows the CLAUDE.md schema:
- It never writes to `raw/`
- It always cites sources
- It maintains the logging format
- It uses the specified article structure

The LLM's creativity is channeled into useful work, not chaos.

## Lessons from Building This

### Start with Operations, Not Structure

I didn't design the perfect folder hierarchy first. I started by defining *what I wanted to do*:
- Ingest new material
- Research topics
- Query the knowledge base
- Audit for consistency

The structure emerged to support those operations.

### The Schema is a Living Document

CLAUDE.md started simpler. As I used the system, I added rules:
- "One source, one file in ai-research/"
- "Always include Related links"
- "Log every operation"

The schema co-evolves with usage.

### Embrace Multiplicity

One podcast episode might touch agents, ethics, AND business. Instead of forcing a single category, the wiki creates articles in *all* relevant topics with cross-links.

This mirrors how knowledge actually works — concepts span domains.

### The Lint Operation is Underrated

Running `lint` asks Claude to audit the entire wiki for:
- Contradictions between articles
- Orphan pages with no inbound links
- Missing concepts mentioned but never defined
- Stale claims superseded by newer sources

It's like having a fact-checker review your entire knowledge base.

## The Future: Your AI Research Assistant

This isn't just for podcasts. Imagine:
- **Academic researchers** dropping papers in raw/, having the AI maintain a literature review wiki with automatic citation graphs
- **Investors** building a company wiki from earnings calls, news, and research reports
- **Writers** creating a story bible that grows and cross-links as they develop their world
- **Students** turning textbooks and lecture notes into an interconnected study guide
- **Journalists** maintaining a source database with automatic relationship mapping

The pattern is universal:
1. Drop raw material
2. AI organizes and links
3. Query and generate from structured knowledge
4. Audit for quality

## Try It Yourself

The complete system is defined in one markdown file. Create a `CLAUDE.md` in any folder and you have an LLM-Wiki. Here's the minimal version:

```markdown
# Vault Schema

## Layers
- `raw/` — Drop sources here. Immutable.
- `wiki/` — AI's workspace. Organized knowledge.

## Operations

### Ingest
When human says "compile":
1. Read new files in raw/
2. Create/update wiki articles
3. Add source citations and cross-links
4. Update master index

### Query
When human asks a question:
1. Read relevant wiki articles
2. Synthesize answer with [[wikilinks]]
3. Cite sources
```

That's it. Everything else is elaboration.

## Conclusion: The Librarian Pattern

We're at an inflection point in personal knowledge management. The old paradigm was: *"I organize, computer stores."* The new paradigm is: *"I collect, AI organizes, we collaborate."*

Andrej Karpathy calls current LLMs "ghosts" — entities with capabilities we're still learning to harness. The LLM-Wiki pattern turns that ghost into a librarian: bounded, useful, trustworthy.

Not AGI. Not a replacement for human judgment. Just a really good assistant that:
- Reads everything I can't
- Organizes what I won't
- Surfaces what I'd miss
- Maintains what I'd forget

**My podcast folder went from 54 dusty PDFs to a searchable, cross-linked, living knowledge base in 5 minutes.**

The future of knowledge work isn't more apps. It's AI that lives in your existing workflows, governed by simple rules you can read and modify.

Start your own LLM-Wiki. All it takes is a markdown file and a vision for what you want to know.

---

*[Your Name]*  
*April 2026*

---

**Connect:**
- GitHub: [link]
- Twitter: [link]

**Related Reading:**
- Andrej Karpathy's [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/)
- Andrej Karpathy's [The Append-and-Review Note](https://karpathy.bearblog.dev/the-append-and-review-note/)
- Microsoft's [LLMLingua](https://llmlingua.com/) for prompt compression
