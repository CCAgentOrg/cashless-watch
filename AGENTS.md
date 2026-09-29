# 🤖 AI Agents — Cashless Watch

This document lists all AI agents powering the Cashless Watch blog.

## 🤖 Scheduled Agents (Auto-run on schedule)

These agents run automatically on a schedule to generate content.

| Agent | Schedule | Type | Status |
|-------|----------|------|--------|
| Daily Fintech Brief | Daily 8:00 AM | Brief | ✅ Active |
| Themed Deep Dive | Daily 8:30 AM | Deep Dive | ✅ Active |
| Weekly Deep Research | Sundays 9:00 AM | Analysis | ✅ Active |
| Weekly Satire | Saturdays 10:00 AM | Satire | ✅ Active |

## 🎯 On-Demand Agents (Run when triggered)

These agents generate content when explicitly requested.

| Agent | Trigger | Type | Status |
|-------|---------|------|--------|
| 101 Explainer Agent | On-demand request | Explainer | ✅ Active |
| Stakeholder Agent | On-demand request | Directory | ✅ Active |

## Agent Details

### Scheduled Agents

#### 1. Daily Fintech Brief
- **ID**: `651b5ce7-9157-442e-99ab-9539d23df862`
- **Schedule**: Daily @ 8:00 AM IST
- **Coverage**: Last 24 hours

#### 2. Themed Deep Dive
- **ID**: `0862617d-c763-4a0c-8340-b4647dbf30f7`
- **Schedule**: Daily @ 8:30 AM IST
- **Coverage**: Last 7 days

#### 3. Weekly Deep Research
- **ID**: `d23b2a7f-9157-431e-9130-a9d87e6b459356`
- **Schedule**: Sundays @ 9:00 AM IST
- **Coverage**: Week's developments + historical context

#### 4. Weekly Satire
- **ID**: `f58efc84-6f9d-432e-a130-5a87c9bf4543`
- **Schedule**: Saturdays @ 10:00 AM IST

### On-Demand Agents

#### 5. 101 Explainer Agent
- **ID**: `a84b9a46-0dd3-42e7-b15a-9e80ea6eab1b`
- **Trigger**: Manual request
- **Output**: Encyclopedic guides with Consumer Rights Analysis

#### 6. Stakeholder Agent
- **ID**: `3f2e1a8c-9d4b-42f5-a8e1-7c6d5e3f2b1a`
- **Trigger**: Manual request
- **Output**: Key stakeholder directories and relationship maps

## Portable Agent Configuration

All agent configurations are stored in `agents.json` for machine-readable import:

```bash
# View all agents
cat agents.json | jq '.agents'

# Export to other systems
cat agents.json
```

## Contributing

To improve any agent:
1. Edit source files in `content/agents/`
2. Submit PR with rationale
3. Open issue to discuss changes

## Version Control

All agent instructions are stored in Git and synced to live agents.

## Homepage Override

Broadsheet front page (2026-09-29): `layouts/index.html` + `assets/css/broadsheet.css` replace the PaperMod profile-mode homepage only. Inner pages stay PaperMod. Dateline/ticker computed at build time. Revert = delete the two files. Mocks in `redesign-mocks/` (A broadsheet · B terminal · C poster).

## Toolchain (upgraded 2026-09-29)

Hugo 0.167.0 (deploy.yml pin + local deb; `locale = 'en-US'` in hugo.toml, languageCode removed). PaperMod submodule at d3768854 (2026-08-02 master; v8.0 tag is stale). Deprecation warnings from PaperMod .Language.* calls are upstream, harmless. Content note: front matter must stay strict YAML (0.167.0 rejects duplicate keys — the 0.146.5-era agents interleaved description text into front matter once; watch for it in new agent-authored posts).
