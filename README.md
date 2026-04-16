# 🏛️ Claude as Librarian: LLM-Wiki

> **A personal knowledge management system where Claude acts as your librarian, automatically organizing and cross-linking your knowledge base.**

[![Inspired by](https://img.shields.io/badge/Inspired%20by-Andrej%20Karpathy-blue)](https://karpathy.ai)
[![Built with](https://img.shields.io/badge/Built%20with-Claude-orange)](https://anthropic.com)

---

## 📖 The Concept

This project implements the **"LLM-Wiki"** concept — an idea explored by Andrej Karpathy where an LLM serves as an intelligent librarian for your personal knowledge base. Instead of manually organizing notes, tagging files, and creating cross-references, you drop raw content into an inbox and let Claude do the rest.

### Why This Approach?

| Traditional Note-Taking | LLM-Wiki |
|------------------------|----------|
| You organize everything manually | Claude organizes for you |
| Tags and folders get messy over time | Consistent structure enforced by schema |
| Cross-references require manual effort | Automatic wikilinks between related topics |
| Searching means remembering keywords | Natural language queries with cited answers |
| Knowledge silos form naturally | Connections surfaced automatically |

---

## 🏗️ Architecture

The vault is organized into **4 layers**, each with a specific purpose:

```
superdatascience_podcasts/
├── CLAUDE.md              # The "constitution" - defines all operations
├── raw/                   # 📥 INBOX - Drop source material here
│   └── podcasts_AI/       #    54 podcast transcripts (PDFs)
├── ai-research/           # 🔍 AI-discovered sources (web research)
│   ├── llmlingua-*.md     #    7 research files on token optimization
│   └── ...
├── wiki/                  # 📚 THE WIKI - Claude's workspace
│   ├── _master-index.md   #    Entry point to all topics
│   ├── log.md             #    Append-only operation log
│   ├── ai-agents/         #    Topic folders with articles
│   ├── llms/
│   ├── people/            #    Guest profiles
│   └── ... (12 topics)
└── output/                # 📤 Query results, reports, artifacts
    ├── query-*.md         #    Saved Q&A history
    └── medium-blog-*.md   #    Generated content
```

### Layer Rules

| Layer | Who Writes | Purpose |
|-------|-----------|---------|
| `raw/` | Human only | Source material inbox (immutable) |
| `ai-research/` | Claude only | Web research sources (immutable once saved) |
| `wiki/` | Claude only | Compiled knowledge base |
| `output/` | Claude only | Query results and generated artifacts |

---

## ⚙️ Operations

Claude responds to four primary operations, all defined in `CLAUDE.md`:

### 1. 📥 Ingest (`"compile"`)

Triggered by saying **"compile"** or dropping new files in `raw/`.

```
Human: compile

Claude:
1. Reads all new files in raw/
2. Identifies topics and key concepts
3. Creates/updates wiki articles with proper structure
4. Adds cross-links between related content
5. Updates topic indexes and master index
6. Logs the operation
```

**One raw file → 10-15 wiki file updates** (articles, indexes, cross-links)

### 2. 🔍 Research

Triggered by asking Claude to **research a topic**.

```
Human: research effective ways to reduce LLM token costs

Claude:
1. Searches the web for high-quality sources
2. Saves FULL content of each source to ai-research/
3. Runs Ingest to compile findings into wiki/
4. Creates new topic folder if needed
```

**Separates human-curated sources (`raw/`) from AI-discovered sources (`ai-research/`)**

### 3. ❓ Query

Triggered by asking a **question about the wiki**.

```
Human: What AI science tools are covered in the podcasts?

Claude:
1. Reads _master-index.md to find relevant topics
2. Reads topic _index.md to find specific articles
3. Reads 1-3 full articles
4. Synthesizes answer with [[wikilinks]] and source citations
5. Saves result to output/query-YYYY-MM-DD-topic.md
```

**Every query is saved, building searchable Q&A history**

### 4. 🔬 Lint (`"lint"` or `"audit"`)

Triggered by saying **"lint"** or **"audit the wiki"**.

Produces a report covering:
- Contradictions between articles
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Missing concepts mentioned but not documented
- Suggested new articles

**Output: `output/lint-report-YYYY-MM-DD.md`**

---

## 📊 Current Stats

| Metric | Count |
|--------|-------|
| Source podcasts | 54 |
| Wiki articles | 222+ |
| Topic categories | 12 |
| Guest profiles | 28 |
| Research sources | 7 |

### Topic Categories

- `ai-agents/` - Autonomous agents, tool use, reasoning
- `ai-architecture/` - Model architectures, transformers, scaling
- `ai-business/` - AI startups, enterprise adoption
- `ai-careers/` - Career advice, skills, job market
- `ai-ethics-society/` - Safety, alignment, societal impact
- `ai-industry/` - Industry applications, case studies
- `ai-products-tools/` - Developer tools, MLOps, platforms
- `ai-science/` - Research tools, notebooks, data science
- `agi-future/` - AGI timelines, future predictions
- `icymi-roundups/` - Weekly AI news roundups
- `llms/` - Large language models, prompting, fine-tuning
- `token-optimization/` - Token costs, prompt compression, caching

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- [Claude](https://claude.ai) (via Cursor, VS Code + Copilot, or API)

### Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/singhak-abbvie/claude-as-librarian-llm-wiki.git
   cd claude-as-librarian-llm-wiki
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install pypdf
   ```

4. **Open in your IDE with Claude**
   - Use Cursor, VS Code with GitHub Copilot, or any Claude-integrated editor
   - Make sure Claude can read `CLAUDE.md` at session start

### Usage

1. **Add source material** → Drop PDFs, articles, or notes into `raw/`

2. **Compile** → Tell Claude: `"compile"`

3. **Query** → Ask questions: `"What do the podcasts say about AI agents?"`

4. **Research** → Request new research: `"research latest developments in MoE architectures"`

5. **Audit** → Check wiki health: `"lint"`

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Vault schema - the "constitution" Claude follows |
| `wiki/_master-index.md` | Entry point to all topics |
| `wiki/log.md` | Append-only log of all operations |
| `extract_and_compile.py` | Python script for bulk PDF processing |

---

## 🎯 Design Principles

1. **Append-only logging** — Every operation is logged, creating an audit trail
2. **Source separation** — Human sources (`raw/`) vs AI sources (`ai-research/`)
3. **Immutable sources** — Raw files and research files are never modified
4. **Index-driven retrieval** — Queries use indexes, not brute-force search
5. **Schema co-evolution** — `CLAUDE.md` evolves with the human over time
6. **Wikilinks everywhere** — `[[topic/article]]` syntax for Obsidian compatibility

---

## 🙏 Credits

- **Concept inspiration**: [Andrej Karpathy](https://karpathy.ai) — The LLM-wiki idea from his blog posts and talks
- **Source material**: [Super Data Science Podcast](https://www.superdatascience.com/podcast) — 54 AI-focused episodes
- **Built with**: [Claude](https://anthropic.com) by Anthropic

---

## 📜 License

MIT License — Feel free to fork and build your own LLM-wiki!

---

<p align="center">
  <i>"The best note-taking system is one that organizes itself."</i>
</p>
