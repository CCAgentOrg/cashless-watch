#!/usr/bin/env python3
"""
Send CashlessWatch Stock Market Summary to Telegram
"""

import json
import sys
import os
import requests

def format_price(price):
    """Format price with Indian notation"""
    if price >= 1000:
        return f"₹{price:,.2f}"
    return f"₹{price:.2f}"

def get_emoji(change_pct):
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

def generate_telegram_message(data):
    """Generate formatted Telegram message"""
    from datetime import datetime
    
    date_str = datetime.now().strftime('%B %d, %Y')
    time_str = datetime.now().strftime('%I:%M %p IST')
    
    lines = [
        f"📊 *CashlessWatch Stock Market Summary*",
        f"*{date_str} | {time_str}*",
        "",
        "━" * 20,
        "*📊 INDICES*",
        "━" * 20,
    ]
    
    # Indices
    indices = data.get('indices', {})
    index_map = {
        'NIFTY_50': 'Nifty 50',
        'NIFTY_BANK': 'Nifty Bank',
        'FINNIFTY': 'FinNifty',
        'NIFTY_IT': 'Nifty IT'
    }
    
    for key, label in index_map.items():
        if key in indices and 'error' not in indices[key]:
            idx = indices[key]
            price = idx.get('price', 0)
            change_pct = idx.get('change_pct', 0)
            emoji = get_emoji(change_pct)
            lines.append(f"`{label:<12} {price:>10,.2f}  {emoji} {change_pct:+.2f}%`")
    
    # Banks
    lines.extend([
        "",
        "━" * 20,
        "*🏦 BANKS — Digital Payments*",
        "━" * 20,
    ])
    
    banks = data.get('banks', {})
    bank_order = ['HDFCBANK', 'ICICIBANK', 'SBIN', 'AXISBANK', 'KOTAKBANK']
    
    for key in bank_order:
        if key in banks and 'error' not in banks[key]:
            bank = banks[key]
            name = bank.get('name', key)
            price = bank.get('price', 0)
            change_pct = bank.get('change_pct', 0)
            emoji = get_emoji(change_pct)
            
            # Truncate long names
            display_name = name[:15] if len(name) > 15 else name
            lines.append(f"`{display_name:<15} {format_price(price):>10}  {emoji}`")
    
    # Fintech summary
    lines.extend([
        "",
        "━" * 20,
        "*💳 FINTECH — Pure Play*",
        "━" * 20,
    ])
    
    fintech = data.get('fintech', {})
    valid_fintech = [v for v in fintech.values() if 'error' not in v]
    
    if valid_fintech:
        # Show top 3 movers
        top_movers = sorted(valid_fintech, key=lambda x: abs(x.get('change_pct', 0)), reverse=True)[:3]
        for stock in top_movers:
            name = stock.get('name', '')[:12]
            price = stock.get('price', 0)
            change_pct = stock.get('change_pct', 0)
            emoji = get_emoji(change_pct)
            lines.append(f"`{name:<12} {format_price(price):>10}  {emoji} {change_pct:+.2f}%`")
    else:
        lines.append("`⏳ Small-cap data delayed`")
        lines.append("`   Check live terminals`")
    
    # Footer
    lines.extend([
        "",
        "━" * 20,
        "⚠️ *Not investment advice*",
        f"📎 Full report: https://github.com/CCAgentOrg/cashless-watch",
    ])
    
    return "\n".join(lines)

def send_telegram(message):
    """Send message via Telegram"""
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    if not bot_token or not chat_id:
        print("Telegram credentials not configured", file=sys.stderr)
        return False
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown',
        'disable_web_page_preview': True
    }
    
    try:
        resp = requests.post(url, json=payload, timeout=30)
        return resp.status_code == 200
    except Exception as e:
        print(f"Telegram error: {e}", file=sys.stderr)
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: send-telegram-alert.py <input_json>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    message = generate_telegram_message(data)
    
    # For testing, print to stdout
    if os.environ.get('TELEGRAM_BOT_TOKEN'):
        success = send_telegram(message)
        if success:
            print("Telegram alert sent successfully")
        else:
            print("Failed to send Telegram alert", file=sys.stderr)
            sys.exit(1)
    else:
        print("TELEGRAM_BOT_TOKEN not set, printing message:")
        print("=" * 50)
        print(message)
        print("=" * 50)

if __name__ == "__main__":
    main()
