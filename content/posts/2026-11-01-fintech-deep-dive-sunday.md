---
title: "Fintech Deep Dive — Sunday | November 01, 2026"
date: 2026-11-01T08:30:00+05:30
draft: false
tags: ["Fintech", "Deep Dive", "Theme: Sunday"]
categories: ["Deep Dive"]
description: "Weekly analysis of Sunday theme in Indian fintech"
---

# Fintech Deep Dive — Sunday | November 01, 2026

*Weekly review | Developments reported October 25–31, 2026*

The week India's fintech quarter came due. Three listed fintechs — Paytm, Pine Labs and PB Fintech — reported September-quarter results in the same seven days, and for once the numbers did the arguing for them: profits everywhere, in three different business models. The same week, investigators revealed that roughly ₹300 crore had been siphoned out of small NBFCs through their own plumbing, UPI completed its first fortnight under merchant fees with PhonePe's CEO campaigning loudly for more of them, the Supreme Court drew a compensation line for digital-arrest victims, and the RBI opened a sovereign data centre and an e₹ sandbox. Here are the five stories that will shape December.

## 1. Earnings week: the profitable-fintech quarter is now a pattern

Paytm's parent One 97 Communications reported a net profit of about ₹226 crore for Q2 FY27, up nearly tenfold from ₹21 crore a year ago, on operating revenue of ₹2,648 crore, up 28% — its sixth consecutive profitable quarter. EBITDA rose 90% to a record ₹270 crore, crossing 10% margin for the first time; payment services revenue grew 25% to ₹1,434 crore, subscription merchants reached 1.64 crore (up 27 lakh year-on-year), and the company said its UPI gross transaction value is growing at more than double the industry rate.[^1][^2] Shares got a further fillip from Bernstein issuing its first Paytm price target above the IPO price.[^2] The caveats are in the guidance: Paytm expects Q3 contribution margin to decline on materially higher default-loss-guarantee costs and a festive-season shift toward card processing, and it is still spending ₹400 crore a quarter on payment devices.[^2]

Pine Labs, the merchant-commerce platform, posted a 543% jump in net profit to ₹38.6 crore, with revenue up 24% to ₹806 crore — a five-quarter high — and EBITDA up 68% to ₹126 crore (15.6% margin). It now processes around 25 million transactions a day (up 22%), with online payments up more than 45% and gross transaction value up 140%; the stock rose 7% on results day.[^3][^4] Quieter but strategically louder: its Setu unit received RBI approval to acquire account aggregator Agya Technologies, consolidating consent-based data infrastructure into a listed payments company.[^5]

PB Fintech, the Policybazaar parent, reported net profit of ₹192 crore, up 43%, on operating revenue of ₹2,178 crore, up 35%. Total insurance premium rose 38% to ₹9,385 crore, led by 46% growth in new health insurance premium; core renewal and trail revenue hit an annualised run-rate of ₹1,153 crore, up 52%. Since listing, revenue has compounded at 51% annually.[^6][^7]

Analysis: three different models — payments-led, merchant-platform, regulated distribution — printed profits simultaneously, which suggests the sector's cost cuts and monetisation have genuinely stuck rather than belong to one anomalous balance sheet. But each earnings report carries its regulatory shadow in the footnotes. Paytm's Q3 warning is an artifact of distributing credit through payments; Pine Labs' data-infrastructure acquisition will live or die by regulator appetite; and PB Fintech's strongest quarter lands just as the insurance regulator weighs caps on distributor commissions — the single biggest threat to its model, flagged alongside its results.[^8] Momentum and exposure are now the same story.

## 2. ₹300 crore walked out of small NBFCs — the API layer is the crime scene

The Economic Times reported on October 29 that an estimated ₹300 crore has been siphoned from non-banking financial companies, mostly smaller lenders, over roughly two months, with nearly 150 complaints or FIRs filed — about 30 in Mumbai, over 25 in Delhi, 15–16 in Chennai — against a backdrop of 8,502 registered NBFCs. Investigators told the paper the attacks pair Chinese AI toolkits (Artex, CyberStrike) with open-source models, and the CyberStrike platform has been identified in completed probes.[^9][^10]

The mechanics matter more than the totals. In one police complaint reviewed by Reuters, two Mumbai NBFCs lost about $2 million through more than 700 unauthorised transfers on October 8–9 after hackers compromised the API connection used to send loan-disbursal instructions to ICICI Bank — the criminals moved money through a channel the banks themselves trusted.[^11][^12] That came alongside the SBI confirmation that data of 3,897 customers had surfaced on the dark web as part of a 375,000-record dataset, with customer advisories going out only on October 30.[^9][^13]

The regulatory response was unusually fast and unusually blunt. An October 19 RBI advisory told regulated entities to treat their technology environments as compromised until forensically cleared; the central bank has since asked lenders for proof of cyber compliance, API-vulnerability reviews and AI-risk readiness, with one source telling Reuters that smaller lenders and their vendors are viewed as "softer targets."[^11][^12] CERT-In and CSIRT-Fin had flagged attack campaigns against NBFCs, digital lenders and payment providers on October 9; CERT-In followed on October 15 with an advisory on AI agents exceeding their assigned authorisations, and ran a drill on October 27 with over 300 officials from more than 55 financial institutions.[^10][^13]

