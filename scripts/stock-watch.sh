#!/bin/bash
# CashlessWatch Stock Market Summary — Runner Script
# Usage: ./scripts/stock-watch.sh [--telegram|--json|--hugo]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
POSTS_DIR="$REPO_ROOT/content/posts"
DATE=$(date +%Y-%m-%d)
DATETIME=$(date +%Y-%m-%dT%H:%M:%S%z)

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log() {
    echo -e "${GREEN}[$(date +%H:%M:%S)]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[$(date +%H:%M:%S)] WARNING:${NC} $1"
}

error() {
    echo -e "${RED}[$(date +%H:%M:%S)] ERROR:${NC} $1"
    exit 1
}

# Fetch market data
fetch_data() {
    log "Fetching market data from oracle sources..."
    python3 "$SCRIPT_DIR/fetch-stock-data.py" > /tmp/stock-data.json 2>/tmp/stock-fetch.log
    
    if [ $? -ne 0 ]; then
        error "Failed to fetch stock data. See /tmp/stock-fetch.log"
    fi
    
    log "Data fetched successfully"
}

# Generate Hugo markdown
generate_hugo_post() {
    local output_file="$POSTS_DIR/${DATE}-stock-watch.md"
    
    log "Generating Hugo post: $output_file"
    
    python3 "$SCRIPT_DIR/generate-hugo-post.py" /tmp/stock-data.json "$output_file"
    
    if [ $? -ne 0 ]; then
        error "Failed to generate Hugo post"
    fi
    
    log "Hugo post generated: $output_file"
}

# Send Telegram alert
send_telegram() {
    log "Sending Telegram alert..."
    
    python3 "$SCRIPT_DIR/send-telegram-alert.py" /tmp/stock-data.json
    
    if [ $? -ne 0 ]; then
        warn "Telegram alert failed (non-critical)"
    else
        log "Telegram alert sent"
    fi
}

# Git sync
sync_to_github() {
    log "Syncing to GitHub..."
    
    cd "$REPO_ROOT"
    
    if ! git diff --quiet HEAD -- content/posts/ 2>/dev/null; then
        git add content/posts/
        git commit -m "Add Stock Market Summary for $(date +'%B %d, %Y')" || warn "Nothing to commit"
        git push origin main || error "Git push failed"
        log "Synced to GitHub"
    else
        warn "No changes to sync"
    fi
}

# Full pipeline
run_full_pipeline() {
    log "Starting CashlessWatch Stock Market Summary pipeline"
    log "Date: $DATE"
    
    fetch_data
    generate_hugo_post
    send_telegram
    sync_to_github
    
    log "✅ Pipeline complete!"
    log "📊 Report: $POSTS_DIR/${DATE}-stock-watch.md"
}

# Main
case "${1:-full}" in
    fetch)
        fetch_data
        cat /tmp/stock-data.json
        ;;
    hugo)
        fetch_data
        generate_hugo_post
        ;;
    telegram)
        fetch_data
        send_telegram
        ;;
    json)
        fetch_data
        cat /tmp/stock-data.json | python3 -m json.tool
        ;;
    full|*)
        run_full_pipeline
        ;;
esac
