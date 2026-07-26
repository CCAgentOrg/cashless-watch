---
title: "BoB's 15,774-File Leak: Anatomy of India's Worst PSU Bank Breach"
date: 2026-07-26T16:45:00+05:30
draft: false
tags: ["Security", "BoB", "Bank of Baroda", "Data Breach", "Triple X", "Ransomware", "DPI", "Consumer Protection", "Investigation"]
categories: ["Deep Dive"]
description: "The Triple X ransomware group dumped BoB's internal SharePoint — 15,774 files across 2,671 directories, including KYC records, CBS transactions, VAPT reports, and DB credentials. What happened, what was taken, and what customers need to do."
---

## BoB's 15,774-File Leak: Anatomy of India's Worst PSU Bank Breach

On the morning of July 26, a Tor hidden service went live carrying what may be the most comprehensive single breach of an Indian public sector bank's internal systems ever documented. **15,774 files. 2,671 subdirectories. No authentication required to access any of it.**

The Triple X ransomware group — a new actor first detected in May 2026 — published the complete directory tree of Bank of Baroda's internal SharePoint / Windows file server. Our team crawled the dump server for 995 seconds across 925 HTTP fetches with zero errors. This analysis is based on the metadata alone: file names, directory paths, and structure. We downloaded nothing.

**Here is what the dump tells us, what it means for customers, and what should happen next.**

### What Was Taken

The exposed data is not a "customer database export" — it is the bank's entire shared document infrastructure, spanning approximately 5 years of operations with files dated as recently as June 2025. The key categories:

#### Customer Data
- **1,163 Basic Customer Report (BCR) files** — individual customer documents with name, address, KYC status, Aadhaar/PAN linkage, photographs
- **~9,200+ files containing 14-16 digit account-number patterns** — 84 distinct account number prefixes across the dataset
- **50+ CBS transaction logs** — daily Core Banking System transaction exports covering August 2024 through January 2025, representing all CBS transactions for those dates
- **Agriculture credit (BKCC) data** — farmer loan portfolios including Self-Help Group data and multiple BKCC dumps from Bhilwara, Rajasthan
- **Loan portfolio snapshots** — including a Loan Dump dated February 2026
- **eKYC and CKYC files** — bulk Aadhaar-linked identity records, KYC scanner setup files
- **PMSBY insurance claims data** — government insurance scheme beneficiary data
- **NPA records** — post-merger and current non-performing asset data

#### Security Infrastructure
This is the most unusual part of the breach. The dump includes a structured **audit evidence package** (labelled Point1 through Point51+) — what appears to be material prepared for an external auditor or regulator, exfiltrated in its entirety:

- **VAPT Mastersheet** — the bank's complete vulnerability assessment database across all applications
- **VAPT reports** for Bob World iOS (v3.7.1, v3.7.2), Android, NEFT/RTGS/SFMS core payment systems, Guyana and Uganda operations
- **Secure code review reports** from Cheggout Services (third-party security vendor) — Android and iOS
- **Threat modelling documents** for Bob World mobile app (UAT and Production configurations)
- **ISO 27001:2022 certificate** — the bank's ISMS certification document
- **PCI-DSS compliance evidence**
- **Network packet captures (PCAPs)** — raw traffic from the bank's network

#### International Operations
The dump exposes operations across 7 countries:

- **UAE (38 files)**: Complete server inventory, database user credentials, httpd configs for both primary Data Center and Disaster Recovery sites, DC/DR cutover plans, M-Connect Plus iOS app binary
- **Uganda (95 files)**: Fraud monitoring solutions, VAPT reports for Android and iOS
- **Guyana (80 files)**: Fraud monitoring documentation
- **Seychelles (80 files)**: Fraud monitoring and RFCs
- **Botswana (22 files)**, **Fiji (21 files)**, **Kenya (3 files)** including the BOB mPassbook Kenya iOS app binary

#### Credentials and Access
- **Database user details file** for UAE operations
- **MPIN/TPIN records** — mobile and transaction PIN data
- **Admin portal activity logs**
- **Password policy documents**
- **Admin portal SOP** — a complete step-by-step guide to administering the bank's internal systems

### How Big Is This?

Compare to known Indian financial sector breaches:

| Breach | Year | Files/Documents | Type |
| --- | --- | --- | --- |
| **BoB (this)** | **2026** | **15,774 files** | **Full file server** |
| Dominos India | 2021 | ~13M records | Database tables |
| Air India | 2021 | 4.5M records | SITA PSS data |
| Upstox | 2021 | ~2.5M records | KYC database |
| BoB (previous) | 2024 | Unknown | Ransomware (limited) |

