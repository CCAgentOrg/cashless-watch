#!/usr/bin/env python3
"""
CashlessWatch Stock Data Fetcher
Fetches market data from oracle sources for the Stock Market Summary agent.
"""

import json
import sys
import os
from datetime import datetime
import requests

# Oracle Sources Configuration
ORACLE_SOURCES = {
    "nse_official": {
        "name": "NSE India Official",
        "base_url": "https://www.nseindia.com/api",
        "reliability": "tier_1",
        "priority": 1
    },
    "moneycontrol": {
        "name": "Moneycontrol", 
        "base_url": "https://www.moneycontrol.com",
        "reliability": "tier_2",
        "priority": 2
    },
    "yahoo_finance": {
        "name": "Yahoo Finance",
        "base_url": "https://query1.finance.yahoo.com/v8/finance",
        "reliability": "tier_2", 
        "priority": 3
    }
}

# Stock Universe
STOCKS = {
    "indices": {
        "NIFTY_50": {"symbol": "^NSEI", "nse_symbol": "NIFTY 50", "yf": "^NSEI"},
        "NIFTY_BANK": {"symbol": "^NSEBANK", "nse_symbol": "NIFTY BANK", "yf": "^NSEBANK"},
        "FINNIFTY": {"symbol": "^NSEFIN", "nse_symbol": "NIFTY FIN SERVICE", "yf": "^NSEFIN"},
        "NIFTY_IT": {"symbol": "^NSEIT", "nse_symbol": "NIFTY IT", "yf": "^NSEIT"}
    },
    "banks": {
        "HDFCBANK": {"nse": "HDFCBANK", "yf": "HDFCBANK.NS", "name": "HDFC Bank"},
        "ICICIBANK": {"nse": "ICICIBANK", "yf": "ICICIBANK.NS", "name": "ICICI Bank"},
        "SBIN": {"nse": "SBIN", "yf": "SBIN.NS", "name": "State Bank of India"},
        "AXISBANK": {"nse": "AXISBANK", "yf": "AXISBANK.NS", "name": "Axis Bank"},
        "KOTAKBANK": {"nse": "KOTAKBANK", "yf": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank"}
    },
    "fintech": {
        "PAYTM": {"nse": "PAYTM", "yf": "PAYTM.NS", "name": "One97 Communications (Paytm)", "tier": "B1"},
        "PBFINTECH": {"nse": "PBFINTECH", "yf": "PBFINTECH.NS", "name": "PB Fintech (PolicyBazaar)", "tier": "B2"},
        "INFIBEAM": {"nse": "INFIBEAM", "yf": "INFIBEAM.NS", "name": "Infibeam Avenues", "tier": "B3"},
        "FINOPB": {"nse": "FINOPB", "yf": "FINOPB.NS", "name": "Fino Payments Bank", "tier": "B4"},
        "SBICARD": {"nse": "SBICARD", "yf": "SBICARD.NS", "name": "SBI Cards", "tier": "B4"},
        "AGSTRA": {"nse": "AGSTRA", "yf": "AGSTRA.NS", "name": "AGS Transact", "tier": "B5", "note": "Under CIRP"}
    }
}

def fetch_yahoo_finance(symbols):
    """Fetch data from Yahoo Finance"""
    results = {}
    for key, config in symbols.items():
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{config['yf']}?interval=1d&range=5d"
            resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if data.get('chart') and data['chart'].get('result'):
                    result = data['chart']['result'][0]
                    meta = result['meta']
                    timestamps = result.get('timestamp', [])
                    closes = result['indicators']['quote'][0].get('close', [])
                    
                    if closes and len(closes) >= 2:
                        current = closes[-1]
                        previous = closes[-2] if len(closes) > 1 else meta.get('previousClose', current)
                        change = current - previous
                        change_pct = (change / previous * 100) if previous else 0
                        
                        results[key] = {
                            'source': 'yahoo_finance',
                            'price': round(current, 2),
                            'previous': round(previous, 2),
                            'change': round(change, 2),
                            'change_pct': round(change_pct, 2),
                            'name': config.get('name', key),
                            'tier': config.get('tier', '')
                        }
        except Exception as e:
            results[key] = {'error': str(e), 'name': config.get('name', key)}
    return results

def fetch_nse_indices():
    """Fetch NSE indices data"""
    results = {}
    try:
        # NSE All Indices API
        url = "https://www.nseindia.com/api/allIndices"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        }
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            for item in data.get('data', []):
                index_name = item.get('index', '')
                if index_name in ['NIFTY 50', 'NIFTY BANK', 'NIFTY FINANCIAL SERVICES', 'NIFTY IT']:
                    key = index_name.replace(' ', '_').replace('NIFTY_', 'NIFTY_')
                    results[key] = {
                        'source': 'nse_official',
                        'price': item.get('last', 0),
                        'change': item.get('change', 0),
                        'change_pct': item.get('percChange', 0),
                        'name': index_name
                    }
    except Exception as e:
        results['error'] = str(e)
    return results

def generate_market_summary(data):
    """Generate formatted market summary"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    summary = {
        'timestamp': timestamp,
        'indices': data.get('indices', {}),
        'banks': data.get('banks', {}),
        'fintech': data.get('fintech', {}),
        'meta': {
            'data_sources_used': list(set([v.get('source', 'unknown') for v in {**data.get('indices', {}), **data.get('banks', {}), **data.get('fintech', {})}.values() if 'error' not in v])),
            'stocks_with_data': len([v for v in {**data.get('banks', {}), **data.get('fintech', {})}.values() if 'error' not in v]),
            'stocks_with_errors': len([v for v in {**data.get('banks', {}), **data.get('fintech', {})}.values() if 'error' in v])
        }
    }
    
    return summary

def main():
    """Main execution"""
    print("🔍 CashlessWatch Stock Data Fetcher", file=sys.stderr)
    print("=" * 50, file=sys.stderr)
    
    # Fetch all data
    data = {
        'indices': fetch_nse_indices(),
        'banks': fetch_yahoo_finance(STOCKS['banks']),
        'fintech': fetch_yahoo_finance(STOCKS['fintech'])
    }
    
    # Generate summary
    summary = generate_market_summary(data)
    
    # Output JSON
    print(json.dumps(summary, indent=2))
    
    # Stats to stderr
    print(f"\n✅ Indices: {len(summary['indices'])} fetched", file=sys.stderr)
    print(f"✅ Banks: {len([v for v in summary['banks'].values() if 'error' not in v])} fetched", file=sys.stderr)
    print(f"✅ Fintech: {len([v for v in summary['fintech'].values() if 'error' not in v])} fetched", file=sys.stderr)

if __name__ == "__main__":
    main()
