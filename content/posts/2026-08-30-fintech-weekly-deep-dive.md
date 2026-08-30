---
title: "Fintech Weekly Deep Dive — UPI’s Second Decade: The Free Ride Ends | August 24–30, 2026"
date: 2026-08-30T09:00:00+05:30
draft: false
tags: ["Fintech", "Deep Dive", "Weekly", "Analysis", "UPI", "MDR", "Consumer Protection"]
categories: ["Weekly Deep Dive"]
description: "As UPI turns 10 with 13,000x growth, the system faces a trilemma: funding sustainability, consumer control over incoming payments, and privacy. The free ride is ending."
image: ""
---

# Fintech Weekly Deep Dive — UPI’s Second Decade: The Free Ride Ends | Week of August 24–30, 2026

## Executive Summary

UPI turned ten on August 25. The numbers are deservedly celebrated — 24,162 crore annual transactions, ₹314 lakh crore in value, 49% of all real-time payments globally, 741 banks live, 11 countries connected. But this week’s coverage of the anniversary coincided with three developments that, taken together, reveal the platform’s most consequential inflection point since demonetisation drove its initial adoption.

First, the Lok Sabha has passed the Taxation and Other Laws (Amendment) Bill, 2026, which amends the Payment and Settlement Systems Act to give the central government discretion to notify which digital payment modes can attract charges — formally laying the legal groundwork for a return of Merchant Discount Rate (MDR) on UPI. Second, the Allahabad High Court issued notice to the RBI, NPCI, and the Finance Ministry on a PIL seeking a mandatory “Accept/Decline” mechanism for incoming UPI credits, exposing a glaring gap in consumer agency. Third, NPCI confirmed it is working to mask phone numbers on UPI apps and make username-based Virtual Payment Addresses (VPAs) the default, a long-overdue privacy correction.

These are not isolated moves. They are the three legs of a single transformation: UPI is transitioning from a growth-at-all-costs public good to a mature payment infrastructure that must grapple with who pays, who controls, and who sees. The second decade will be defined by how India answers these questions.

## The Story in Depth

### Context: The Architecture of “Free”

UPI’s zero-MDR regime was introduced in January 2020, building on a policy bet that making merchant payments free would accelerate adoption beyond urban early adopters into the informal economy — street vendors, kirana stores, auto-rickshaw drivers, village mandis. The bet worked spectacularly. Annual volume surged from 25.5 billion transactions in FY 2019-20 to 241.6 billion in FY 2025-26, a nearly ten-fold increase in six years. P2M transactions, the primary target of the zero-MDR policy, now account for 63% of UPI’s total volume, with 86% of merchant transactions below ₹500.

But “free” was never actually free. The cost was borne by a patchwork of subsidies and cross-subsidies. The government’s incentive scheme for RuPay debit cards and low-value BHIM-UPI P2M transactions allocated ₹2,485 crore in FY 2023-24. That figure dropped to a Budget Estimate of just ₹437 crore for FY 2025-26 before being revised upward mid-year to ₹2,196 crore — a 403% upward revision that itself signals how poorly the initial estimate matched reality. For FY 2026-27, the allocation is ₹2,000 crore. PhonePe, which processes 48% of all UPI transactions, called the ₹2,000 crore figure “far short of what’s needed,” noting that the FY 2023-24 payout of ₹3,900 crore was itself insufficient to cover operational costs.

The government’s own Socio-Economic Impact Analysis of the Incentive Scheme, released during the Chintan Shivir 2026, found that digital transactions increased nearly 11 times during the scheme’s operation — but stopped short of recommending its continuation at the same scale, instead calling for a “studied approach” to transition toward a self-sustaining model.

### What Happened This Week

**The Legislative Foundation for MDR’s Return.** On August 4, the Lok Sabha passed the Taxation and Other Laws (Amendment) Bill, 2026, which includes a critical amendment to Section 26 of the Payment and Settlement Systems Act, 2007. The new provision gives the central government explicit discretion to determine which digital payment modes “shall not incur any charges.” The inversion is deliberate: rather than listing which modes can be charged, the government now has the power to exempt specific modes from charges — meaning everything else is implicitly chargeable. Finance Minister Nirmala Sitharaman has assured Parliament that end consumers and small merchants will not bear MDR, and that any charges would apply only to large merchants on high-value transactions (reportedly above ₹2,000, at 0.3–0.5%).