Analysis: India's fintech architecture is a mesh of bank–NBFC–fintech APIs, and this week established that attackers no longer breach the fortress — they borrow a valid gate key from the weakest participant and walk through. The RBI's "treat everything as compromised" posture is the right read of that reality. The disclosure gap is the scandal in waiting: the DPDP Act's detailed breach-reporting obligations (the 72-hour report to the Data Protection Board) take effect only on May 13, 2027, so the public record of these NBFC attacks will stay patchy for months.[^13] Consumers are downstream of all of it — the loan books and KYC files sitting on the soft targets are theirs even when the immediate theft is funds.

## 3. UPI's money question: fees are live, the cap is coming, and PhonePe said the quiet part

The new UPI merchant-discount-rate regime completed its first full fortnight. From October 15, eligible person-to-merchant transactions above ₹2,000 carry a 0.4% MDR, capped at ₹300 for payments of ₹75,000 or more; specified sectors (railways, telecom, insurance, fuel, agricultural inputs) pay a flat ₹5; capital-market transactions attract 0.02%; person-to-person payments and small-merchant transactions stay free, and the government has been at pains to clarify customers pay nothing.[^14] Mid-October reports that the rollout might slip to January 2027 amid trader pushback proved wrong — it went ahead on schedule — but the uncertainty has kept payments stocks jumpy, with Paytm, MobiKwik and Pine Labs at one point falling as much as 6.5% on rollout confusion.[^15][^16]

Into that nervousness walked PhonePe CEO Sameer Nigam at the Business Standard BFSI Insight Summit, arguing MDR is vital to sustain UPI's growth as he laid out a target of a billion UPI users over the next decade. On NPCI's 30% market-share cap — effective December 2026, a rule written six years ago amid WhatsApp's entry into UPI — Nigam pointed out that more than 100 third-party UPI apps now operate, insisted his market share isn't deterring investment, and said that if ordered to stop onboarding customers in December he "would protest but comply."[^17]

Analysis: the funding model of India's payment system is flipping from government incentive to merchant pays, and the numbers explain why: the FY27 budget provides ₹2,000 crore for RuPay debit and low-value BHIM-UPI incentives against a Standing-Committee-cited industry operating cost of ₹20,700 crore.[^14] December now stacks two stress tests: the 30% cap lands on the market's largest apps in the middle of the first festive quarter where merchants above the threshold are paying for UPI at all. Watch large-ticket UPI volumes — if they bend, the MDR-vs-inclusion trade-off moves from op-ed pages to NPCI dashboards.

## 4. RBI's infrastructure week: a sovereign data centre and an open e₹

On October 25, the Prime Minister inaugurated the RBI's ₹169-crore Data Centre and Cyber Security Training Institute at Info Valley-II in Jatni, Bhubaneswar — a campus that will host the RTGS and NEFT settlement systems. Governor Sanjay Malhotra framed the security doctrine plainly: "any system that is not secure is incapable of winning public trust," listing the RBI's frameworks for IT governance, cyber resilience, outsourcing, third-party risk and digital payment security. Finance Minister Nirmala Sitharaman used the same stage to declare UPI the world's largest real-time payment system, handling over 2,400 crore transactions a month — nearly 80 crore payments a day.[^18][^19]

The same week, the RBI launched a retail sandbox for its central bank digital currency, enabling fintech firms to develop and test on the digital rupee rather than merely receive it through bank wallets.[^20]

Analysis: the scaling question for Indian payments is settled; the resilience question is not. At 80 crore payments a day, even a short outage touches tens of millions of people, which is exactly why hardened sovereign infrastructure for the settlement core — plus a dedicated cyber-talent pipeline — is the regulator planning around its own single points of failure. The e₹ sandbox is the more consequential shift for builders: after three years of a closed, bank-distributed pilot, the RBI is letting fintechs build on programmable central-bank money. Whether the e₹ finds consumers will depend on use cases UPI doesn't already serve — and that bar keeps rising.

## 5. The rest of the week, briefly

The Supreme Court's digital-arrest order (October 29) deserves more than a bullet — a CJI Surya Kant bench directed that the RBI's pending KYC Amendment Directions must mandate financial institutions to indemnify fraud victims "not less than equivalent to the amount lost" where institutional due diligence failed, with the rules to be notified by November 30 and operationalised by December 31 — and Saturday's issue carried the full analysis.[^21][^22] In funding, it was a thin week for venture: early-stage Indian startups raised $72.25 million across 24 deals, with healthtech's Cent ($15 million) the largest cheque.[^23] The fintech sliver was Mochatrade's $5.5 million seed from CoinFund, Coinbase Ventures, Y Combinator and Pioneer Fund for rupee-denominated trading in tokenised US equities — notable chiefly because it operates as an FIU-IND-registered virtual-digit-asset service provider, testing the outer edge of what Indian retail can legally reach.[^24] And the quarter's capital-markets backdrop was strong: EY-IVCA counted $17.1 billion of PE/VC investment across 348 deals in Q3, up 46% year-on-year, with financial services leading exit value at $2.8 billion across 21 exits.[^25]

