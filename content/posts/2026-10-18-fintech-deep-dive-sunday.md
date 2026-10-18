---
title: "Fintech Deep Dive — Sunday | October 18, 2026"
date: 2026-10-18T08:30:00+05:30
draft: false
tags: ["Fintech", "Deep Dive", "Theme: Sunday"]
categories: ["Deep Dive"]
description: "Weekly review of Indian fintech: UPI pricing, data consent, authentication and capital"
---

# Fintech Deep Dive — Sunday | October 18, 2026

**Focus:** Weekly Review — the week’s most consequential Indian fintech developments  
**Coverage period:** October 11–18, 2026 (IST)

## Executive summary

This week’s fintech story was about who pays, who may use data, and what counts as adequate proof that a payment is genuine. NPCI postponed the start of selected UPI merchant fees until after Diwali; PFRDA challenged whether NPS contributions should count as merchant payments at all. An RBI executive warned account aggregators against monetising customer data, while a new telecom-based UPI device check aims to reduce dependence on SMS OTPs. Meanwhile, nine-month funding totals rose even as deal numbers and seed investment fell, and Paramotor Digital filed for a ₹1,000-crore IPO.

Together, these developments show a sector seeking commercial sustainability without making customers bear the cost through opaque fees, excessive data use or brittle security.

## 1. UPI MDR is delayed, not cancelled

