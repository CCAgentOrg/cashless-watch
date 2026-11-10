---
title: "Fintech Brief — November 10, 2026"
date: 2026-11-10T08:00:00+05:30
draft: false
tags: ["Fintech", "Daily Brief", "India", "RBI", "NPCI", "UPI", "Cybersecurity", "Funding"]
categories: ["Daily Brief"]
description: "RBI orders CERT-In audits for NBFC API clients and debit safeguards by December 3, UPI's October data shows merchants dominate volume but person-to-person transfers carry 69% of value, Dubai Duty Free offers 10% off for UPI payments, and fintech funding concentrates late-stage while a $5M seed targets remittance receivers."
---

# Fintech Brief — November 10, 2026

## Today's Top Stories

### RBI to banks: audit your NBFC API clients, whitelist beneficiaries, and watch for mule patterns

Beyond last week's consolidated cyber rulebook for non-bank payment operators, RBI has moved on the bank side. A **confidential cybersecurity advisory dated November 3**, now circulating through explainers published over the weekend, directs banks offering **API-based fund transfers to NBFCs** to lock down a channel that has become a favoured route for unauthorised debits ([The Head & Tale](https://theheadandtale.com/deepdives/exclusive-rbi-tightens-api-security-rules-for-banks-after-nbfc-cyberattacks-mandates-audits-beneficiary-checks/); [MediaNama](https://www.medianama.com/2026/11/223-rbi-cyber-security-rules-payment-companies); [Elets BFSI](https://bfsi.eletsonline.com/rbi-bank-nbfc-api-controls/)). Banks must maintain a full **inventory of every API client** — NBFCs, business correspondents, payment aggregators, PSPs — with business profiles, integration details, transaction limits and security contacts. NBFC clients must undergo **annual audits by CERT-In-empanelled auditors**: new NBFCs get audited before they touch the API, and existing ones have until **February 3, 2027** to complete a first audit, with re-audits after any material cyber incident. By **December 3, 2026**, banks must enforce one of two safeguards on API debits — **beneficiary whitelisting** (payouts only to pre-registered accounts) or **maker-checker / out-of-band confirmation** — with narrow exceptions only after a documented risk assessment. The advisory also demands client-specific fraud baselines: alerts for sudden spikes, transactions patterned just below limits, after-hours activity, mule accounts and shifts in software fingerprints.

Consumer takeaway: the unauthorised-debit complaints that begin "I never signed up for this loan app EMI" travel through exactly these bank-to-NBFC APIs. Audits before access and whitelisted payout accounts attack the failure at its source — but the advisory is confidential, so there is no public register of which banks actually complied by December 3. Watch your statements regardless.

### UPI October: merchant payments own the volume, person-to-person owns the money

NPCI's October data, published November 9, shows UPI at **25.47 billion transactions worth ₹31.53 lakh crore** — up 5.8% and 7.3% over September, and 23% and 15.6% over October 2025 ([MediaNama](https://www.medianama.com/2026/11/223-upi-p2m-p2p-transactions-october-2026/); [NPCI](https://www.npci.org.in/product/upi/product-statistics)). The composition is the interesting part: merchant payments were **16.09 billion transactions — 63.2% of volume — but only ₹9.71 lakh crore, 30.8% of value**, while person-to-person transfers were 9.37 billion transactions carrying **₹21.82 lakh crore, 69.2% of all value**. Average daily value crossed ₹1.01 lakh crore, with the average ticket at ₹1,238 and 758 banks now live. The split matters for the MDR fight in the Supreme Court: the contested fee touches only person-to-merchant payments above ₹2,000 — about 4% of P2M volume by NPCI's own submission — while the two-thirds of value that flows person-to-person stays free at any amount. Separately, technical declines among the top 20 banks rose to **0.24%** in September ([MediaNama](https://www.medianama.com/2026/11/223-upi-technical-decline-rate-rises-september-2026/)) — a reminder that scale is outrunning reliability.

Consumer takeaway: when you hear "UPI is mostly merchant payments", remember the money says otherwise — big-ticket transfers between people dominate value, and that entire flow remains outside the MDR debate.

### UPI lands a 10% discount at Dubai Duty Free

NPCI International has tied up with **Dubai Duty Free** to give Indian travellers **10% off eligible purchases paid via UPI, capped at AED 100**, across Dubai International and Al Maktoum International airports, with **Network International** as the acquiring partner ([Trak.in](https://trak.in/stories/dubai-duty-free-starts-offering-upi-discount-upto-10); [Zee Business](https://www.zeebiz.com/world/news-dubai-duty-free-offer-indian-tourists-can-save-up-to-aed-100-on-dubai-duty-free-purchases-using-upi-405169)). Travellers must activate **UPI International** in their UPI app and hold an eligible Indian bank account before paying.

Consumer takeaway: a ₹2,400-max discount is a marketing nudge, not a deal-breaker — but the acceptance build-out at one of the world's busiest airports is the real signal. Before flying, check that your bank and app actually support UPI International, and compare the FX conversion your app applies against carrying dirhams.

### Fintech funding: up 14% and going late-stage

India's fintech funding for January–September 2026 stands at **$2.2 billion, up 14% year-on-year**, with three fintech IPOs against two last year and India ranked second globally behind the US on Dealroom's tally — but roughly **two-thirds of the capital went to late-stage rounds**, and seed and Series A investors have turned selective, leaving early-stage founders facing a widening Series A gap ([BW Disrupt](https://www.bwdisrupt.com/article/how-india-s-fintech-growth-hinges-on-bridging-the-series-a-gap-632694)). One fresh early round cuts against the grain: London-based **Seva Money raised a $5 million seed** to build wallets and cards for **remittance receivers in India and Mexico** — payment instruments for the people at the receiving end of cross-border transfers, not the senders ([Tech Funding News](https://techfundingnews.com/seva-money-5m-seed-remittance-wallets-recipient-cards)).

Consumer takeaway: capital concentrating in proven companies means fewer experiments in consumer financial products — which makes the rare early bets on underserved users, like remittance receivers, worth watching.
