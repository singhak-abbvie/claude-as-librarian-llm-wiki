"""
Extract PDF transcripts and compile wiki structure.
"""
from pypdf import PdfReader
import os
import re
from pathlib import Path
from datetime import datetime

RAW_DIR = Path(r'd:\git_repo\Superdatascience\superdatascience_podcasts\raw\podcasts_AI')
WIKI_DIR = Path(r'd:\git_repo\Superdatascience\superdatascience_podcasts\wiki')

# Topic classification based on keywords
TOPIC_KEYWORDS = {
    'ai-agents': ['agent', 'agentic', 'multi-agent', 'enterprise data operations', 'automating'],
    'llms': ['llm', 'gpt', 'pre-training', 'post-training', 'jailbreak', 'transformer', 'nemotron', 'language model'],
    'agi-future': ['agi', 'superintelligence', 'future of ai', 'world model', 'laws of thought'],
    'ai-architecture': ['causal ai', 'data lake', 'npu', 'gpu', 'cpu', 'mixture-of-expert', 'state-space', 'performance engineering', 'post-transformer'],
    'ai-industry': ['journalism', 'legal', 'manufacturing', 'enterprise', 'physical world', 'industry'],
    'ai-careers': ['career', 'engineer', 'hired', '100x', 'coding jobs', 'future-proof', 'work'],
    'ai-ethics-society': ['global issues', 'phishing', 'misalignment', 'blackmail', 'ethics'],
    'ai-products-tools': ['notebook', 'marimo', 'code review', 'product', 'fireworks ai', 'pytorch lightning'],
    'ai-business': ['profit', 'optimization', 'bubble', 'arr', 'strategy'],
    'ai-science': ['physics', 'music', 'art', 'creative', 'neuroscience'],
    'icymi-roundups': ['in case you missed it', 'icymi']
}

TOPIC_DESCRIPTIONS = {
    'ai-agents': 'AI agent systems, agentic architectures, and autonomous AI',
    'llms': 'Large Language Models - training, deployment, safety, and capabilities',
    'agi-future': 'Artificial General Intelligence and the future of AI',
    'ai-architecture': 'Technical AI architectures and infrastructure',
    'ai-industry': 'AI applications and disruption across industries',
    'ai-careers': 'Career development in AI and workforce transformation',
    'ai-ethics-society': 'AI ethics, safety, and societal impacts',
    'ai-products-tools': 'AI-powered products, tools, and platforms',
    'ai-business': 'AI business strategy, economics, and entrepreneurship',
    'ai-science': 'AI in scientific research and creative applications',
    'icymi-roundups': 'Monthly roundup episodes highlighting key developments',
    'people': 'Experts, researchers, and leaders featured on the podcast'
}


def extract_pdf_content(pdf_path):
    """Extract full text from PDF."""
    reader = PdfReader(pdf_path)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text())
    return '\n\n'.join(pages)


def parse_transcript(content, filename):
    """Parse transcript to extract metadata and clean content."""
    # Clean whitespace for title extraction
    clean = ' '.join(content.split()[:200])
    
    # Extract episode number and title
    match = re.search(r'EPISODE\s+(\d+):\s*(.+?)\s*Show Notes', clean, re.IGNORECASE)
    if match:
        ep_num = match.group(1)
        title = match.group(2)
    else:
        ep_num = re.search(r'PT(\d+)', filename).group(1)
        title = "Unknown Title"
    
    # Extract guest name from title if present
    guest_match = re.search(r'WITH\s+(.+?)(?:\s*$|,\s*WITH)', title, re.IGNORECASE)
    guest = guest_match.group(1).strip() if guest_match else None
    
    # Clean content - remove excessive whitespace but preserve structure
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('Show Notes:'):
            cleaned_lines.append(line)
    
    cleaned_content = '\n'.join(cleaned_lines)
    
    return {
        'episode': ep_num,
        'title': title,
        'guest': guest,
        'content': cleaned_content,
        'filename': filename
    }


def classify_topics(title, content):
    """Classify episode into topics based on keywords."""
    topics = []
    text = (title + ' ' + content[:5000]).lower()
    
    for topic, keywords in TOPIC_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text:
                if topic not in topics:
                    topics.append(topic)
                break
    
    # Default to ai-industry if no topic found
    if not topics:
        topics = ['ai-industry']
    
    return topics


def generate_key_takeaways(content):
    """Extract key points from content."""
    # Look for structured sections or notable quotes
    takeaways = []
    
    # Look for time-stamped sections with interesting content
    sections = re.findall(r'\d{2}:\d{2}:\d{2}\s+(.+?)(?=\d{2}:\d{2}:\d{2}|$)', content[:8000], re.DOTALL)
    
    for section in sections[:10]:
        # Clean and truncate
        clean = ' '.join(section.split())[:200]
        if len(clean) > 50:
            takeaways.append(clean)
    
    return takeaways[:5] if takeaways else ["Detailed discussion on the topic - see full transcript"]


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text[:50]