On October 13, NPCI deferred the planned October 15 start of merchant discount rates (MDR) on selected person-to-merchant UPI payments until after Diwali. A new effective date is still to be notified. The framework itself was not withdrawn: eligible merchant payments above ₹2,000 face a reported 0.4% rate, with specified categories on flat fees; person-to-person transfers and many low-value payments remain exempt. [Business Standard’s report](https://www.business-standard.com/finance/news/upi-mdr-deferred-until-after-diwali-new-date-to-be-notified-npci-126101300556_1.html) records NPCI’s announcement. An [October 11 report on an IIT Bombay analysis](https://www.business-standard.com/finance/news/upi-mdr-framework-needs-rationalisation-to-protect-public-trust-report-126101100489_1.html) describes calls to refine the design before implementation.

The immediate result is a festive-season reprieve, not clarity about the long-term payer. MDR is formally a merchant-side cost, not a tax collected from the customer. But merchants can absorb it, shift payment preferences, or try to recover it through prices or checkout friction. The practical test is whether customers can challenge an unauthorised surcharge and whether exemptions appear in actual bills—not just in payment-system documentation.

The late change also exposes a rollout problem. Acquiring banks, payment aggregators, apps and merchant systems must all update billing logic; changing the start date two days before launch is poor notice for an industry-wide rule. September UPI activity was 24.07 billion transactions worth ₹29.37 trillion, according to the same report. Even a limited fee therefore needs a fixed date, precise merchant guidance and a reliable dispute route. The IIT Bombay proposals are recommendations, not adopted policy; the next thing to watch is whether NPCI publishes clear implementation instructions before switching the framework on.

## 2. PFRDA asks whether retirement savings are a “merchant” payment

On October 13, Mint reported that the Pension Fund Regulatory and Development Authority had asked the Department of Financial Services to exempt UPI contributions made through NPS Direct Remittance (D-Remit) from MDR. PFRDA’s argument: subscribers are transferring money from their own bank accounts into retirement savings, not buying goods from a merchant. The request was pending when reported; it was not an approved exemption. Mint put NPS at 23.4 million subscribers and ₹17.36 trillion in assets. [Read Mint’s account](https://www.livemint.com/economy/pfrda-seeks-upi-mdr-exemption-for-nps-contributions-11791863636686.html).

This is a classification issue with a household consequence. A saver making a voluntary contribution above ₹2,000 should not have to guess whether a transfer into a regulated retirement account is treated like a retail purchase. If the price depends on the receiver, payment systems need to distinguish an own-account or savings transfer from an ordinary sale—and explain the distinction before the user pays.

An exemption should not be granted simply because a recipient is a financial institution. The useful rule is one based on the economic substance of a transaction: who ultimately benefits, whether a merchant is actually selling something, and whether the payer is moving money into their own account. That test could apply beyond NPS, but it must be published and consistently enforced. Until the government or NPCI answers PFRDA, subscribers should not assume either that a fee applies or that they are exempt. It is another reason the post-Diwali notice needs transaction-level examples, not only a percentage table.

## 3. RBI’s account-aggregator reminder: consent is not a licence to monetise

At Sahamati’s Samvaad 2026, RBI Executive Director Kesavan Ramachandran cautioned account aggregators against monetising customer financial data. He said information should be shared only with customer consent and for the authorised purpose, and reiterated the framework’s data-blind design. The remarks were reported on October 15 by [The Times of India](https://timesofindia.indiatimes.com/business/india-business/rbi-cautions-account-aggregators-against-monetising-data/articleshow/134969096.cms). This was a public supervisory signal—not a new RBI circular or enforcement order.

The AA system is meant to transmit data from a financial information provider to a financial information user under a customer-approved consent artefact. The aggregator is not supposed to turn that flow into a proprietary customer-data store. Consent to share information for one loan or service should not quietly become permission for persistent profiling, resale or unrelated targeting. Without purpose limits that survive downstream transfers, “consent-based” describes the interface, not the actual data practice.

Ramachandran also cautioned providers against withholding data when a customer has given valid consent, and spoke about interoperability and standardised formats. That creates a dual obligation: make customer-directed sharing work, while ensuring that interoperability does not become a larger market for sensitive data. Customers should be able to see who requested which data, for what purpose and duration, and how to revoke access. Firms need audit trails across vendors and AI-enabled processing—not merely a consent screen. The RBI’s remarks point toward that standard, but the reviewed coverage did not identify a new binding direction.

## 4. Silent mobile verification trades OTP friction for network-level signals

Bureau announced Silent Mobile Verification for UPI device binding on October 15. Instead of asking customers to enter an SMS OTP, the service checks through a telecom operator’s data network whether a phone number, SIM and requesting device are associated. [ETTelecom reported](https://telecom.economictimes.indiatimes.com/amp/news/devices/bureau-launches-silent-mobile-verification-for-upi-device-binding/134967005) that NPCI circular OC-238 recognises silent verification as an alternative binding method. Bureau says its service handles more than three million checks a day across 20-plus enterprises and has coverage above 96%; these are company-reported figures, not independent performance results.

Less OTP friction could help onboarding and reduce exposure to some message-interception or SIM-swap attacks. But “silent” does not mean risk-free or invisible. The service description involves sharing a mobile number and device IP address with the verification provider, which checks with the operator. Customers should be told what data is used, how long it is retained and what happens when a check fails.

A SIM/device match is one signal, not proof that the account holder is present or that a payment is legitimate. It cannot stop a customer being coached into approving a transfer. The protection depends on how apps combine it with transaction-risk checks, safe account recovery, a fallback for unsupported devices or poor connectivity, and usable dispute handling. The product’s value will be measured not only by faster authentication, but also by false rejections, privacy practices and whether fraud losses actually fall.

## 5. Funding totals rise as the pipeline narrows; IPO filings test the market

A Tracxn snapshot published October 13 found Indian fintech raised $2.2 billion in January–September 2026, 14% more than a year earlier. Yet funding rounds fell 41%, from 260 to 153. Five deals of $100 million or more made up about $1.1 billion; CRED’s $540 million Series H alone contributed roughly a quarter. Late-stage funding grew to $1.5 billion, 67% of capital and the only stage to expand. Early-stage funding fell 33% to $668 million, while seed funding dropped 57% to $73.8 million. [Business Standard’s Tracxn report](https://www.business-standard.com/finance/news/fintech-funding-up-14-to-2-2-bn-in-jan-sep-deal-count-falls-41-tracxn-126101300252_1.html) shows a market concentrating rather than broadly accelerating.

Digital lending drew $809 million, payments $776 million and investment technology $450 million over the nine months. Those figures do not mean every category is thriving: fewer rounds and lower seed investment make the runway harder for new firms, even as established companies attract large cheques. A rising total can therefore coexist with weaker access to capital for first-time founders. The policy question is whether this concentration rewards responsible scale—or makes incumbents the only firms able to finance compliance, security and distribution.

Paramotor Digital Technology’s proposed IPO adds a public-market test. The fintech, which works in digital gifting, spend management, rewards and loyalty, filed updated draft papers for a ₹1,000-crore issue: up to ₹698 crore of fresh shares and ₹302 crore of promoter sales. The company may also consider a ₹139.60-crore pre-IPO placement. Proceeds are intended mainly for customer acquisition and promotion (₹355 crore) and technology and cloud infrastructure (₹94 crore). [The Hindu BusinessLine’s report](https://www.thehindubusinessline.com/markets/paramotor-digital-files-for-1000-crore-ipo-with-sebi/article71586661.ece) gives FY26 consolidated revenue of ₹603.15 crore and profit after tax of ₹59.14 crore, while noting that earlier-year revenue figures were standalone. It also reports 1.58 million transacting users and 99% retention.

The fresh issue funds the company; the OFS gives existing shareholders liquidity. Investors should examine segment margins, revenue recognition and how much growth came from new products before treating the headline growth as comparable. The filing is not a valuation or a guarantee of listing success. Its significance is that fintech firms are seeking public capital while private money concentrates in later-stage businesses—and markets will have to judge the quality, not just the scale, of reported growth.

## The week’s pattern

Across fees, data and authentication, classification is becoming part of the infrastructure. “Merchant” versus “own-account transfer” decides MDR; customer-authorised versus monetised data decides privacy; device binding versus identity assurance sets the limits of silent verification. Those labels shape both economics and user experience, so they need transparent rules and appeal routes.

The week also shows capital staying available but becoming choosier. UPI fee uncertainty, consent rules and IPO disclosures all point to the same test: can a fintech business grow without exporting risk to consumers? “Free,” “consented” and “frictionless” are not outcomes until users can contest charges, revoke access and recover from false security decisions.

## Data points to carry forward

- UPI MDR: October 15 start deferred until after Diwali; date pending.
- September UPI: 24.07 billion transactions worth ₹29.37 trillion.
- NPS: 23.4 million subscribers; ₹17.36 trillion in assets; PFRDA’s request unresolved.
- Fintech funding: $2.2 billion across 153 rounds in 9M 2026; late-stage share 67%.
- Paramotor proposal: ₹1,000 crore, split between ₹698 crore fresh issue and ₹302 crore OFS.

## Watchlist for the coming week

1. NPCI’s new MDR date, implementation guidance and merchant-facing surcharge protections.
2. A decision on PFRDA’s D-Remit request and a general test for own-account transfers.
3. Written AA guidance on consent, purpose limits and downstream auditability.
4. Independent SMV results: privacy, coverage gaps, false rejections and fraud outcomes.
5. Paramotor’s full prospectus, segment economics and further fintech IPO filings.

## Sources

- [NPCI MDR deferral and September UPI data — Business Standard, October 13](https://www.business-standard.com/finance/news/upi-mdr-deferred-until-after-diwali-new-date-to-be-notified-npci-126101300556_1.html)
- [IIT Bombay MDR analysis — Business Standard, October 11](https://www.business-standard.com/finance/news/upi-mdr-framework-needs-rationalisation-to-protect-public-trust-report-126101100489_1.html)
- [PFRDA’s NPS request — Mint, October 13](https://www.livemint.com/economy/pfrda-seeks-upi-mdr-exemption-for-nps-contributions-11791863636686.html)
- [RBI account-aggregator remarks — The Times of India, October 15](https://timesofindia.indiatimes.com/business/india-business/rbi-cautions-account-aggregators-against-monetising-data/articleshow/134969096.cms)
- [Silent Mobile Verification — ETTelecom, October 15](https://telecom.economictimes.indiatimes.com/amp/news/devices/bureau-launches-silent-mobile-verification-for-upi-device-binding/134967005)
- [9M fintech funding — Business Standard / Tracxn, October 13](https://www.business-standard.com/finance/news/fintech-funding-up-14-to-2-2-bn-in-jan-sep-deal-count-falls-41-tracxn-126101300252_1.html)
- [Paramotor Digital IPO — The Hindu BusinessLine, October 15](https://www.thehindubusinessline.com/markets/paramotor-digital-files-for-1000-crore-ipo-with-sebi/article71586661.ece)
