#!/usr/bin/env python3
"""
Generate Hugo markdown post from stock data JSON
"""

import json
import sys
from datetime import datetime

def get_market_emoji(change_pct):
    if change_pct > 2:
        return "🚀"
    elif change_pct > 1:
        return "🟢"
    elif change_pct > 0:
        return "📈"
    elif change_pct > -1:
        return "📉"
    else:
        return "🔴"

def format_table_row(name, price, change, change_pct):
    emoji = get_market_emoji(change_pct)
    return f"| {name} | {price:,.2f} | {change:+,.2f} | {change_pct:+.2f}% |"

def generate_frontmatter(data):
    date_str = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+05:30')
    return f"""---
title: "CashlessWatch Stock Market Summary — {datetime.now().strftime('%B %d, %Y')}"
date: {date_str}
draft: false
tags: ["Stocks", "Fintech", "Markets", "India", "Daily"]
categories: ["Stock Watch"]
description: "Pre-market summary of Indian indices, banking stocks, and pure-play fintech/paytech companies"
---

# CashlessWatch Stock Market Summary — {datetime.now().strftime('%B %d, %Y')}

**Summary as of {datetime.now().strftime('%I:%M %p IST, %B %d, %Y')}**

---
"""

def generate_indices_section(indices):
    output = ["## 📊 INDICES", ""]
    output.append("| Index | Level | Change | % Change |")
    output.append("|-------|-------|--------|----------|")
    
    index_map = {
        'NIFTY_50': 'Nifty 50',
        'NIFTY_BANK': 'Nifty Bank',
        'FINNIFTY': 'FinNifty',
        'NIFTY_IT': 'Nifty IT'
    }
    
    for key, label in index_map.items():
        if key in indices and 'error' not in indices[key]:
            idx = indices[key]
            output.append(format_table_row(
                label,
                idx.get('price', 0),
                idx.get('change', 0),
                idx.get('change_pct', 0)
            ))
    
    output.append("")
    
    # Market sentiment
    nifty_change = indices.get('NIFTY_50', {}).get('change_pct', 0)
    if nifty_change > 1:
        sentiment = "🟢 **Strong positive opening expected.**"
    elif nifty_change > 0:
        sentiment = "📈 **Positive sentiment.**"
    elif nifty_change > -1:
        sentiment = "📉 **Weak opening expected.**"
    else:
        sentiment = "🔴 **Negative sentiment.**"
    
    output.append(f"**Market Direction:** {sentiment}")
    output.append("")
    
    return "\n".join(output)

def generate_banks_section(banks):
    output = ["## 🏦 BANKS — Digital Payments Leaders", ""]
    output.append("| Company | Symbol | Price | Change | % Change |")
    output.append("|---------|--------|-------|--------|----------|")
    
    bank_order = ['HDFCBANK', 'ICICIBANK', 'SBIN', 'AXISBANK', 'KOTAKBANK']
    
    valid_banks = []
    for key in bank_order:
        if key in banks and 'error' not in banks[key]:
            bank = banks[key]
            output.append(format_table_row(
                bank.get('name', key),
                bank.get('price', 0),
                bank.get('change', 0),
                bank.get('change_pct', 0)
            ))
            valid_banks.append(bank)
    
    output.append("")
    
    # Banking sector summary
    if valid_banks:
        avg_change = sum(b.get('change_pct', 0) for b in valid_banks) / len(valid_banks)
        leader = max(valid_banks, key=lambda x: x.get('change_pct', 0))
        
        if avg_change > 1:
            sentiment = "🟢 **Strong rally across banking sector.**"
        elif avg_change > 0:
            sentiment = "📈 **Positive momentum in banks.**"
        else:
            sentiment = "📉 **Weakness in banking stocks.**"
        
        output.append(f"**Banking Sector:** {sentiment} {leader.get('name')} leading with {leader.get('change_pct', 0):+.2f}%.")
    else:
        output.append("⚠️ **Data unavailable for banking stocks.**")
    
    output.append("")
    
    return "\n".join(output)

def generate_fintech_section(fintech):
    output = ["## 💳 PURE-PLAY FINTECH/PAYTECH", ""]
    
    # Group by tier
    tiers = {'B1': [], 'B2': [], 'B3': [], 'B4': [], 'B5': []}
    tier_names = {
        'B1': 'Digital Payments & Wallets',
        'B2': 'Insurance & Credit Marketplaces',
        'B3': 'Payment Infrastructure & Gateways',
        'B4': 'Payments Banking & Cards',
        'B5': 'ATM & Cash Management'
    }
    
    for key, stock in fintech.items():
        if 'error' not in stock:
            tier = stock.get('tier', 'B3')
            tiers[tier].append(stock)
    
    for tier, stocks in tiers.items():
        if stocks:
            output.append(f"### Tier {tier}: {tier_names[tier]}")
            output.append("")
            output.append("| Company | Symbol | Price | Change | % Change |")
            output.append("|---------|--------|-------|--------|----------|")
            
            for stock in sorted(stocks, key=lambda x: x.get('name', '')):
                note = stock.get('note', '')
                name = stock.get('name', '')
                if note:
                    name += f" ({note})"
                
                output.append(format_table_row(
                    name,
                    stock.get('price', 0),
                    stock.get('change', 0),
                    stock.get('change_pct', 0)
                ))
            
            output.append("")
    
    return "\n".join(output)

def generate_footer():
    return """---

## 📰 Sector News

- **Market Movers:** Check live terminals for breaking news
- **RBI/NPCI:** Monitor for policy announcements
- **Earnings:** Watch for quarterly results from major banks

---

## ⚠️ DISCLAIMER

**Not investment advice.** This summary is for informational purposes only. Data sourced from NSE India, Yahoo Finance, and Moneycontrol. Verify prices from official sources before trading.

---

*Data sources: NSE India (nseindia.com), Yahoo Finance, Moneycontrol*
*Generated by CashlessWatch Stock Market Summary Agent*
"""

def main():
    if len(sys.argv) < 3:
        print("Usage: generate-hugo-post.py <input_json> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Generate content
    content = []
    content.append(generate_frontmatter(data))
    content.append(generate_indices_section(data.get('indices', {})))
    content.append("---")
    content.append("")
    content.append(generate_banks_section(data.get('banks', {})))
    content.append("---")
    content.append("")
    content.append(generate_fintech_section(data.get('fintech', {})))
    content.append(generate_footer())
    
    # Write output
    with open(output_file, 'w') as f:
        f.write("\n".join(content))
    
    print(f"Generated: {output_file}")

if __name__ == "__main__":
    main()