The previous Indian financial breaches were database table leaks. This is an entire file server — including the bank's own security documentation, credentials, and architecture blueprints. The difference in magnitude is not incremental. It is categorical.

### The Geography of Compromise

The data's structure tells us something about the attack path. Three branches dominate:

- **SHIVAMOGGA-AUDITDOCUMENTS/** — 3,023 files (Karnataka region)
- **BOBWOLRDAUDIT/** — 2,911 files (Bob World audit)
- **saurabh.kumar8/** — 2,464 files (a named employee's personal workspace)

The regional concentration in Shivamogga (Karnataka) and Bhilwara (Rajasthan — agriculture credit branch) suggests the initial compromise may have been through a regional office with weaker security posture, followed by lateral movement to the central file server.

The presence of named employee directories (`saurabh.kumar8/`, `storageamit/`, `PERSONALFOLDER01092025/`) confirms the attackers gained access to individual user profile folders — either through domain credential compromise or file-server-level access.

### The Threat Actor: Triple X

Triple X is a newly emergent ransomware group (first observed May 2026). Their two confirmed victims are both large state-owned banks: Bank Negara Indonesia (May 2026) and Bank of Baroda (July 2026). Their Tor dump servers provide unauthenticated recursive directory access — no sample data teasers, no negotiation games. The full content, or enough of it to reconstruct the structure, is public.

The "weak password" attribution for the BoB breach comes from GalaxyWarden. If true, it means a single weak credential — an employee password, a VPN account, a forgotten service account — was the initial access vector into a bank with 15,774 documents of internal data, 5+ years of operations, and international operations across 7 countries.

### What This Means for the Indian Banking System

#### For BoB Customers
The immediate risk is not the dump itself (the files are behind Tor and most criminals do not use Tor). The risk is what happens next:

1. **Targeted phishing.** Attackers now know BoB's document formats, transaction templates, and internal communication patterns. Expect SMS and calls that perfectly mimic official BoB communications.
2. **Credential stuffing.** Account numbers are exposed. Password hashes may be present in archived/non-indexed content. Automated login attempts against bob World are inevitable.
3. **Identity fraud.** CKYC documents, PAN records, and Aadhaar linkage data enable fraudulent loan applications and account openings.
4. **Social engineering against bank staff.** Named employees are identified. Admin portal SOP is public. Phone numbers and email addresses from branch contact lists enable direct targeting of bank personnel.

**See our companion action plan:** [BoB Data Breach: Your 8-Step Action Plan](https://cashlessconsumer.zo.space/blog/cashlessconsumer/post?slug=2026-07-26-bob-data-breach-advisory)

#### For Regulators
This breach tests the DPDP Act 2023's effectiveness. The Act mandates:
- Breach notification to affected data principals within a reasonable timeframe
- Penalties of up to ₹250 crore for breach of personal data

The 2022 CERT-In directions require incident reporting within 6 hours. RBI's Master Direction on Information Security requires mandatory disclosure.

If BoB does not initiate customer notification within 30 days of discovery, the DPDP Act's provisions should be triggered. Past form — Indian banks have a history of silence on data breaches — suggests regulators must act proactively, not reactively.

#### For Other Banks
The Triple X group is actively operating. The BNI breach in May, now BoB in July — this pattern suggests a group that targets large state-owned banks in emerging markets. If your bank uses SharePoint for internal document management, ask whether your VAPT reports, admin credentials, and customer CKYC documents live on the same server.

### What the Bank Should Do (and We'll Track Whether They Do)

This is not a breach where deactivating a few accounts suffices. The scale requires:

1. **Immediate:** Isolate the compromised server. Force-reset all credentials for every employee and customer who accessed the system since the breach window.
2. **Short-term:** Identify every affected customer (the BCR, CBS, CKYC, and BKCC files suggest millions potentially impacted). Notify them formally. Offer credit monitoring. Reissue cards.
3. **Medium-term:** Third-party forensic audit. Structural restructuring of document management with least-privilege access. Network segmentation of international operations from domestic operations.

### What We Are Doing

We have documented the full inventory — all 2,671 directories and 15,774 files — as a structured reference. Our crawl methodology is transparent: Python-based BFS via Tor SOCKS5 proxy, metadata only, zero file contents downloaded.

We are monitoring BoB's public communications for:
- Customer notification (deadline: ~30 days from breach discovery under DPDP Act)
- Card reissuance offers
- Credit monitoring provisions
- Transparent post-incident reporting

**History suggests Indian banks default to silence. We are here to make silence impossible.**

---

*Full intelligence report and inventory at `file BoBHack/` in the CashlessConsumer open workspace. Crawl date: July 26, 2026. Server status: Online (may change).* 
