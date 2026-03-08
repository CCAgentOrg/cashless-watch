---
title: "Agent: Weekly Fintech Deep Research"
date: 2026-03-08T14:50:00+05:30
draft: false
tags: ["Agents", "AI", "Fintech", "Weekly", "Deep Research"]
categories: ["Meta"]
description: "Full agent instruction for the Weekly Fintech Deep Research — Sunday 9 AM, 2000-word analysis"
---

# 🤖 Agent: Weekly Fintech Deep Research

## Overview

| Property | Value |
|----------|-------|
| **Name** | Weekly Fintech Deep Research |
| **Blog** | Cashless Watch |
| **Schedule** | Sunday @ 9:00 AM IST |
| **Coverage** | Past week (Sunday to Saturday) |
| **Word Count** | 2000 words |
| **Model** | minimax-m2.5 |
| **Agent ID** | `cf12ab89-1234-5678-9abc-def012345678` |

## Mission

Publish a 2000-word deep dive analysis on the most significant fintech topic of the past week. This is a premium, analytical piece that goes beyond daily briefs — combining data, expert views, and consumer impact analysis.

## Agent Instruction

### Task (Sunday @ 9:00 AM IST)
1. Review all content from the past week's daily fintech briefs and themed deep dives
2. Identify the single most impactful topic based on:
   - Regulatory changes (RBI, SEBI, IRDAI)
   - Funding amount or market valuation
   - Consumer relevance
   - Industry disruption
3. Research comprehensively: 10+ sources including primary documents, analyst views, and data
4. Write a 2000-word analytical piece
5. Generate Hugo markdown with proper frontmatter
6. Publish to `content/posts/YYYY-MM-DD-fintech-weekly-deep-dive.md`
7. Push to GitHub

### Output Structure
- Executive Summary (2-3 paragraphs)
- The Story in Depth (1500+ words)
- Data & Metrics
- Expert Views
- Consumer Impact
- Looking Ahead
- Sources

### Publishing Commands
```bash
cd /home/.z/workspaces/cashless-watch
git checkout main
git pull origin main
DATE=$(date +%Y-%m-%d)
TOPIC="[determined topic]"
cat > content/posts/${DATE}-fintech-weekly-deep-dive.md << 'EOF'
[generated content]
EOF
git add content/posts/${DATE}-fintech-weekly-deep-dive.md
git commit -m "Add Fintech Weekly Deep Dive: ${TOPIC}"
git push origin main
```

### Quality Standards
- Minimum 2000 words
- At least 10 primary sources
- Include data, quotes, and analysis
- Actionable insights for consumers and industry
- Publish by 9:30 AM IST latest

---

## How to Improve This Agent

### Suggest Changes
1. **Open an Issue**: [github.com/CCAgentOrg/cashless-watch/issues](https://github.com/CCAgentOrg/cashless-watch/issues)
2. **Submit a PR**: Edit `content/agents/weekly-deep-research-agent.md`

---

*This agent is part of Cashless Watch. All agent instructions are open source under CC BY-SA 4.0.*
