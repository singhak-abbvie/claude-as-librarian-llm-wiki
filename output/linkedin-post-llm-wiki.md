# LinkedIn Post: Claude as Librarian

---

🏛️ **What if your notes organized themselves?**

Andrej Karpathy recently shared a brilliant pattern called **LLM-Wiki** — instead of using RAG to re-discover knowledge from scratch on every query, you let an LLM build and maintain a **persistent, compounding wiki** that sits between you and your raw sources.

> *"The knowledge is compiled once and then kept current, not re-derived on every query... The wiki keeps getting richer with every source you add and every question you ask."*
> — Karpathy's LLM-Wiki Gist

I took this concept and built it out with Claude as my librarian.

**The problem:** We all have messy folders of PDFs, articles, and notes that never get organized. Cross-references? Forget about it.

**The solution:** Drop files into an inbox. Say "compile." Claude reads everything, creates wiki articles, adds cross-links, and maintains a searchable index.

Here's what it did with 54 podcast transcripts:
→ 222 wiki articles  
→ 12 topic categories  
→ 28 guest profiles  
→ Automatic cross-linking between related concepts

The magic is in `CLAUDE.md` — a "vault schema" that defines exactly how Claude should behave as librarian. Think of it as a constitution for your knowledge base.

**4 operations:**
📥 **Compile** — Ingest new sources into the wiki  
🔍 **Research** — Claude finds & saves web sources  
❓ **Query** — Ask questions, get cited answers  
🔬 **Lint** — Audit for contradictions & gaps

🔗 **Karpathy's original concept:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

🔗 **My implementation:** https://github.com/singhak-abbvie/claude-as-librarian-llm-wiki

The best note-taking system is one that organizes itself.

---

#AI #LLM #KnowledgeManagement #Productivity #Claude #Anthropic #PKM #SecondBrain

---

**Copy-paste version (under 3000 chars):**

🏛️ What if your notes organized themselves?

Andrej Karpathy recently shared a brilliant pattern called LLM-Wiki — instead of RAG re-discovering knowledge on every query, let an LLM build a persistent, compounding wiki between you and your sources.

"The knowledge is compiled once and kept current, not re-derived on every query."

I built this with Claude as my librarian.

Drop files into an inbox. Say "compile." Claude reads everything, creates wiki articles, adds cross-links, and maintains a searchable index.

From 54 podcast transcripts → 222 wiki articles, 12 topics, 28 guest profiles. All automatically cross-linked.

The magic is in CLAUDE.md — a "vault schema" defining how Claude behaves as librarian.

4 operations:
📥 Compile — Ingest sources into wiki
🔍 Research — Claude finds web sources
❓ Query — Ask questions, get cited answers
🔬 Lint — Audit for contradictions

🔗 Karpathy's concept: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

🔗 My repo: https://github.com/singhak-abbvie/claude-as-librarian-llm-wiki

#AI #LLM #KnowledgeManagement #Productivity #Claude
