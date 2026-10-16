---
title: "Fintech Deep Dive — Friday | October 16, 2026"
date: 2026-10-16T08:30:00+05:30
draft: false
tags: ["Fintech", "Deep Dive", "Theme: Friday"]
categories: ["Deep Dive"]
description: "Weekly analysis of Friday theme in Indian fintech"
---

# Fintech Deep Dive — Friday | October 16, 2026

**Policy & regulation | October 9–16, 2026**

## Executive summary

India’s proposed UPI merchant discount rate (MDR) did not arrive quietly. In the week it was due to begin, the National Payments Corporation of India (NPCI) pushed its start until after Diwali; the pension regulator asked that a particular kind of savings transfer be treated as person-to-person rather than merchant activity; and legal commentators questioned how a ban on passing the charge to customers would work in practice. Together, these are not three unrelated objections. They expose the harder design problem: who pays to keep a widely used payment rail reliable, and how do users know that a new charge is correctly classified and fairly enforced?

A clarification on scope: the MDR schedule was not an RBI circular announced this week. It is a payment-system pricing framework communicated through NPCI and the UPI and Services Steering Committee, under the Payment and Settlement Systems Act framework. On October 13, NPCI deferred the planned October 15 start. As of October 16, there is no new implementation date. The proposed schedule below is therefore policy context—not a fee that consumers or merchants should assume is already live.

## 1. NPCI’s Diwali pause is a reprieve, not a reversal

The framework was set to charge 0.4% on specified person-to-merchant (P2M) UPI payments above ₹2,000, with the fee capped at ₹300 on transactions of ₹75,000 or more. Some essential or thin-margin categories—including railways, telecom, insurance, fuel and agricultural inputs—were assigned a flat ₹5 charge; capital-market payments, including mutual funds and stockbrokers, were assigned 0.02%, also capped at ₹300. Person-to-person transfers, small payments and merchants covered by the P2PM exemption were to remain free. The government estimated that roughly 96% of P2M transactions would be unaffected.

On October 13, NPCI said its UPI and Services Steering Committee had decided that MDR on “select” P2M transactions would begin “immediately post Diwali”, on a date to be notified separately. Diwali falls on November 8 this year. This is a delay of at least several weeks, not cancellation: the committee left the rates and exemptions intact in its announcement and did not set a replacement date. The stated reason was the festive season. The decision also followed objections from trader unions, including the Confederation of All India Traders, which welcomed the delay and argued that an added cost could burden traders and MSMEs during a high-volume sales period.

The timing matters. Merchants had prepared for October 15; customers were hearing that “UPI charges” were imminent. The postponement avoids an immediate checkout shock but leaves acquirers and businesses unsure whether to absorb the fee or reconfigure checkout. It also demands an answer: what evidence would justify restarting the schedule?

These exemptions mean this is not a blanket UPI tax: P2P transfers are not shop payments, and not every merchant transaction is charged. Still, payment value is a poor proxy for ability to pay: a ₹3,000 basket at a large chain differs from the same basket at a thin-margin independent shop. Before restarting, the committee should publish categories, calculation rules, exemptions and date in one searchable notice, not leave users to infer them from QR stickers or app alerts.

