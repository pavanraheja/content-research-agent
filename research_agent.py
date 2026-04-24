"""
UAE Crypto Content Research Agent
----------------------------------
Uses Claude to research trending UAE crypto topics, pain points, regulatory
updates (VARA, UAE Central Bank), and rate each by search demand × monetization
× content gap.

Designed to run on a schedule (cron / launchd) as part of an AI content
operations pipeline.

Requirements:
    pip install anthropic

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    python research_agent.py
"""

import os
import datetime
import anthropic

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "./output/pain-points")
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-7")

RESEARCH_PROMPT = """
You are a UAE crypto content research analyst.

Your job:
1. Research the latest trending topics in UAE crypto space
2. Find new pain points UAE residents face with crypto
3. Identify any regulatory updates (VARA, UAE Central Bank)
4. Spot viral/trending discussions on Reddit, Twitter, LinkedIn around UAE crypto
5. Rate each topic by: Search Demand (High/Med/Low), Monetization Potential, Content Gap

Output format:
- Date: [today]
- Top 5 Trending Topics
- New Pain Points Found
- Regulatory Updates
- Content Recommendations
- Monetization Opportunities

Be concise and actionable.
"""


def run_research():
    client = anthropic.Anthropic()

    print(f"[{datetime.datetime.now()}] Running UAE Crypto Research Agent ({MODEL})...")

    message = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        messages=[{"role": "user", "content": RESEARCH_PROMPT}],
    )

    today = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = os.path.join(OUTPUT_DIR, f"research_{today}.md")

    with open(filename, "w") as f:
        f.write(f"# UAE Crypto Research — {today}\n\n")
        f.write(message.content[0].text)

    print(f"Research saved to: {filename}")
    return filename


if __name__ == "__main__":
    run_research()
