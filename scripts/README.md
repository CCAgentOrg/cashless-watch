# CashlessWatch Scripts

Helper scripts for the CashlessWatch Stock Market Summary agent.

## 📁 Script Inventory

| Script | Purpose | Language |
|--------|---------|----------|
| `fetch-stock-data.py` | Fetch market data from oracle sources | Python 3 |
| `generate-hugo-post.py` | Generate Hugo markdown from stock data | Python 3 |
| `send-telegram-alert.py` | Send Telegram alert with summary | Python 3 |
| `stock-watch.sh` | Main runner script (pipeline orchestrator) | Bash |

---

## 🚀 Quick Start

### Full Pipeline (Default)
```bash
cd /home/.z/workspaces/con_PXCpywVCLwND9RsD/cashless-watch
./scripts/stock-watch.sh
```

Runs the complete pipeline:
1. Fetch data from oracle sources
2. Generate Hugo post
3. Send Telegram alert
4. Sync to GitHub

### Individual Steps
```bash
# Fetch data only
./scripts/stock-watch.sh fetch

# Generate Hugo post from existing data
./scripts/stock-watch.sh hugo

# Send Telegram alert only
./scripts/stock-watch.sh telegram

# Output JSON for inspection
./scripts/stock-watch.sh json
```

---

## 📊 Oracle Data Sources

### Tier 1 (Primary)
| Source | Data | Endpoint | Fallback |
|--------|------|----------|----------|
| NSE India | Indices | `nseindia.com/api/allIndices` | Yahoo Finance |
| NSE India | Stock quotes | `nseindia.com/api/equity-stockIndices` | Yahoo Finance |

### Tier 2 (Secondary)
| Source | Data | Endpoint | Notes |
|--------|------|----------|-------|
| Yahoo Finance | Global stocks | `query1.finance.yahoo.com/v8/finance` | Reliable, no auth |
| Moneycontrol | Indian markets | `moneycontrol.com` | HTML scraping |

### Tier 3 (Fallback)
| Source | Data | Notes |
|--------|------|-------|
| BSE India | Indices | If NSE fails |
| Google Finance | Quick quotes | Unofficial API |

---

## 🏦 Stock Universe

### Indices
- Nifty 50 (NSEI)
- Nifty Bank (NSEBANK)
- Nifty Financial Services (NSEFIN)
- Nifty IT (NSEIT)

### Banks (Digital Payments Leaders)
| Symbol | Company | Digital Edge |
|--------|---------|--------------|
| HDFCBANK | HDFC Bank | 22% credit card share, ML fraud |
| ICICIBANK | ICICI Bank | iMobile Pay, Apple Pay |
| SBIN | State Bank of India | Largest UPI volume, Yono |
| AXISBANK | Axis Bank | Digital focus, credit cards |
| KOTAKBANK | Kotak Mahindra Bank | 811 digital bank |

### Fintech (Tier-Based)
| Tier | Symbol | Company | Focus |
|------|--------|---------|-------|
| B1 | PAYTM | One97 Communications | Digital payments, UPI |
| B1 | MOBIKWIK | MobiKwik | Mobile wallet |
| B2 | PBFINTECH | PB Fintech | Insurance marketplace |
| B3 | INFIBEAM | Infibeam Avenues | Payment gateway |
| B3 | PINELABS | Pine Labs | Merchant payments |
| B3 | NPST | NPST | UPI infrastructure |
| B4 | FINOPB | Fino Payments Bank | Payments bank |
| B4 | SBICARD | SBI Cards | Credit cards |
| B5 | AGSTRA | AGS Transact | ATM/cash (⚠️ CIRP) |

---

## 🔧 Configuration

### Environment Variables
```bash
# Telegram (for alerts)
export TELEGRAM_BOT_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"

# Git (auto-configured from repo)
export GITHUB_TOKEN="ghp_xxx"  # For pushes (optional)
```

### Data Output Format
```json
{
  "timestamp": "2026-03-11 08:15:00",
  "indices": {
    "NIFTY_50": {
      "source": "nse_official",
      "price": 24261.60,
      "change": 233.55,
      "change_pct": 0.97,
      "name": "Nifty 50"
    }
  },
  "banks": {
    "HDFCBANK": {
      "source": "yahoo_finance",
      "price": 849.45,
      "change": 8.75,
      "change_pct": 1.04,
      "name": "HDFC Bank"
    }
  },
  "fintech": {
    "PAYTM": {
      "source": "yahoo_finance",
      "price": 780.00,
      "change": 15.00,
      "change_pct": 1.96,
      "name": "One97 Communications (Paytm)",
      "tier": "B1"
    }
  },
  "meta": {
    "data_sources_used": ["nse_official", "yahoo_finance"],
    "stocks_with_data": 12,
    "stocks_with_errors": 2
  }
}
```

---

## 📅 Agent Integration

The Stock Market Summary agent runs via:

```bash
# Scheduled execution (via Zo Agent)
RRULE: FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=8;BYMINUTE=15

# Manual execution
./scripts/stock-watch.sh
```

### Agent Instruction (Source of Truth)
See: `content/agents/stock-market-summary-agent.md`

---

## 🛠️ Troubleshooting

### Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| "NSE API blocked" | Rate limiting | Use Yahoo Finance fallback |
| "Data delayed" | Market closed | Wait for pre-market data |
| "Telegram failed" | Missing env vars | Set TELEGRAM_BOT_TOKEN |
| "Git push failed" | Auth issue | Check git remote/credentials |

### Debug Mode
```bash
# Verbose output
DEBUG=1 ./scripts/stock-watch.sh fetch

# Check data
./scripts/stock-watch.sh json | python3 -m json.tool
```

---

## 📝 Changelog

| Date | Change | Commit |
|------|--------|--------|
| 2026-03-11 | Initial scripts created | [TBD] |

---

*Part of the CashlessWatch Stock Market Summary system.*
