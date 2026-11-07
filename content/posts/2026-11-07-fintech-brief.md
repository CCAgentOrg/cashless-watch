---
title: "Fintech Brief — November 7, 2026"
date: 2026-11-07T08:00:00+05:30
draft: false
tags: ["Fintech", "Daily Brief", "India", "RBI", "Cybersecurity", "SEBI", "NBFC", "Funding", "AI"]
categories: ["Daily Brief"]
description: "RBI turns its AI-fraud warnings into binding API-security rules for banks, nearly 30 investors allege ₹100 crore of unauthorised US-stock trades on Stockal, MobiKwik gets its NBFC licence to lend ₹5,000 crore, and Cashfree opens its checkout to AI shopping agents."
---

# Fintech Brief — November 7, 2026

## Today's Top Stories

### RBI follows its AI-fraud warnings with binding API-security rules for banks

RBI's warnings about AI-assisted attacks on payment APIs just turned into enforceable rules. A **confidential Cyber Security and IT Risk advisory issued November 3**, after the regulator's meeting with bankers, and made public this week, requires banks that process API-based fund transfers to maintain a **full inventory of API clients** — business profile, services, integration details, transaction limits and security contacts — and to get a **CERT-In security audit before onboarding any new NBFC client**, with existing NBFC clients given until **February 3, 2027**. Business correspondents, payment aggregators, PSPs and fintech clients must be risk-assessed within three months. Every bank must enforce **per-transaction and daily cumulative limits immediately**, add intra-day velocity limits within a month, run **beneficiary whitelisting** where payouts to unregistered accounts are rejected and additions happen only through a separate MFA-protected channel, and apply **maker-checker or out-of-band confirmation** to API debits — with at least one such safeguard live for all existing integrations by **December 3, 2026**. The directive lands a week after I4C and CERT-In warned that agentic-AI tooling lets attackers drain disbursement APIs at machine speed, and alongside CERT-In's new AI Security Auditing Guidelines. [MediaNama](https://www.medianama.com/2026/11/223-rbi-bankers-ai-cyber-attacks-security-audits) · [The Head and Tale](https://theheadandtale.com/deepdives/exclusive-rbi-tightens-api-security-rules-for-banks-after-nbfc-cyberattacks-mandates-audits-beneficiary-checks/)

Consumer takeaway: expect payout delays and extra confirmation steps when fintech apps send money to a newly added bank account — that friction is the whitelisting working. If a transfer you didn't authorise hits your account, call your bank and **1930** within minutes, not hours.

### Nearly 30 investors say Stockal sold their US stocks without consent — ₹100 crore at stake

The developing Stockal saga is now formally a SEBI matter. **Moneycontrol, which broke the story on November 3, reports that nearly 30 retail investors claim over ₹100 crore in losses** after their US-stock holdings — Apple, Nvidia, Amazon, Tesla, Alphabet — were liquidated without authorisation on **October 15** through Stockal Securities, a Bengaluru-based, SEBI-registered platform for US investing. Proceeds were allegedly moved into shares of a little-known Chinese digital-insurance company that then crashed; India Today documented one investor's **₹3.19 crore** wipeout. Stockal's parent **Borderless Investing denied any breach** of its platform on November 4, pointing instead to possible credential theft via social engineering. Investors have complained to **SEBI, FINRA and the SEC**, and filed police complaints. The latest turn, reported November 6: an aggrieved investor says Stockal's CEO had personally assured him the firm was SEBI-registered. The structural issue underneath: India-facing apps like Stockal sit on top of US clearing brokers such as DriveWealth, which actually holds the shares — a custody chain most users never see. [Moneycontrol](https://www.moneycontrol.com/news/business/markets/stockal-ceo-told-me-the-firm-was-sebi-registered-says-aggrieved-investor-14071546.html) · [India Today](https://www.indiatoday.in/business/story/indian-investor-stockal-us-stocks-sold-without-consent-securities-trade-fraud-3031975-2026-11-04)

Consumer takeaway: the ₹100 crore figure is an early investor estimate and no regulator has ruled on fault yet. But know your custody chain — find out which US broker actually holds your foreign shares, turn on 2FA, and treat portfolio alerts as something you read, not archive.

### MobiKwik gets its NBFC licence — the wallet becomes a lender

One MobiKwik Systems announced on November 6 that its subsidiary **MobiKwik Financial Services has received RBI's Certificate of Registration to operate as an NBFC**, converting the in-principle approval granted in April 2026. The company plans to **disburse ₹5,000 crore of loans over three to four years** — secured and unsecured credit to consumers and MSMEs — through an **asset-light co-lending model**, with lending to start within three to six months. Until now MobiKwik lent only as a Lending Service Provider distributing other lenders' money; the licence lets it originate on its own book. The push comes with lending already recovering: Q2FY27 disbursements were **₹1,083 crore, up 34% year-on-year**, and the company posted its highest quarterly profit of ₹11.8 crore across its 196-million-user network. [Economic Times](https://m.economictimes.com/tech/funding/mobikwik-gets-rbi-nod-for-nbfc-arm-plans-to-launch-in-3-6-months/articleshow/135604374.cms) · [CNBC-TV18](https://www.cnbctv18.com/market/mobikwik-gets-rbi-licence-to-operate-as-nbfc-targets-rs5000-crore-in-loans-20028986.htm)

Consumer takeaway: when your wallet app starts lending its own money, the credit offer inside the app carries its own underwriting — before tapping accept, check who the actual lender is, the effective annual rate, and whether prepayment carries a penalty.

### Cashfree opens its checkout to AI shopping agents

Cashfree Payments launched **Checkout for Agents** on November 6 — a WebMCP-based layer that lets AI shopping agents read a checkout page's order amount, items and available payment methods directly, instead of scraping pixels, cutting token consumption by over 40%. The agent can assemble and initiate the payment, but **the final approval stays with the customer** on their own device. It's among the first moves by an Indian payment processor into agentic commerce, arriving in the same week the regulator and CERT-In flagged AI agents as a bank-attack vector — the same capability is now simultaneously a sales channel and a security problem. [Business Standard](https://www.business-standard.com/companies/news/cashfree-makes-its-checkout-readable-for-ai-agents-to-speed-up-payments-126110601690_1.html)

Consumer takeaway: when an agent pays on your behalf, the approval screen is the only checkpoint that's actually yours — verify the amount and merchant name before you confirm, because a manipulated agent can checkout faster than you can review.

## Quick hits

- **UPI MDR's post-Diwali start date is still unnotified.** The Financial Express reports sources now point to a possible **January 1, 2027** rollout, but NPCI's only confirmed position remains "immediately after Diwali" — merchants and consumers wait. [Financial Express](https://www.financialexpress.com/money/upi-mdr-after-diwali-when-will-charges-start-who-will-pay-and-what-changes-4378408)
