---
title: "DPI Weekly Deep Dive — UPI Sustainability at Crossroads | Week of March 9-15, 2026"
date: 2026-03-15T09:00:00+05:30
draft: false
tags: ["DPI", "Digital India", "UPI", "Deep Dive", "Weekly", "Analysis"]
categories: ["Weekly Deep Dive"]
description: "2000-word analysis of UPI sustainability debate and proposed interchange fees in India's Digital Public Infrastructure"
image: ""
---

# DPI Weekly Deep Dive — UPI Sustainability at Crossroads | Week of March 9-15, 2026

## Executive Summary

India's Unified Payments Interface (UPI), the world's largest real-time payment platform processing over 21.7 billion transactions monthly worth ₹28.33 lakh crore, faces an unprecedented sustainability challenge. This week, a Parliamentary Standing Committee on Finance recommended exploring a tiered charging structure that would introduce interchange fees for larger merchants while preserving free transactions for small vendors and peer-to-peer payments. Simultaneously, NPCI announced revised TPAP and PSP fee structures for RuPay credit card transactions on UPI, effective April 1, 2026. These developments mark a critical inflection point in India's digital public infrastructure journey, forcing policymakers to balance financial inclusion objectives with ecosystem viability. The proposed changes draw comparisons to Brazil's Pix and China's digital payment systems, where hybrid revenue models have sustained massive transaction volumes without compromising adoption.

## The Story in Depth

### Context: UPI's Extraordinary Growth Trajectory

The Unified Payments Interface has transformed from a novel experiment in 2016 into the backbone of India's digital economy. As of January 2026, UPI processes approximately 698 million transactions daily, integrating 691 banks into a unified network that accounts for roughly 49% of all global real-time digital payments. [^1] The platform has achieved what no other payment system in history has accomplished: enabling instant, interoperable, zero-cost transactions at national scale across a population of over 1.4 billion people.

The success of UPI extends far beyond payment volumes. The platform has catalyzed financial inclusion by enabling 491 million individuals and 65 million merchants to participate in the digital economy. [^2] Street vendors in Tier-III cities now accept digital payments, small businesses have access to formal payment rails, and consumer behavior has fundamentally shifted toward digital transactions. The ecosystem has also spawned innovative financial products including UPI-based credit, insurance premiums, and investment subscriptions.

However, this extraordinary growth has come with a hidden cost structure that is now demanding attention. Industry estimates suggest that stakeholders collectively incur approximately ₹2 per UPI transaction in operational costs, including technology infrastructure, switching systems, settlement networks, fraud monitoring, server maintenance, and cybersecurity systems. [^3] While this amount appears negligible individually, the sheer scale of 228 billion annual transactions transforms these micro-costs into a significant aggregate burden.

### What Happened This Week

The most significant development this week centers on the Parliamentary Standing Committee on Finance's recommendation to explore a tiered charging structure for UPI transactions. The committee's proposal suggests maintaining free services for small merchants and street vendors while introducing transaction fees for larger merchants and banks to ensure long-term ecosystem sustainability. [^4]

This recommendation emerges from growing concerns about the zero-merchant discount rate (zero-MDR) policy introduced in 2020, which eliminated processing fees on most UPI payments to accelerate digital adoption. While this policy drove rapid uptake, it also removed the primary revenue stream for banks and payment processors who must bear operational costs without corresponding fee income.

Separately, NPCI announced revisions to Third Party Application Provider (TPAP) and Payment Service Provider (PSP) fees for RuPay credit card transactions on UPI, effective April 1, 2026. Under the new structure, TPAP fees for consumer payments through RuPay credit cards on UPI have been reduced from 8 basis points to 6 basis points for non-industry categories, and from 4 basis points to 3 basis points for industry categories. [^5] Notably, these changes apply only to consumer-facing app revenue and do not affect merchant MDR, leaving the fundamental zero-MDR structure intact for now.

