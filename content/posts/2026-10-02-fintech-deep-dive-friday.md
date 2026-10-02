---
title: "Fintech Deep Dive — Friday | October 02, 2026"
date: 2026-10-02T08:30:00+05:30
draft: false
tags: ["Fintech", "Deep Dive", "Theme: Friday"]
categories: ["Deep Dive"]
description: "Weekly analysis of Friday theme in Indian fintech"
---

# Fintech Deep Dive — Friday | October 02, 2026

**Focus:** Friday — Policy & Regulation: RBI, SEBI, payments law and compliance  
**Coverage period:** September 26–October 2, 2026 (seven calendar days)

## Executive summary

This week’s story is who sets payment prices, how banks publish theirs, and what cross-border reporting means when a service is bought by card. The Supreme Court let UPI MDR proceed for now, reserving legal questions; merchant groups withdrew, but did not resolve, their protest. RBI’s bulk-deposit and foreign-trade reporting rules went live. SEBI’s exchange self-listing review remains only a reported proposal.

## Key developments

### 1. UPI MDR survives the first court test; the argument moves to implementation

On September 28, the Supreme Court declined to stay the Centre’s new MDR framework for specified high-value person-to-merchant (P2M) UPI payments. It issued notice to the Centre and other respondents and sought their replies. The bench reportedly pressed the government to explain the legal character and basis of the charge — including whether it is a tax or a fee. This is not a ruling that the framework is valid: the constitutional and statutory questions remain open. The petition, *Anjan Datta v. Union of India*, challenges how the government can withdraw the previous no-charge protection for certain UPI transactions, draw categories and set rates. [The Hindu’s court report](https://www.thehindu.com/business/Economy/if-neither-tax-nor-fee-what-is-this-expropriation-supreme-court-asks-govt-on-upi-mdr-charges/article71518779.ece) and [LawBeat’s account of the petition](https://lawbeat.in/top-stories/breaking-supreme-court-refuses-to-stay-centres-mdr-on-upi-transactions-over-2000-1636066) distinguish the court’s questions from the petitioner’s allegations.

The operational terms remain due to take effect on October 15: the government says a 0.4% MDR will apply to eligible P2M transactions above ₹2,000, capped at ₹300 for transactions of ₹75,000 or more. Specified essential and thin-margin sectors—including railways, telecom, insurance, fuel and agricultural inputs—pay a flat ₹5; capital-market payments use 0.02%, capped at ₹300. P2P transfers stay free; [NPCI says P2PM merchants with up to ₹1 lakh in monthly QR receipts remain exempt, even on a single payment above ₹2,000](https://www.npci.org.in/uploads/FA_Qs_Merchant_Discount_Rate_MDR_on_Select_UPI_P2_M_Transactions_58dba1d39e.pdf). The government says roughly 96% of merchant transactions are outside the fee, and that merchants should not pass it on to customers. Those are the government’s framework and estimates, not independent evidence that a merchant will absorb every rupee. [The Finance Ministry’s September 15 statement](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2310586) sets out the tiers, exemptions and consumer-protection position.

On September 30, AIMRA and AICPDF called off their proposed October 2 “No UPI Day” after a delegation met Finance Minister Nirmala Sitharaman. Their representation had sought deferral or phasing, a revised threshold and exclusion of merchant-to-merchant payments; the minister’s assurance that concerns would be considered was not a change to the October 15 start date. [Mint’s report](https://www.livemint.com/news/india/traders-body-associations-cait-aimra-call-off-no-upi-day-protest-2-october-assurance-finance-minister-nirmala-sitharaman-11790777139652.html) records the withdrawal, not a settlement of the policy dispute.

The context is a still-growing network, not a network in retreat: NPCI data reported by Mint show 24.07 billion UPI transactions worth ₹29.37 lakh crore in September, down 1.8% and 1.5% respectively from August but up 23% and 18% year on year. The fee was not yet live, so this one-month dip cannot be attributed to MDR. [Mint’s data report](https://www.livemint.com/money/upi-hits-24-billion-transactions-in-september-npci-data-shows-1-8-monthly-dip-amid-mdr-concerns-11790847660336.html) is useful as a baseline, not a causal test.

**Why it matters:** The first big test is not just whether consumers see a line-item surcharge. It is whether merchants reprice, refuse certain payments, split transactions, or shift costs into posted prices. A direction against explicit pass-through can protect the checkout screen without making merchant economics disappear. The court case could also force greater clarity on the statutory instrument, evidence for the categories and thresholds, and who supervises a rate-setting process involving the NPCI-led ecosystem. No stay means prepare for rollout; it does not mean the challenge has been decided.

### 2. RBI makes bulk-deposit pricing visible — with a liquidity exception

RBI’s deposit-rate amendments took effect on October 1. Banks must publish bulk-deposit rates on their websites by 10:00 a.m. on each business day, with a ten-minute grace period, and pay according to the rate disclosed in advance. For deposits of similar amount accepted on the same date, the rate must be uniform across a bank’s branches and customers. The amendment also lets a bank offer different rates where deposits carry different run-off treatment under the Liquidity Coverage Ratio (LCR) rules. In other words: more public pricing, not one universal rate for every large depositor. [RBI’s July 30 direction](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=13656&Mode=0) is the primary text; [BusinessLine’s October 1 report](https://www.thehindubusinessline.com/money-and-banking/banks-lose-pricing-advantage-as-rbis-bulk-deposit-disclosure-norm-kicks-in/article71534059.ece) checked how publication looked on the first day.

For scheduled commercial banks and small finance banks, “bulk” generally means a single rupee term deposit of ₹3 crore or more; thresholds differ for some other bank categories. This does not change the rate on an ordinary household fixed deposit. It changes how treasurers, institutions and large depositors can compare offers — and constrains branch-by-branch bargaining for otherwise similar deposits. The public table may also be useful to deposit-marketplace and treasury-software providers, but only if they capture the rate’s timestamp, tenure, deposit type and any LCR-linked condition rather than flattening unlike products into one “best rate.”

The consumer-facing measure is simple: the bank’s own website becomes a reference point if the contracted rate is disputed. The practical gap is data quality. The daily snapshot needs to remain accessible, dated and consistent across the bank’s website and booking channel. RBI’s LCR exception also means depositors should ask why two apparently similar offers differ; transparency lets them see the terms, but does not erase legitimate liquidity-based pricing. Initial reports of banks still updating rates on day one are a compliance-and-observability issue to monitor, not proof that the direction has been universally ignored.

### 3. Cross-border service reporting goes live; card-funded subscriptions expose a gap

RBI’s new Foreign Exchange Management (Export and Import of Goods and Services) framework came into force on October 1. A September 22 amendment, published in the Gazette on September 24, changed the export-realisation window: generally, export proceeds must now be realised within nine months, rather than fifteen; where the invoice or settlement is in rupees, the comparable period is twelve months rather than eighteen. Authorised Dealer (AD) banks also have to record service-import details in the Import Data Processing and Monitoring System (IDPMS) within five working days of receiving the importer’s documents. For eligible service invoices up to ₹10 lakh, an importer’s declaration can support closure of an entry, including through a quarterly declaration. The RBI framework also requires banks to publish an operating policy, keep charges reasonable and proportional, and not penalise customers for a regulatory delay or violation. See the [RBI’s consolidated regulations](https://www.rbi.org.in/Scripts/BS_FemaNotifications.aspx?Id=13277) and [September amendment](https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=13714&Mode=0).

That is a real reporting framework for trade in services — but it is not yet an intelligible instruction for a person paying an overseas software or media subscription by international card. The rules say an AD bank records service-import details as declared and submitted by the importer. In a card transaction, payment may already have been authorised before the issuer has the underlying invoice or trade data. On October 1, *The Economic Times* reported that the new regulations do not specify how individuals’ personal-service purchases or corporate-card service purchases should be reported to banks, and that the process for international card payments remains unclear. [Its report on services such as software and digital subscriptions](https://economictimes.indiatimes.com/news/economy/finance/claude-new-yorker-bandcamp-rbi-rules-leave-international-card-payments-in-grey-area/articleshow/134601744.cms) highlights an implementation question, not a confirmed new duty on every cardholder.

The distinction matters. “Services are now in the trade-reporting system” does not, by itself, tell an individual to file a form for every app subscription. RBI and card issuers should publish a plain-language answer on scope, who supplies the invoice data, what the cardholder must do, and whether recurring small payments can be reported in aggregate. Until that arrives, consumers should follow their issuer’s written instructions rather than infer a filing requirement from headlines. Indian firms buying cloud, design, data or AI services abroad should meanwhile keep invoices and payment records accessible and ask their AD bank how its new service-import workflow handles card settlement.

### 4. SEBI reportedly reopens exchange self-listing — a governance question, not a rule

On September 28, NDTV Profit reported that SEBI was expected to form a panel of officials and market experts to examine whether a stock exchange could list its own shares on its own platform. The report, citing unnamed sources, said recommendations might follow in 60–90 days and could lead to a consultation paper. It also described a possible safeguard: another “primary” exchange could retain compliance oversight. No panel order, consultation paper or new rule was public in the report; this should be treated as a reported proposal, not a SEBI decision. [NDTV Profit’s report](https://www.ndtvprofit.com/markets/after-nse-lists-on-bse-sebi-set-to-form-panel-to-revisit-self-listing-rules-12108091) situates the question after NSE shares began trading on BSE.

This is adjacent to fintech rather than a startup-specific rule, but exchanges are core digital market infrastructure. Self-listing could widen access to ownership and market discipline; it also puts a commercial issuer inside the venue that sets trading rules, monitors conduct and operates market systems. Any design needs independent surveillance, transparent data access and a credible route for investigating the exchange’s own securities. The proposal’s value will depend less on whether self-listing is allowed in principle than on whether the regulator can make oversight demonstrably independent. The next meaningful signal is a published panel mandate or consultation, not another anonymous-source headline.

## Trend analysis

The four stories point in different directions. UPI pricing is being challenged in court and negotiated politically; deposit rules move the opposite way by forcing large-ticket rates into public view; foreign-trade reporting expands data capture faster than it explains the cardholder journey; and exchange governance is still at the “study this” stage. Across them, the regulator’s choice of mechanism matters as much as the objective. A fee needs a transparent legal basis and safeguards against hidden consumer incidence. A reporting duty needs a workable data path from merchant and card network to bank. A disclosure rule needs a stable record that a depositor can actually verify.

## Data & metrics

- **UPI MDR:** 0.4% on eligible merchant payments above ₹2,000; cap of ₹300 from ₹75,000; government estimates about 4% of merchant transactions affected. These are official framework figures, not observed outcomes.
- **UPI use:** September volume was 24.07 billion; value was ₹29.37 lakh crore. Both fell slightly month on month but grew year on year. MDR does not begin until October 15, so the September change predates it.
- **Deposit disclosures:** daily bulk-rate publication is due by 10:00 a.m., with a grace period to 10:10 a.m.; LCR-based differentiation remains permitted.
- **Trade reporting:** the current amended export-realisation windows are nine months, or twelve months for specified rupee-settled exports.

## Upcoming watchlist

1. The Supreme Court’s four-week response window in *Anjan Datta v. Union of India*; whether the government supplies the legal instrument and evidentiary basis questioned in the petition.
2. October 15 UPI MDR commencement: actual merchant billing, consumer complaints, exemptions and whether merchants reprice or refuse eligible payments.
3. RBI/card-issuer instructions for imported services paid by international card, especially subscriptions and software purchases.
4. Whether banks publish dependable daily bulk-rate records, and whether SEBI formally announces a self-listing panel or opens public consultation.

## Sources

- [RBI — Commercial Banks Interest Rate on Deposits, Second Amendment Directions (July 30)](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=13656&Mode=0)
- [RBI — Export and Import of Goods and Services Regulations (consolidated through September 22)](https://www.rbi.org.in/Scripts/BS_FemaNotifications.aspx?Id=13277)
- [RBI — Export and Import of Goods and Services Amendment Regulations (September 22)](https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=13714&Mode=0)
- [NPCI — MDR FAQs, including merchant categorisation and exemptions](https://www.npci.org.in/uploads/FA_Qs_Merchant_Discount_Rate_MDR_on_Select_UPI_P2_M_Transactions_58dba1d39e.pdf)
- [Finance Ministry — UPI MDR framework and exemptions (September 15)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2310586)
- [The Hindu — Supreme Court refuses interim stay and questions legal basis (September 28)](https://www.thehindu.com/business/Economy/if-neither-tax-nor-fee-what-is-this-expropriation-supreme-court-asks-govt-on-upi-mdr-charges/article71518779.ece)
- [LawBeat — Anjan Datta petition and court notice (September 28)](https://lawbeat.in/top-stories/breaking-supreme-court-refuses-to-stay-centres-mdr-on-upi-transactions-over-2000-1636066)
- [Mint — Trader groups withdraw planned “No UPI Day” (September 30)](https://www.livemint.com/news/india/traders-body-associations-cait-aimra-call-off-no-upi-day-protest-2-october-assurance-finance-minister-nirmala-sitharaman-11790777139652.html)
- [Mint — September UPI transaction figures (October 1)](https://www.livemint.com/money/upi-hits-24-billion-transactions-in-september-npci-data-shows-1-8-monthly-dip-amid-mdr-concerns-11790847660336.html)
- [The Hindu BusinessLine — Bulk-deposit rates on first day of RBI rules (October 1)](https://www.thehindubusinessline.com/money-and-banking/banks-lose-pricing-advantage-as-rbis-bulk-deposit-disclosure-norm-kicks-in/article71534059.ece)
- [The Economic Times — International card payments and RBI service-import reporting gap (October 1)](https://economictimes.indiatimes.com/news/economy/finance/claude-new-yorker-bandcamp-rbi-rules-leave-international-card-payments-in-grey-area/articleshow/134601744.cms)
- [NDTV Profit — SEBI exchange self-listing panel under consideration (September 28)](https://www.ndtvprofit.com/markets/after-nse-lists-on-bse-sebi-set-to-form-panel-to-revisit-self-listing-rules-12108091)
