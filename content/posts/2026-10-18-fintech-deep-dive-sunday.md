---
title: "Fintech Deep Dive — Sunday | October 18, 2026"
date: 2026-10-18T08:30:00+05:30
draft: false
tags: ["Fintech", "Deep Dive", "Theme: Sunday"]
categories: ["Deep Dive"]
description: "Weekly analysis of Sunday theme in Indian fintech"
---

# Fintech Deep Dive — Sunday | October 18, 2026

**Focus:** Weekly Review — the week’s most consequential Indian fintech developments  
**Coverage period:** October 11–18, 2026 (IST)

## Executive summary

This week’s fintech story was a renegotiation of trust and cost. NPCI delayed selected UPI merchant fees until after Diwali, with no new date. PFRDA’s request to exempt NPS D-Remit transfers raises whether a payment to one’s own retirement account is a merchant purchase. The RBI warned account aggregators against monetising customer data, while a telecom-backed UPI verification product promises less OTP friction. Funding rose even as deals and seed rounds fell; a ₹1,000-crore fintech IPO filing now tests public-market appetite.

The common thread: digital finance must fund growth without quietly billing consumers through charges, data use, or brittle authentication.

## 1. UPI MDR is delayed, not cancelled

On October 13, NPCI postponed the planned October 15 start of merchant discount rates on selected UPI transactions until after Diwali. A new effective date is still pending. The reported framework remains: 0.4% MDR on eligible person-to-merchant payments above ₹2,000, with specified categories using a flat ₹5 charge; P2P transfers and most small payments remain outside the charge. [Business Standard](https://www.business-standard.com/finance/news/upi-mdr-deferred-until-after-diwali-new-date-to-be-notified-npci-126101300556_1.html) reported the deferral. An [October 11 report on an IIT Bombay analysis](https://www.business-standard.com/finance/news/upi-mdr-framework-needs-rationalisation-to-protect-public-trust-report-126101100489_1.html) captures the concern that the framework needs to protect public trust.

The immediate effect is a reprieve for merchants during peak festive trading, not a resolution of who should fund payment infrastructure. The formal fee is a merchant-side cost, not a tax charged to the payer. But that does not guarantee consumers will never feel it: merchants can absorb the cost, adjust prices, change payment preferences, or add checkout friction. Transparency about any surcharge and a workable complaint route matter as much as the headline rate.

The late deferral also exposes an operational weakness. Acquirers, payment aggregators, apps and merchant systems all need to implement the same rules. Changing the start date two days before launch reduces immediate disruption but makes testing and business planning harder. The stakes are large: September UPI handled 24.07 billion transactions worth ₹29.37 trillion, up 22.6% and 18% respectively year over year, according to Business Standard. Even a narrowly scoped fee rule operates across a vast payments network.

The IIT Bombay recommendations are proposals, not adopted policy. The next test is whether NPCI issues a firm date and clear operational guidance before launch—and whether exemptions show up in merchant settlement statements, not only in circulars.

## 2. NPS contributions expose a classification fault line

Mint reported on October 13 that PFRDA had asked the Department of Financial Services to treat NPS contributions through UPI’s D-Remit facility as P2P transfers, not merchant payments. Subscribers move money from their own bank accounts into their retirement accounts; PFRDA argues this is not a retail purchase. The regulator confirmed it had made the request, but no decision had been reported. NPS had 23.4 million subscribers and ₹17.36 trillion in assets. [Mint’s report](https://www.livemint.com/economy/pfrda-seeks-upi-mdr-exemption-for-nps-contributions-11791863636686.html) explains the request and the D-Remit mechanism.

This is more than a technical label. If MDR depends on the receiving entity, a saver making a voluntary contribution above ₹2,000 needs to know whether the payment is being treated as a purchase or a transfer into their own regulated account. Payment systems should distinguish economic purpose, not infer it from the recipient’s merchant identifier alone.

An exemption could protect long-term saving from a fee designed for commerce. But exemptions need principled boundaries: automatically exempting every financial institution could create a maze of special cases. A published test should consider who benefits, whether a product is being sold, and whether funds are being transferred to the customer’s own account. Until DFS or NPCI answers, savers should not assume either that a charge will apply or that it will not. The MDR notification needs transaction-level examples, not just rates.

## 3. RBI’s account-aggregator reminder: consent is not a licence to monetise

At Sahamati’s Samvaad 2026, RBI Executive Director Kesavan Ramachandran said account aggregators must guard against monetising customer financial data. Information should move only with customer consent and for the purpose authorised; the AA should preserve a data-blind role rather than store or decrypt the data. He also cautioned financial information providers against withholding data when valid consent exists. These remarks were reported on October 15 by [The Times of India](https://timesofindia.indiatimes.com/business/india-business/rbi-cautions-account-aggregators-against-monetising-data/articleshow/134969096.cms). This was a speech, not a new RBI circular or enforcement order.

That distinction is important. The AA framework is meant to transmit customer-authorised information between financial information providers and users. If a narrow permission becomes persistent profiling, resale, or unrelated targeting, “consent-based” becomes a label rather than a meaningful limit. The customer should be able to see what was requested, by whom, for what purpose, and how to revoke access.

The RBI is also pursuing interoperability and standardised data formats. This could reduce repeated onboarding and make it easier for smaller AAs to compete, while making purpose limits, access logs, revocation and incident response more important across the data chain. There are duties on both sides: providers should honour valid consent, and recipients should not repurpose the data. The remarks are best read as a supervisory signal about the direction of travel—not proof that any particular AA broke a rule. Firms should be able to demonstrate consent and purpose controls through every downstream vendor, including AI-enabled processing.

## 4. Silent mobile verification reduces OTP friction—but adds a new data flow

Bureau announced Silent Mobile Verification for UPI device binding on October 15. The service uses a mobile operator’s network to check whether the registered number, SIM and requesting device are associated, instead of asking the customer to enter an SMS OTP. ETTelecom reported a response in under four seconds, company-stated coverage above 96% across three leading operators, and more than three million daily checks across 20-plus enterprises. Those figures are vendor claims, not independent performance results. [ETTelecom’s report](https://telecom.economictimes.indiatimes.com/amp/news/devices/bureau-launches-silent-mobile-verification-for-upi-device-binding/134967005) says the service aligns with NPCI operating circular OC-238, dated September 30, which recognises silent verification as an alternative device-binding method.

Less reliance on OTPs could improve onboarding and reduce exposure to some message-interception and SIM-swap workflows. But “silent” is not the same as risk-free or invisible. The service description says an app shares a mobile number and device IP address with the provider, which checks with the telecom operator. Customers need clear answers on what data moves, what is retained, and how a failed match affects access.

A network signal is not a complete fraud verdict: it cannot prove who is holding the phone, whether a transaction is legitimate, or whether the user is being socially engineered. The gain depends on layering verification with transaction-risk checks, safe account recovery, fallback methods and accessible dispute handling. The deployment question is also one of inclusion: a customer with unsupported hardware or poor connectivity must not be locked out without a usable alternative. The next generation of authentication may be smoother, but it increasingly depends on private risk vendors and telecom infrastructure; independent testing and data minimisation should be part of rollout.

## 5. Funding concentrates; Paramotor tests public-market appetite

Tracxn data reported October 13 showed Indian fintech raised $2.2 billion in January–September 2026, up 14% from $1.9 billion a year earlier. Yet rounds fell 41%, from 260 to 153. Five deals of at least $100 million made up nearly half the total. Late-stage funding nearly doubled to $1.5 billion, or 67% of all capital; early-stage funding fell 33% to $668 million and seed funding fell 57% to $73.8 million. [Business Standard’s report](https://www.business-standard.com/finance/news/fintech-funding-up-14-to-2-2-bn-in-jan-sep-deal-count-falls-41-tracxn-126101300252_1.html) details the stage-wise split.

So “funding up” hides a narrower market. Established companies still attract large cheques, while fewer rounds and lower seed activity make it harder for new entrants to test alternatives. Lending drew $809 million, payments $776 million, and investment technology $450 million in the nine-month period. These numbers indicate capital allocation, not proof of product quality or consumer benefit. The signal is a preference for scale, perceived risk control, and a credible route to profitability or liquidity.

Paramotor Digital Technology’s proposed IPO provides a case study. The company filed updated draft papers for a ₹1,000-crore issue: up to ₹698 crore of fresh shares and ₹302 crore of promoter sales. It may also raise up to ₹139.60 crore in a pre-IPO placement, reducing the fresh issue correspondingly. The Hindu BusinessLine reported FY26 consolidated revenue of ₹603.15 crore, profit after tax of ₹59.14 crore, 1.58 million transacting users and a reported 99% retention rate. FY24 and FY25 revenue figures in the filing were standalone, while FY26 was consolidated, so the series is not directly comparable without the full accounting and acquisition context. [BusinessLine’s coverage](https://www.thehindubusinessline.com/markets/paramotor-digital-files-for-1000-crore-ipo-with-sebi/article71586661.ece) describes the issue and use of proceeds, including ₹355 crore for customer acquisition and brand promotion.

Fresh capital funds the business; an offer for sale gives existing holders liquidity. Neither is inherently good or bad, but investors should inspect segment margins, revenue recognition, customer concentration and whether growth came from new products or acquisitions. For consumers, the relevant question is whether spending on customer acquisition and loyalty platforms produces durable value—or simply buys engagement. The IPO is proposed, not priced; the disclosed results and eventual valuation will matter more than the ₹1,000-crore headline.

## The week’s pattern

Three fault lines stand out. First, **classification now determines economics and rights**: merchant versus P2P sets UPI fees; authorised sharing versus monetisation sets data boundaries; device binding versus identity assurance sets the limits of fraud controls. Those labels need to be explainable and contestable.

Second, the trust bargain must be visible in daily operations. “Free UPI,” “consented data,” and “frictionless authentication” mean little if customers cannot contest a fee, revoke access, recover an account or reach a person after automation fails.

Finally, capital remains available but concentrated. That may reward firms with proven economics, while starving early-stage alternatives that could improve choice. Scale is not itself consumer value.

## Data points to carry forward

- MDR: October 15 start deferred until after Diwali; replacement date pending.
- UPI, September: 24.07 billion transactions; ₹29.37 trillion value.
- NPS: 23.4 million subscribers; ₹17.36 trillion assets; PFRDA request unresolved.
- Fintech, 9M 2026: $2.2 billion across 153 rounds; late-stage capital was 67%.
- Paramotor proposal: ₹1,000 crore, including ₹698 crore fresh issue and ₹302 crore OFS.

## Watchlist for the coming week

1. NPCI’s new MDR date, merchant guidance, exemptions and rules against passing a separate fee to consumers.
2. A formal DFS or NPCI decision on D-Remit—and the principle for other own-account transfers.
3. Whether RBI or Sahamati turns AA consent and data-blindness remarks into auditable guidance.
4. Independent results and privacy safeguards for silent verification, including fallback and failure handling.
5. Paramotor’s full prospectus: segment economics, revenue recognition and use of fresh proceeds.

## Sources

- [UPI MDR deferral and September transaction data — Business Standard, October 13](https://www.business-standard.com/finance/news/upi-mdr-deferred-until-after-diwali-new-date-to-be-notified-npci-126101300556_1.html)
- [IIT Bombay analysis of the MDR framework — Business Standard, October 11](https://www.business-standard.com/finance/news/upi-mdr-framework-needs-rationalisation-to-protect-public-trust-report-126101100489_1.html)
- [PFRDA request on NPS D-Remit — Mint, October 13](https://www.livemint.com/economy/pfrda-seeks-upi-mdr-exemption-for-nps-contributions-11791863636686.html)
- [RBI account-aggregator remarks — The Times of India, October 15](https://timesofindia.indiatimes.com/business/india-business/rbi-cautions-account-aggregators-against-monetising-data/articleshow/134969096.cms)
- [Silent Mobile Verification for UPI — ETTelecom, October 15](https://telecom.economictimes.indiatimes.com/amp/news/devices/bureau-launches-silent-mobile-verification-for-upi-device-binding/134967005)
- [Fintech funding in January–September 2026 — Business Standard / Tracxn, October 13](https://www.business-standard.com/finance/news/fintech-funding-up-14-to-2-2-bn-in-jan-sep-deal-count-falls-41-tracxn-126101300252_1.html)
- [Paramotor Digital’s proposed IPO — The Hindu BusinessLine, October 15](https://www.thehindubusinessline.com/markets/paramotor-digital-files-for-1000-crore-ipo-with-sebi/article71586661.ece)