## The week ahead

November 30 is the date to circle: the RBI's KYC amendments are due for notification that day, with the Supreme Court returning to the matter. December 31 brings operationalisation; sometime in December, the NPCI market-share cap bites. In between, the first festive-season data under merchant MDR will tell us whether UPI's pricing experiment bent demand — or whether 80 crore daily payments simply absorbed a new line item.

[^1]: https://www.tradingview.com/news/moodys:50b2c6c234163:0-paytm-q2-fy27-profit-rises-over-10-fold-to-rs-225-crore-revenue-grows-28-to-rs-2-648-crore
[^2]: https://www.cnbctv18.com/market/stocks/paytm-q2-results-net-profit-jumps-over-10-fold-to-%E2%82%B9226-crore-revenue-surges-29-20019761.htm
[^3]: https://m.economictimes.com/markets/stocks/news/pine-labs-shares-jump-7-as-q2-net-profit-soars-543-yoy-to-rs-39-crore/articleshow/135298034.cms
[^4]: https://www.businessworld.in/article/pine-labs-q2-profit-rises-over-sixfold-to-rs-39-cr-revenue-grows-24-631098
[^5]: https://m.economictimes.com/tech/newsletters/tech-top-5/cyberattacks-hit-nbfcs-pine-labs-q2-profit-zooms/articleshow/135314211.cms
[^6]: https://www.ndtvprofit.com/markets/pb-fintech-q2-results-net-profit-rises-43-to-rs-193-crore-insurance-premium-jumps-38-12259322
[^7]: https://www.bwdisrupt.com/article/pb-fintech-q2-net-profit-rises-42-5-to-rs-192-4-cr-revenue-grows-35-631394
[^8]: https://www.moneycontrol.com/technology/pb-fintech-s-net-profit-rises-43-to-rs-192-crore-in-q2-revenue-up-35-to-rs-2-178-crore-article-14064621.html
[^9]: https://m.economictimes.com/industry/banking/finance/ai-powered-cyberattacks-siphon-300-crore-from-small-nbfcs-in-two-months/articleshow/135278215.cms
[^10]: https://www.moneycontrol.com/news/business/rs-300-crore-stolen-from-small-nbfcs-in-cyberattacks-officials-flag-jamtara-style-fraud-risk-14063062.html
[^11]: https://www.indiatoday.in/business/story/rbi-cybersecurity-checks-banks-nfbc-api-vulnerabilities-ai-risks-3028543-2026-10-30
[^12]: https://bfsi.economictimes.indiatimes.com/articles/cybersecurity-becomes-a-balance-sheet-risk-for-lenders-as-breaches-rise/135378116
[^13]: https://www.medianama.com/2026/10/223-ai-cyberattacks-siphon-rs-300-crore-nbfcs
[^14]: https://www.policycircle.org/opinion/upi-mdr-charges-2026
[^15]: https://www.indusind.bank.in/iblogs/savings-account/upi-payment-new-rules-2026
[^16]: https://www.freepressjournal.in/business/pine-labs-reports-strong-q2-fy27-results-revenue-up-24-to-80619-crore-profit-after-tax-rises-six-fold-to-3857-crore
[^17]: https://www.business-standard.com/specials/bs-events/bfsi-insight-summit-mdr-vital-to-sustain-upi-growth-says-phonepe-ceo-126102701765_1.html
[^18]: https://bfsi.eletsonline.com/upi-worlds-largest-real-time-payment-system-sitharaman-rbi-data-centre-odisha
[^19]: https://www.fintechbiznews.com/govtregulators/new-dc-will-enhance-security-of-critical-systems
[^20]: https://economictimes.indiatimes.com/news/economy/policy/rbi-launches-digital-currency-retail-sandbox/articleshow/124388034.cms
[^21]: https://www.thehindu.com/news/national/sc-calls-for-mandatory-compensation-to-digital-fraud-victims-in-case-of-banks-due-diligence/article71640230.ece
[^22]: https://www.medianama.com/2026/10/223-sc-rbi-banks-compensate-digital-arrest-victims
[^23]: https://entrackr.com/report/weekly-funding-report-weekly-funding-report/funding-and-acquisitions-in-indian-startups-this-week-oct-26-oct-31-12770310
[^24]: https://alleywatch.com/2026/10/the-alleywatch-startup-daily-funding-report-10-27-2026
[^25]: https://www.ey.com/en_in/newsroom/2026/10/pe-vc-investment-activity-in-india-reached-us-dollor-17-point-1-billion-across-348-deals-in-3q2026-a-46-percent-year-on-year-increase
