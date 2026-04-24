"""
YouTube Topic Research Agent — UAE Crypto
------------------------------------------
Uses Claude to analyse YouTube trends, top channels, content gaps, and
generate concrete video ideas for the UAE crypto niche.

Part of the same AI content operations pipeline as research_agent.py.

Requirements:
    pip install anthropic

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    python youtube_research_agent.py
"""

import os
import datetime
import anthropic

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "./output/youtube")
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-7")

YOUTUBE_RESEARCH_PROMPT = """
You are a YouTube content strategist specializing in UAE crypto content.

Research and analyze the following for YouTube:

1. TOP PERFORMING VIDEO TOPICS
   - What UAE crypto topics get the most views?
   - What titles/thumbnails work best?
   - Ideal video length for this niche?

2. CONTENT GAPS
   - What topics are being searched but have low quality/few videos?
   - Where can a new creator dominate?

3. TOP CHANNELS TO STUDY
   - Who are the top UAE or Arabic crypto YouTubers?
   - What makes their content work?

4. VIDEO IDEAS (give 10 specific titles)
   - Based on pain points: banking, VARA, scams, tax, real estate
   - Format: Hook title + thumbnail idea + 3 key talking points

5. MONETIZATION ON YOUTUBE
   - CPM estimates for UAE crypto content
   - Sponsorship opportunities
   - How to grow to monetization threshold fast in this niche

Output as a structured markdown report.
"""


def run_youtube_research():
    client = anthropic.Anthropic()

    print(f"[{datetime.datetime.now()}] Running YouTube Research Agent ({MODEL})...")

    message = client.messages.create(
        model=MODEL,
        max_tokens=2500,
        messages=[{"role": "user", "content": YOUTUBE_RESEARCH_PROMPT}],
    )

    today = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = os.path.join(OUTPUT_DIR, f"youtube_research_{today}.md")

    with open(filename, "w") as f:
        f.write(f"# YouTube Research — UAE Crypto — {today}\n\n")
        f.write(message.content[0].text)

    print(f"YouTube research saved to: {filename}")
    return filename


if __name__ == "__main__":
    run_youtube_research()
