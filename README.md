# Content Research Agent

Two small Claude-powered agents that automate the top of the content operations funnel for a niche newsletter: trending-topic research and YouTube content strategy. Built to seed [The Emirates Allocator](https://pavan.blog/articles) newsletter — UAE crypto — but the pattern generalises to any niche.

## Agents

### `research_agent.py` — Trending Topics & Pain Points

Runs a structured research brief against Claude and writes a dated markdown report.

- **Top 5 trending topics** in UAE crypto
- **New pain points** surfacing for UAE residents
- **Regulatory updates** (VARA, UAE Central Bank)
- **Content recommendations** scored by search demand × monetization × content gap

### `youtube_research_agent.py` — YouTube Content Strategy

Same pattern, tuned for the YouTube surface.

- Top-performing topics and formats in UAE crypto
- Content gaps a new creator can own
- Channels to study
- 10 specific video ideas with hook title + thumbnail concept + talking points
- CPM and sponsorship monetization notes

## Run

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pip install -r requirements.txt
python research_agent.py
python youtube_research_agent.py
```

Reports land in `./output/pain-points/` and `./output/youtube/` as dated `.md` files.

## Design notes

- **Structured prompt, free-form output.** Prompts enforce a report shape; the model fills it. Cheaper and faster than chaining multiple calls, and the output is human-reviewable in seconds.
- **Env-var config.** `ANTHROPIC_API_KEY`, `OUTPUT_DIR`, `ANTHROPIC_MODEL` — no secrets in code, no hardcoded paths.
- **Dated files.** Every run is immutable — easy to diff week-on-week for trend drift.
- **Said no to.** RAG, web-scraping, embeddings, vector DBs — a single prompt + fresh model call is enough for weekly cadence content research. Save the complexity budget for downstream production.

## Why this exists

Content research is the slowest, most expensive part of running a niche newsletter when done by hand. These agents turn a Monday morning's research into a 2-minute cron job — the editorial team spends the time on judgment and voice, not link-hunting.

## License

MIT