RBI Governor Sanjay Malhotra’s commentary this week was more direct. “Somebody must bear the cost,” he told reporters on August 5, adding that consumers may already be bearing UPI’s costs indirectly through the broader economy. “There are no charges currently. But there is a cost,” Malhotra said, framing the question as one of fiscal honesty rather than policy choice.

**The Accept/Decline PIL.** On August 24, a Division Bench of the Allahabad High Court’s Lucknow Bench issued notice to the RBI, NPCI, and the Union Finance Ministry on a PIL filed by advocate Anupriya Agarwal. The petition seeks a mandatory “Accept/Decline” mechanism for all incoming electronic credits, arguing that the complete absence of recipient consent undermines consumer autonomy and privacy.

The timing is not coincidental. India’s cyber-fraud epidemic has made the lack of recipient control a consumer-safety issue. Between 2021 and 2025, ₹53,000 crore was lost to cyber fraud; only ₹167 crore was recovered — a recovery rate of 0.31%. The government’s Centralised Cyber Fraud SOP 2026, issued by the Ministry of Home Affairs, created the CFCFRMS framework that can freeze accounts linked to suspected fraud. But the blunt instrument of account-freezing has produced its own victims: in July, the Delhi High Court ordered the de-freezing of a chhole-bhature vendor’s entire bank account (₹1.2 lakh balance) over a disputed incoming credit of ₹105. A Reddit thread titled “Why does UPI not have an option to accept/reject incoming payments?” went viral this week after a user described receiving an unsolicited ₹500 credit followed by an immediate callback demanding it be returned — a classic social-engineering precursor to fraud.

**Phone Number Masking.** Business Standard reported on July 29 that NPCI has asked UPI apps to mask phone numbers and make username-based VPAs the default for new users. The move addresses a long-standing privacy concern: UPI’s current design exposes the payer’s registered mobile number to the payee (and vice versa) during transaction initiation, creating a data-exposure surface that has been exploited for spam calls, phishing, and surveillance. The shift to VPA-first identity is part of a broader security overhaul that includes device binding, SMS-less onboarding, and biometric authentication via Aadhaar (rolled out from October 2025).

### Why It Matters

**The Sustainability Question is No Longer Theoretical.** The Bernstein analysis cited in the TechCrunch report quantifies the trade-off precisely: transactions above ₹2,000 account for only 4% of UPI’s volume but nearly 70% of its value. A 15–30 basis point MDR on that slice would generate ₹5,000–10,000 crore annually by FY 2028, per Jefferies. But this revenue would flow primarily to the top two PSPs — PhonePe (48% volume share) and Google Pay (33%) — reinforcing a duopoly that the India Fintech Foundation has already flagged to the government. NPCI’s 30% volume cap per app, designed to prevent exactly this concentration, has been effectively gamed by the market leaders’ first-mover advantages.

The political economy of MDR is treacherous. The government wants to signal fiscal responsibility while avoiding anything that looks like a “tax on digital payments” ahead of election cycles. Sitharaman’s assurance that consumers and small merchants are protected is designed to insulate the government from backlash — but the legislative change means the exemption can be narrowed at any future date without returning to Parliament.

**Consumer Agency is the Unaddressed Gap.** The Allahabad HC PIL names the exact asymmetry that makes UPI dangerous in its current form: the payer initiates, the platform processes, the payee’s account receives — with zero input from the payee at any stage. This design choice made sense in 2016 when UPI was a niche inter-bank transfer tool. In 2026, when 2,366 crore transactions hit accounts every month and cyber-fraud losses exceed ₹53,000 crore over four years, it is a liability. The UK’s APP Fraud Mandatory Reimbursement Framework (2024) and Singapore’s Shared Responsibility Framework offer templates, but India’s scale makes any retrofit exponentially harder. The Delhi High Court’s ₹105 vendor ruling shows the current system failing at the margins; a systemic accept/decline mechanism would address the structural problem.

**Privacy as a Second-Order Effect.** Phone number masking is a welcome move but arrives years late. Every UPI transaction over the past decade has potentially exposed the registered mobile numbers of both parties to the other’s UPI app, creating a massive, unconsented data trail. The Data Protection Act, 2023 provides a legal framework, but enforcement against data already exposed is retroactive and impractical. NPCI’s move to VPA-first identity is damage control, not prevention.

