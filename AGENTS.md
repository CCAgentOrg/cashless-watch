# 🤖 AI Agents — Cashless Watch

This document tracks the AI agents that power the Cashless Watch blog.

## Active Agents

### 1. Daily Fintech Brief
| Property | Value |
|----------|-------|
| **Agent ID** | `651b5ce7-9157-442e-99ab-9539d23df862` |
| **Schedule** | Daily @ 8:00 AM IST |
| **Model** | minimax-m2.5 |
| **Source** | `content/agents/daily-fintech-brief-agent.md` |

**Mission**: Publish a concise daily fintech news brief covering RBI regulations, SEBI circulars, UPI updates, and banking news.

**Oracle Sources**: rbi.org.in, sebi.gov.in, npci.org.in, inc42.com, theken.in

### 2. Fintech Deep Dive
| Property | Value |
|----------|-------|
| **Agent ID** | `0862617d-c763-4a0c-8340-b4647dbf30f7` |
| **Schedule** | Daily @ 8:30 AM IST |
| **Model** | minimax-m2.5 |
| **Source** | `content/agents/fintech-deep-dive-agent.md` |

**Mission**: Publish themed deep dive analysis on fintech topics with weekly rotation.

**Daily Themes**:
- Monday: Payments & UPI
- Tuesday: Lending & Credit
- Wednesday: Insurance & Wealth
- Thursday: Regulatory Analysis
- Friday: Startup & Funding
- Saturday: Consumer Rights & Complaints

## How to Modify

1. **Edit agent instruction**: Modify `content/agents/<agent-name>-agent.md`
2. **Submit PR**: Changes are synced to live agents
3. **Open issue**: https://github.com/CCAgentOrg/cashless-watch/issues

## Version History

| Date | Change | Author |
|------|--------|--------|
| 2026-03-08 | Added oracle sources with consumer rights focus | @cashlessconsumer |
| 2026-03-08 | Initial agent setup | @cashlessconsumer |