def main():
    # Ensure wiki directory exists
    WIKI_DIR.mkdir(exist_ok=True)
    
    # Process all PDFs
    pdfs = sorted(RAW_DIR.glob('*.pdf'))
    episodes = []
    
    print(f"Processing {len(pdfs)} transcripts...")
    
    for pdf in pdfs:
        print(f"  Extracting: {pdf.name}")
        content = extract_pdf_content(pdf)
        parsed = parse_transcript(content, pdf.name)
        parsed['topics'] = classify_topics(parsed['title'], content)
        parsed['takeaways'] = generate_key_takeaways(content)
        episodes.append(parsed)
    
    # Group by topic
    by_topic = {}
    for ep in episodes:
        for topic in ep['topics']:
            if topic not in by_topic:
                by_topic[topic] = []
            by_topic[topic].append(ep)
    
    # Track people mentioned
    people = {}
    for ep in episodes:
        if ep['guest']:
            guest_slug = slugify(ep['guest'])
            if guest_slug not in people:
                people[guest_slug] = {'name': ep['guest'], 'episodes': []}
            people[guest_slug]['episodes'].append(ep)
    
    # Create topic folders and articles
    all_articles = []
    
    for topic, eps in by_topic.items():
        topic_dir = WIKI_DIR / topic
        topic_dir.mkdir(exist_ok=True)
        
        # Create topic index
        index_content = f"""# {topic.replace('-', ' ').title()}

{TOPIC_DESCRIPTIONS.get(topic, 'Articles on this topic.')}

## Articles

"""
        for ep in sorted(eps, key=lambda x: int(x['episode']), reverse=True):
            article_slug = f"sds-{ep['episode']}-{slugify(ep['title'])}"
            index_content += f"- [[{topic}/{article_slug}|SDS {ep['episode']}: {ep['title']}]]\n"
        
        (topic_dir / '_index.md').write_text(index_content, encoding='utf-8')
        
        # Create articles
        for ep in eps:
            article_slug = f"sds-{ep['episode']}-{slugify(ep['title'])}"
            
            # Build related links
            related = []
            for other_topic in ep['topics']:
                if other_topic != topic:
                    related.append(f"[[{other_topic}/_index|{other_topic.replace('-', ' ').title()}]]")
            
            # Add guest link if present
            if ep['guest']:
                guest_slug = slugify(ep['guest'])
                related.append(f"[[people/{guest_slug}|{ep['guest']}]]")
            
            # Add some related episodes from same topic
            same_topic_eps = [e for e in eps if e['episode'] != ep['episode']][:3]
            for other_ep in same_topic_eps:
                other_slug = f"sds-{other_ep['episode']}-{slugify(other_ep['title'])}"
                related.append(f"[[{topic}/{other_slug}|SDS {other_ep['episode']}]]")
            
            article_content = f"""# SDS {ep['episode']}: {ep['title']}

**Source:** raw/podcasts_AI/{ep['filename']}

{ep['title']} - An episode from the SuperDataScience Podcast exploring {'artificial intelligence and machine learning topics' if 'ai' in topic else 'data science topics'}.

## Key Takeaways

"""
            for takeaway in ep['takeaways']:
                article_content += f"- {takeaway}\n"
            
            article_content += f"""
## Related

{chr(10).join(related[:8])}
"""
            
            article_path = topic_dir / f"{article_slug}.md"
            article_path.write_text(article_content, encoding='utf-8')
            all_articles.append({
                'topic': topic,
                'slug': article_slug,
                'episode': ep['episode'],
                'title': ep['title']
            })
    
    # Create people folder
    people_dir = WIKI_DIR / 'people'
    people_dir.mkdir(exist_ok=True)
    
    people_index = """# People

Experts, researchers, and leaders featured on the SuperDataScience Podcast.

## Guests

"""
    for slug, person in sorted(people.items()):
        people_index += f"- [[people/{slug}|{person['name']}]]\n"
        
        # Create person page
        person_content = f"""# {person['name']}

Guest on the SuperDataScience Podcast.

## Episodes

"""
        for ep in person['episodes']:
            person_content += f"- [[{ep['topics'][0]}/sds-{ep['episode']}-{slugify(ep['title'])}|SDS {ep['episode']}: {ep['title']}]]\n"
        
        person_content += """
## Related

[[people/_index|All Guests]]
"""
        (people_dir / f"{slug}.md").write_text(person_content, encoding='utf-8')
    
    (people_dir / '_index.md').write_text(people_index, encoding='utf-8')
    
    # Create master index
    master_content = """# SuperDataScience Podcast Wiki

A knowledge base compiled from SuperDataScience podcast transcripts on AI and data science topics.

## Topics

"""
    for topic in sorted(by_topic.keys()):
        master_content += f"- [[{topic}/_index|{topic.replace('-', ' ').title()}]] ({len(by_topic[topic])} episodes)\n"
    
    master_content += f"""
## People

- [[people/_index|Featured Guests]] ({len(people)} guests)

## Statistics

- Total Episodes: {len(episodes)}
- Topic Categories: {len(by_topic)}
- Unique Guests: {len(people)}

---
*Last compiled: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    (WIKI_DIR / '_master-index.md').write_text(master_content, encoding='utf-8')
    
    # Create log
    log_content = f"""# Compilation Log

## [{datetime.now().strftime('%Y-%m-%d %H:%M')}] ingest | Initial compilation of {len(episodes)} podcast transcripts

"""
    for article in sorted(all_articles, key=lambda x: int(x['episode'])):
        log_content += f"## [{datetime.now().strftime('%Y-%m-%d %H:%M')}] ingest | SDS {article['episode']} | {article['topic']}/{article['slug']}.md\n"
    
    (WIKI_DIR / 'log.md').write_text(log_content, encoding='utf-8')
    
    print(f"\n✓ Created {len(all_articles)} wiki articles across {len(by_topic)} topics")
    print(f"✓ Created {len(people)} guest profiles")
    print(f"✓ Master index: wiki/_master-index.md")
    print(f"✓ Log: wiki/log.md")


if __name__ == '__main__':
    main()