## Data & Metrics

- **24,162 crore** annual UPI transactions in FY 2025-26, up from 1.78 crore in FY 2016-17 (13,000x growth)
- **₹314 lakh crore** annual transaction value in FY 2025-26, up from ₹0.07 lakh crore (4,000x growth)
- **2,366 crore** monthly transactions in July 2026 (₹29.9 lakh crore value) — both records
- **49%** of all global real-time payment transactions (IMF/ACI Worldwide)
- **84%** share of India’s total digital payment transactions by volume
- **86%** of P2M UPI transactions are below ₹500
- **741** banks live on UPI, up from 21 at launch
- **11** countries with active UPI linkages
- **₹2,000 crore** FY 2026-27 budget allocation for UPI/RuPay incentives (vs. ₹2,196 crore revised FY 2025-26, and ₹3,900 crore actual FY 2023-24)
- **4%** of UPI transactions are above ₹2,000, but they represent **70%** of transaction value
- **₹53,000 crore** lost to cyber fraud (2021–2025), with only **₹167 crore** (0.31%) recovered
- **48%** PhonePe, **33%** Google Pay, **8%** Paytm — the top two control 81% of UPI volume

## Expert Views

RBI Governor Sanjay Malhotra: “There is a cost [to UPI transactions]. Someone has to bear it.” (August 5, 2026) — framing the MDR debate not as a policy choice but as an accounting reality.

Amrish Rau, CEO, Pine Labs: “For us to get to 90% penetration, and to take UPI global, startups, fintechs and banks will need to fund this expansion through continued investments in IT, innovation and cyber security.” — arguing that MDR on large merchants is the price of UPI’s continued growth.

PhonePe spokesperson (to Economic Times): “This allocation [of ₹2,000 crore] falls far short of what’s needed to build technical infrastructure, acquire consumers and merchants, drive education initiatives, and implement robust risk and fraud prevention systems for UPI.” — the largest UPI PSP signalling that government subsidies alone cannot sustain the network.

Finance Minister Nirmala Sitharaman: “UPI MDR is not to be borne by end users; it applies only to merchants.” — drawing the political red line that defines the MDR debate’s boundary.

Bernstein (brokerage): “Such an approach would preserve UPI’s consumer-friendly model while creating a meaningful new revenue pool for banks and payment companies.” — identifying the 4% volume / 70% value asymmetry as the policy’s natural target.

## Consumer Impact

**For the vast majority of users, nothing changes in the near term.** The 86% of merchant transactions below ₹500 and all P2P transfers remain zero-MDR. The political cost of touching small-merchant or consumer fees is too high for any government to absorb, and the legislative framework specifically preserves the exemption power.

**For high-value merchants**, a 0.3–0.5% MDR on transactions above ₹2,000 would be a new cost line. At current volumes, this affects roughly 4% of transactions but the merchants it hits — large retailers, e-commerce platforms, travel companies — are the ones most able to absorb it and most likely to negotiate volume-based discounts with their acquiring banks.

**The accept/decline question affects everyone.** The absence of recipient consent over incoming credits is the single largest unaddressed consumer vulnerability in UPI’s design. The ₹105 vendor whose account was frozen, the Reddit user who received an unsolicited ₹500 credit as a social-engineering lure — these are not edge cases. They are the predictable consequences of a system that treats the payee’s account as a passive receiving terminal rather than an active financial instrument. If the Allahabad HC PIL succeeds, every UPI user gains a meaningful new layer of control over their financial life.

**Privacy improvements are incremental but meaningful.** Phone number masking won’t retroactively erase a decade of data exposure, but for new and future users, it closes a glaring loophole. Combined with device binding and biometric authentication (now operational on both Android and iOS), UPI’s security posture is finally catching up to its scale.

## Looking Ahead

1. **MDR rate and threshold notification:** The legislation grants the power but defers the details. Watch for a government notification within 60–90 days specifying the ₹2,000 threshold, the MDR rate (0.3–0.5% is the working range), and the revenue-sharing formula among banks, NPCI, and PSPs.

2. **Allahabad HC PIL hearing:** The next hearing date will be the key milestone. If the court directs the RBI to frame accept/decline guidelines, it could reshape UPI’s core transaction flow — a far more consequential change than MDR.