Paytm, in its stock exchange disclosure, stated that the financial impact of these fee revisions would be immaterial for the company, as the bulk of its payments revenue comes from merchant transactions with margins above 4 basis points. [^6]

### Why It Matters

The sustainability debate carries profound implications for India's digital public infrastructure. If transaction volumes continue to grow while the fee structure remains unchanged, the cumulative cost burden could become increasingly difficult for banks and fintech firms to absorb. Industry analysts estimate that total monthly operational costs already run into thousands of crores when infrastructure, settlement systems, and technology maintenance are included.

The stakes extend beyond individual institutions. UPI's success has made it a template for digital public infrastructure globally, with countries including Brazil, Sri Lanka, Nepal, and several others expressing interest in adopting similar frameworks. Any fundamental instability in the Indian model would send ripples across the global DPI landscape.

Furthermore, the platform's role in Direct Benefit Transfers (DBT) has made it critical to government welfare delivery. Over ₹49.09 lakh crore has been transferred through DBT by January 2026, with the Public Financial Management System (PFMS) helping eliminate fake beneficiaries and reduce leakages amounting to approximately ₹4.31 lakh crore in savings between 2015-2024. [^7] Sustainability concerns could potentially impact this crucial welfare distribution mechanism.

## Technical Deep Dive

### UPI Switch Architecture

Understanding UPI's technical infrastructure illuminates why operational costs accumulate at such scale. A UPI Switch serves as the core transaction processing and routing engine connecting banks, PSPs, and fintech platforms to NPCI's network. [^8]

The architecture comprises three interconnected layers:

**Integration Layer**: Acts as the secure gateway between external systems and the switch core, exposing standardized REST-based APIs with throttling, validation, and authentication controls. This layer handles requests from mobile apps, merchant systems, and internal banking modules.

**Orchestration and Routing Layer**: The operational heart that validates message formats, performs VPA checks, initiates authentication flows, and routes transactions to NPCI and counterparty banks. During peak loads—festive surges or flash sales—this layer dynamically redistributes processing across nodes to prevent bottlenecks through horizontal scaling.

**Security and Compliance Layer**: Manages encryption, key management, and audit logging. Hardware Security Modules (HSM) handle PIN encryption, AES-256 protects data in transit and at rest, and Role-Based Access Control ensures authorized personnel access only.

The entire transaction cycle—from initiation through NPCI routing, issuer authentication, core banking debit, merchant credit, and settlement—completes within milliseconds. For banks and fintechs, those milliseconds determine SLA performance, reconciliation accuracy, and partner confidence.

### Cost Structure Breakdown

Banks incur roughly 3-4 basis points per transaction in operational costs, including network switching charges and technology service provider fees. [^3] While the government has introduced incentive schemes for low-value transactions, industry participants report that subsidies cover only a portion of actual operational costs. The widening gap between zero revenue and positive costs creates the sustainability challenge.

## Government Perspective

The government faces a delicate balancing act. On one hand, free UPI transactions have been instrumental in achieving unprecedented financial inclusion and digital adoption. The Jan Dhan accounts, combined with UPI accessibility, have brought millions into the formal banking system. Any perception of "charging for free services" could generate political backlash.

On the other hand, maintaining an increasingly expensive infrastructure without sustainable funding threatens long-term viability. The Parliamentary Committee's recommendation for tiered charges—free for small merchants, fees for large merchants—represents an attempt to preserve inclusion while introducing sustainability.

Finance Ministry officials have indicated willingness to continue government incentives for low-value transactions while encouraging industry to develop sustainable business models. The RBI has confirmed that UPI payments will continue remaining free for users, preserving seamless peer-to-peer transactions without charges. [^9]

## Citizen Impact

For ordinary Indians, the proposed changes carry mixed implications. Small merchants and street vendors—already enjoying free UPI transactions—would likely see no changes under the tiered structure. These participants, who have benefited most from digital payment adoption, would continue receiving free services.