[Mint’s report on the NPCI postponement](https://www.livemint.com/money/upi-transactions-above-2-000-0-4-mdr-deferred-until-after-diwali-says-npci-11791878899700.html) and [TechCrunch’s account of retailer pushback](https://techcrunch.com/2026/10/13/india-delays-digital-payments-fee-rollout-amid-retailer-pushback/) document the change and the dispute around it.

## 2. PFRDA’s NPS request tests what “merchant payment” means

On October 13, the Pension Fund Regulatory and Development Authority (PFRDA) confirmed to *Mint* that it had written to the Department of Financial Services asking for UPI contributions made through NPS Direct Remittance (D-Remit) to be treated as P2P transfers and kept outside the MDR framework. The regulator’s argument is intuitive: when a subscriber moves their own money from a bank account into their own retirement account, there may be no ordinary merchant sale at the other end. The payment is a contribution to long-term savings, not a purchase of goods.

That distinction matters because the proposed rate is not uniform. Capital-market-related merchant payments were assigned a lower 0.02% MDR, while qualifying P2M transactions generally faced 0.4%. If D-Remit is classified as a merchant payment, a voluntary contribution above ₹2,000 could potentially incur a charge depending on how the payment is routed and categorized. The issue is consequential at scale: *Mint* reported that NPS had 23.4 million subscribers and assets of ₹17.36 trillion. Those totals do not mean all subscribers will pay a fee; the question is narrower—whether a particular UPI route into a pension account is recognized as a payment to a merchant.

D-Remit uses a dedicated virtual account for Tier I and Tier II contributions; UPI contributions date to 2022. That can look merchant-like to a payment network even when the purpose is a person’s own savings. Rules should classify by purpose as well as technical settlement path; otherwise a settlement label silently decides whether pension savers pay.

PFRDA’s letter was a request, not an exemption already granted. *Mint* said the Finance Ministry, DFS, the Finance Minister’s Office and NPCI had not responded by publication. The October 13 postponement means the proposal was not due to take effect on October 15 in any case, but it does not resolve the D-Remit question. Before a new date is announced, authorities should publish the decision, its legal basis, the treatment of contributions made through other channels, and whether any wrongly collected fees would be refunded. A narrow, purpose-based exclusion for transfers into a person’s own regulated retirement account would be more defensible than asking savers to discover the answer after a deduction appears.

[Read *Mint*’s report on PFRDA’s request](https://www.livemint.com/economy/pfrda-seeks-upi-mdr-exemption-for-nps-contributions-11791863636686.html).

## 3. “The merchant pays” is not enough protection for the customer

A separate *Mint* explainer published on October 13 asked the practical question behind the framework: if MDR is charged to a merchant, can that merchant add it to the customer’s bill? The Finance Ministry’s position, as reported by *Mint*, is that merchants cannot pass the charge on. The report also cites clause 7.5 of NPCI’s September 18 circular, which requires the institution handling a merchant’s UPI payments to prevent surcharges. Lawyers quoted in the article said that the restriction applies even where MDR is permitted.

That prohibition is useful, but a rule is only as protective as its enforcement path. *Mint* reported no single surcharge-specific process spelling out who decides a complaint, by when, and how a refund follows. The acquiring bank or payment aggregator may have the first operational role, but customers should not have to identify the merchant’s acquiring chain or distinguish a lawful general service fee from a UPI-only surcharge.

For consumers, the practical safeguards are basic: ask for an itemised bill, keep the transaction reference and payment confirmation, and record whether the same charge applies to other payment methods. A fee explicitly added only because a customer chose UPI is different from a disclosed price or service charge applied consistently across payment methods. If a UPI-linked surcharge is imposed, the merchant should be asked to reverse it; the customer should also complain through the payment app or bank and preserve the invoice and transaction ID. That is guidance for preserving evidence, not a guarantee that the refund route is already uniform.

The policy fix should be more than another general statement that surcharges are prohibited. Before implementation, NPCI and the Finance Ministry should identify the accountable first-contact institution, set a complaint and refund deadline, require acquirers to report surcharge complaints, and publish enforcement outcomes. A small, visible surcharge can be a deterrent to adoption even if the fee is formally borne by the merchant. If the new MDR is meant to finance a public-scale network, the framework must not make customers pay twice—once through indirect price increases and again through a confusing, ineffective complaint process.

[*Mint*’s consumer explainer on UPI charges and surcharge enforcement](https://www.livemint.com/industry/upi-mdr-digital-payments-india-merchants-fee-customer-payments/amp-11791831657458.html) sets out the dispute and the gaps lawyers identified.

## 4. UPI needs a cost model—but the bill cannot be arbitrary

The week’s debate also revived a legitimate question: can a payments network of this size remain dependable if its users pay nothing directly? In an October 13 opinion piece, economists Atul Mehta and Charan Singh noted that UPI processed 24.51 billion transactions worth ₹29.82 trillion in August, citing NPCI data. They contrasted government support of about ₹8,730 crore over FY2022–FY2025 with an industry estimate of roughly ₹20,700 crore in annual UPI operating costs cited by the Parliamentary Standing Committee on Finance, and a ₹2,000 crore allocation in the FY2026–27 Budget. These are not audited, like-for-like numbers: the cost figure is an industry estimate, and the support total and annual estimate cover different periods. But the mismatch is a clear reason to demand transparent accounting, not a reason to assume any proposed rate is automatically justified.

The case for a contribution is real. UPI needs bank and payment infrastructure, resilience, fraud controls, cybersecurity and continued acceptance beyond large cities. Public subsidy has helped build adoption; indefinitely suppressing all pricing could leave providers underfunded or make public budgets carry the entire bill. Yet a transaction fee can also change behavior. Merchants may absorb it, alter discounts, encourage another payment method or raise prices broadly. The legal payer and the person bearing the economic cost are not necessarily the same.

That is why the proposed charge should be judged on evidence: What costs are eligible for recovery? How is revenue divided among banks, payment service providers and apps? What share funds security and resilience rather than customer acquisition? How will fees be reviewed if volumes, fraud costs or service quality change? Without audited cost categories and a public distribution formula, users cannot tell whether MDR is cost recovery or simply a new revenue pool. And because the largest consumer-facing apps have strong network effects, the allocation rules could influence competition as well as infrastructure spending.

A sound settlement would protect P2P transfers and genuinely small merchants, clarify special cases such as NPS D-Remit, and preserve the ban on UPI-only surcharges with a workable refund channel. For the charged categories, it would publish the cost basis, revenue use, monitoring metrics and a scheduled review. The measure of success should not be how much MDR is collected; it should be whether reliability, fraud response and merchant acceptance improve without pushing vulnerable users back toward cash or quietly making digital payments more expensive.

[Mehta and Singh’s October 13 analysis](https://www.livemint.com/opinion/online-views/upi-mdr-charges-new-rules-merchant-discount-rate-11791823504548.html) lays out the sustainability argument and its trade-offs; [NPCI’s UPI statistics page](https://www.npci.org.in/product/ecosystem-statistics/upi) is the underlying public data source.

## What to watch next

As of October 16, the October 15 start is postponed, not rescinded. The next meaningful signals are a dated NPCI notice, a published answer to PFRDA on D-Remit, and clear instructions on preventing and refunding merchant surcharges. The central regulatory test is whether India can fund UPI’s operational resilience while keeping rules legible to the people who use it. “Free” and “sustainable” are not opposites; opaque classification and unreviewable pricing are the avoidable risks.

## Sources

- [Mint: NPCI defers the MDR rollout until after Diwali](https://www.livemint.com/money/upi-transactions-above-2-000-0-4-mdr-deferred-until-after-diwali-says-npci-11791878899700.html)
- [TechCrunch: retailer pushback and the postponed fee](https://techcrunch.com/2026/10/13/india-delays-digital-payments-fee-rollout-amid-retailer-pushback/)
- [Mint: PFRDA seeks an NPS D-Remit exemption](https://www.livemint.com/economy/pfrda-seeks-upi-mdr-exemption-for-nps-contributions-11791863636686.html)
- [Mint: consumer surcharge rules and complaint gaps](https://www.livemint.com/industry/upi-mdr-digital-payments-india-merchants-fee-customer-payments/amp-11791831657458.html)
- [Mint: economists on UPI’s cost and pricing model](https://www.livemint.com/opinion/online-views/upi-mdr-charges-new-rules-merchant-discount-rate-11791823504548.html)
- [NPCI: UPI ecosystem statistics](https://www.npci.org.in/product/ecosystem-statistics/upi)