3. **UPI-TIPS integration timeline:** The ECB’s decision to move to the “realisation phase” for linking Europe’s TIPS system with UPI is the most significant international development. No go-live date has been announced, but enterprises should expect 2027–2028. This creates a direct India-EU instant payment corridor that would make UPI’s current bilateral country linkages (Singapore, UAE, France, etc.) look like pilot projects.

4. **PhonePe’s $12 billion valuation and IPO prospects:** With 48% market share and MDR revenue potentially incoming, PhonePe’s path to profitability becomes clearer — and its IPO, when it comes, will be the most consequential fintech listing in Indian market history.

5. **Cyber-fraud recovery rates:** The 0.31% recovery rate on ₹53,000 crore in fraud losses is unsustainable. The I4C’s GRM and MRM portals are steps in the right direction, but until UPI builds in structural protections (like accept/decline), the fraud problem will scale with transaction volume.

UPI’s first decade was about getting to scale. The second decade is about paying for that scale — not just in rupees, but in privacy, security, and consumer agency. The anniversary celebrations were deserved. But the harder work starts now.

## Sources

- [PIB UPI 10th Anniversary Backgrounder](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2302664)
- [PIB UPI Factsheet — Key Statistics](https://www.pib.gov.in/FactsheetDetails.aspx?id=150962&NoteId=150962&ModuleId=16)
- [TechCrunch — India Moves to Give Its Instant Payments Network a Business Model](https://techcrunch.com/2026/08/04/india-moves-to-give-its-instant-payments-network-a-business-model/)
- [BBC — India Built the World’s Biggest Digital Payments Miracle. Now Comes the Bill](https://www.bbc.com/news/articles/c8xnwqe00v1o)
- [Business Standard — NPCI Plans to Mask Phone Numbers on UPI Apps](https://www.business-standard.com/india-news/npci-plans-to-mask-phone-numbers-on-upi-apps-to-boost-user-privacy-126072900602_1.html)
- [MediaNama — Allahabad HC Notice on UPI Accept/Decline PIL](https://www.medianama.com/2026/08/223-allahabad-high-court-digital-payments)
- [Economic Times — India’s UPI Miracle Has a Money Problem](https://m.economictimes.com/news/economy/policy/budget-2026-indias-upi-miracle-has-a-money-problem/articleshow/126560062.cms)
- [Economic Times — Union Budget 2026 Raises UPI, RuPay Incentives to ₹2,000 Crore](https://bfsi.economictimes.indiatimes.com/articles/union-budget-2026-govt-raises-upi-rupay-incentives-to-rs-2000-crore/127838699)
- [Business Standard — RBI Governor on UPI MDR](https://www.business-standard.com/economy/news/rbi-governor-upi-mdr-merchant-fee-someone-has-to-pay-126080500833_1.html)
- [New Indian Express — Monetize or Not: Government’s UPI Dilemma](https://www.newindianexpress.com/explainers/2026/Apr/18/monetize-or-not-governments-upi-dilemma)
- [ECB — Eurosystem Moves Forward on UPI-TIPS Connection](https://www.ecb.europa.eu/press/intro/news/html/ecb.mipnews251120.en.html)
- [Juspay — UPI-TIPS Linkage: A Game-Changer for Cross-Border Payments](https://juspay.io/blog/upi-tips-linkage-a-game-changer-for-cross-border-payments)
- [Moneycontrol — Banks, Fintechs, NPCI: Who Gets What When MDR Returns to UPI](https://www.moneycontrol.com/news/india/banks-fintechs-npci-who-gets-what-when-mdr-returns-to-upi-14013119.html)
- [ORF — Digital Public Infrastructure and the Future of Digital Payments: Lessons from Pix and UPI](https://www.orfonline.org/research/digital-public-infrastructure-and-the-future-of-digital-payments-lessons-from-pix-and-upi)
- [IMPRI — Scaling UPI: The Economics Behind NPCI’s New Operational Limits](https://www.impriindia.com/centres/center-for-ict-for-development/scaling-upi-the-economics-behind-npcis-new-operational-limits)
- [Entrackr — August Startup Funding Report](https://entrackr.com/report/monthly-funding-report/fintech-and-e-commerce-push-august-startup-funding-to-960-mn-9773541)
- [FinTech Futures — ECB Moves Forward with UPI-TIPS Integration](https://www.fintechfutures.com/instant-real-time-payments/ecb-moves-forward-with-upi-tips-integration)