Larger merchants and businesses could face new transaction costs, potentially 0.2-0.3% of transaction value according to some proposals. [^3] However, these charges remain modest compared to traditional card networks, and businesses may absorb them or pass them to consumers minimally.

For consumers making P2P transfers or paying small merchants, UPI would remain free. The RBI has explicitly confirmed this. Only specific merchant categories might see new charges.

The financial inclusion story remains intact: the 491 million individuals and 65 million merchants currently using UPI would continue accessing the platform without direct charges for basic transactions.

## Global Context

Comparing UPI with other major real-time payment systems reveals interesting sustainability approaches:

**Brazil's Pix**: Provides free transfers for individuals but charges merchants small processing fees typically around 0.22% of transactions—significantly lower than traditional card networks while generating revenue for participating institutions. [^3]

**China's Alipay and WeChat Pay**: Merchants pay transaction fees ranging from roughly 0.6% to 1% depending on services, financing extensive infrastructure, security systems, and consumer features. [^3]

**India's Current Approach**: Treats UPI as public digital infrastructure similar to roads or telecommunications, designed to maximize inclusion rather than generate profit. This remains unusually generous compared to global peers.

The proposed tiered model would align India more closely with Brazil's approach while preserving core inclusion objectives—a middle path that preserves public good characteristics while introducing commercial sustainability.

## Looking Ahead

Several developments warrant monitoring in coming weeks and months:

1. **Final Policy Decisions**: The Finance Ministry will likely deliberate on the Parliamentary Committee's recommendations, potentially announcing a concrete implementation timeline for tiered charging.

2. **Industry Response**: Banks and fintech companies will need to adjust business models, potentially investing more aggressively in value-added services to compensate for any new fee structures.

3. **Merchant Adoption Impact**: Monitoring whether introduction of merchant fees affects adoption rates, particularly among larger retail chains considering digital payment acceptance.

4. **Technology Investment**: Sustained investment in cybersecurity and infrastructure remains critical as transaction volumes continue climbing toward the 1 billion daily mark projected by industry experts.

5. **International Expansion**: Countries watching India's approach—including those already adopting UPI-like systems—will adjust their own sustainability models based on India's policy direction.

The UPI sustainability debate represents not merely a pricing discussion but a fundamental question about the future of digital public infrastructure: how to maintain public good characteristics while ensuring commercial viability at massive scale.

---

## Sources

- [^1]: PIB Press Note - https://www.pib.gov.in/PressNoteDetails.aspx?NoteId=154912&ModuleId=3&reg=3&lang=2
- [^2]: Economic Times - https://economictimes.indiatimes.com/industry/banking/finance/upi-payments-in-india-register-steady-growth-yoy-in-november-2025/articleshow/125671583.cms
- [^3]: ETBFSI - https://bfsi.economictimes.indiatimes.com/amp/articles/the-future-of-upi-can-indias-digital-payment-system-stay-sustainable/129567478
- [^4]: Outlook Money - https://www.facebook.com/outlookmoney/posts/is-the-era-of-free-upi-payments-coming-to-an-end-a-parliamentary-standing-commit/1335810131912640/
- [^5]: Paytm Stock Exchange Disclosure - https://paytm.com/document/ir/stock-exchange-submissions/fy2025-26/mar/Disclosure_Reg_30_LODR_11_Mar_2026.pdf
- [^6]: Financial Express - https://www.financialexpress.com/business/industry/paytm-why-npcis-revised-rupay-credit-card-upi-fees-has-zero-impact-on-revenue/4169054/lite/
- [^7]: GS Times - https://www.gstimes.in/the-rise-of-indias-dpi-stack/
- [^8]: IndiNXT - https://www.indinxt.com/blog/2026/03/12/what-is-a-upi-switch/
- [^9]: DD News - https://www.facebook.com/DDNews/posts/watch-india-is-moving-to-the-next-level-of-development-building-next-generation-/1358367926318092/
