---
title: "15,774 Files: The Inside Story of the Bank of Baroda Data Breach"
date: 2026-07-26T16:45:00+05:30
draft: false
tags: ["Security", "BoB", "Bank of Baroda", "Triple X", "Ransomware", "Data Breach", "OSINT", "Investigation", "PSU Banking"]
categories: ["Security"]
description: "A forensic crawl of the Triple X ransomware dump reveals the complete Bank of Baroda file server — CKYC records, CBS transaction logs, VAPT reports, UAE database credentials, mobile app source code, and more."
---

# 15,774 Files: The Inside Story of the Bank of Baroda Data Breach

On July 26, 2026, the Triple X ransomware group's Tor hidden service went live with a recursive directory listing of what appears to be Bank of Baroda's internal Microsoft SharePoint / Windows file server. No authentication required — anyone with the Tor browser could browse 15,774 files across 2,671 subdirectories as if they were sitting at a branch terminal.

We crawled the server in 995 seconds. 925 HTTP fetches, zero errors. The complete file inventory runs to 19,666 lines. This is what we found.

## I. The Scale

| Metric | Count |
|--------|-------|
| Files exposed | 15,774 |
| Directory branches | 62 top-level, 2,671 total |
| Estimated data volume | ~1 TB (per Triple X claim) |
| Data timeline | ~5 years, through June 2025 |
| Countries | India + 7 international operations |
| Named employees compromised | 3+ individual profile directories |

The five largest branches alone account for 11,149 files — 70% of the total:

- `SHIVAMOGGA-AUDITDOCUMENTS/` — **3,023 files** (Karnataka region audit documents)
- `BOBWOLRDAUDIT/` — **2,911 files** (bob World mobile banking platform audit)
- `saurabh.kumar8/` — **2,464 files** (named employee's personal document cache)
- `SpecialAuditBOBWORLD2/` — **1,588 files** (special audit of bob World)
- `BCR211102023/` — **1,163 files** (Basic Customer Reports — individual account documents)

A named employee workspace with 2,464 files means the attacker had domain-level credential access — not just a web application vulnerability but a Windows domain account that could browse individual user profile folders.

## II. What Was Taken

### Customer Data

The `BCR211102023/` directory contains 1,163 institutionally-formatted Basic Customer Reports. Each typically contains: customer name, address, phone, account numbers, KYC status, Aadhaar/PAN linkage, and photographs.

Across the entire dump, approximately 9,200+ filenames contain 14–16 digit numerical sequences consistent with account numbers. We identified **84 unique 15-digit account number patterns.**

The eKYC exposure includes bulk Aadhaar-linked identity records, Aadhaar Seeding documentation, and Aadhaar Vault configuration documents (BRD-Aadhar Vault.docx, BRD_AADHAR_VAULT_012022.pdf).

### Financial Transaction Logs

The most dangerous financial data in the dump is the **50+ daily CBS transaction exports** covering August 2024–January 2025. These contain every core banking transaction for those dates — complete dance floors for financial analysis.

Loan data is equally exposed: a February 2026 loan dump, agriculture credit portfolios (BKCC) from the Bhilwara region, SHG (Self-Help Group) data, NPA records from the post-merger era, and PMSBY insurance claims with beneficiary Aadhaar linkage.

### Database Credentials

The `UAE_DB_userdetails.xlsx` file contains database user accounts for UAE operations. This is credential material, not metadata. Combined with the httpd configs for both Data Center and Disaster Recovery sites, an attacker has the keys to BoB's UAE infrastructure.

### Vulnerability Database

The `VAPT Mastersheet.xlsx` is potentially the most damaging single file in the dump. It is the complete vulnerability database for all of BoB's applications — every security finding, from critical API flaws to minor configuration issues. For a threat actor, this is a ready-made attack playbook.

Multiple Bob World VAPT reports (iOS v3.7.1, v3.7.2, Android) and secure code review reports from Cheggout Services Private Limited add further detail: hardcoded secrets, insecure storage, authentication bypass paths. All documented, all exposed.

### Network Packet Captures

2 PCAP files were detected in the `VAReports/` directory. If they contain live traffic, they could reveal internal IP schemes, server-to-server authentication mechanisms, database connection strings, and potentially cleartext credentials.

### Mobile Application Source Code

The dump includes 5 APKs, 12 IPAs, and 6 AABs — covering bob World, UPI SDK components, mPassbook Kenya, M-Connect Plus International, and an IFSC app. Combined with the VAPT findings and secure code review reports, these are fully actionable for reverse engineering.

### International Operations Blueprints

The 38 files from UAE operations include: full server inventory, DC/DR cutover plans, technical architecture manual, database user credentials, admin portal SOP, ISO 27001:2022 certificate, and escrow agreements. BoB's entire international banking infrastructure is mapped.

## III. The Threat Actor

Triple X is a newly emergent ransomware group, first observed in May 2026. Prior to BoB, its only confirmed victim was Bank Negara Indonesia (BNI), Indonesia's largest state-owned bank — similarly exfiltrated ~2 TB of customer data.

The group operates a double-extortion model with a distinctive approach to public disclosure. Unlike many groups that post sample teasers, Triple X publishes **complete recursive directory listings** — verbatim copies of the internal file structures. The BoB dump server mirrors the SharePoint folder hierarchy almost exactly.

For BoB, the group claims initial access was via a "weak password." The Geographic concentration in Shivamogga (Karnataka, 3,023 files) and Bhilwara (Rajasthan, multiple BKCC portfolios) suggests the initial vector was likely a regional office, followed by extensive lateral movement through BoB's Windows domain.

## IV. Regulatory & Legal Implications

### Indian Regulations

The breach triggers mandatory reporting to **CERT-In** (within 6 hours under the 2022 Directions) and to **RBI** (under banking data breach guidelines). The **DPDP Act 2023** requires formal notification to affected data principals — all BoB account holders, insurance beneficiaries, and loan customers whose data appears in the dump.

### Multi-Jurisdictional

With data from UAE, Botswana, Fiji, Kenya, Guyana, Seychelles, and Uganda exposed, BoB faces breach notification obligations in multiple jurisdictions — including potential **GDPR** exposure for any EU-connected customers transacting through the international branches.

### Certifications

The breach includes the bank's actual **ISO 27001:2022 certificate** (ISO_27001_Certificate_BOB_2025.pdf) and **PCI-DSS** compliance evidence. Both certifications now require impact assessment and potential re-certification.

## V. What Should Happen Next

### For the Bank

1. **Password reset** for every user with access to the compromised server — not just customers, but employees, vendors, and administrators
2. **Credential rotation** — all exposed database passwords, API keys, and secrets (especially UAE DB accounts)
3. **Mobile app audit** — the exposed APKs and IPAs should be assumed compromised; revoke all API keys embedded in the binaries
4. **VAPT remediation** — every vulnerability documented in the VAPT Mastersheet must be assumed public and exploitable
5. **International coordination** — notify banking regulators in all affected jurisdictions

### For the Regulators

RBI must use this breach to mandate a **PSU-wide audit of document management infrastructure**. If one bank's SharePoint was compromised via a weak password, the same vulnerability exists at every PSU bank that runs similar infrastructure. The seven-year post-merger data integration failure (eDenA and Vijaya Bank data still on BoB servers) should also trigger merger-related data hygiene mandates.

### For Customers

BoB's ~15 crore customers should take these steps immediately:

1. **Change all digital banking passwords** — bob World, Internet Banking, mConnect Plus
2. **Block and reissue debit/credit cards** — card processing databases were in the dump
3. **Enable full transaction alerts** — every transaction, any amount
4. **Lock Aadhaar biometrics** — at myaadhaar.uidai.gov.in
5. **Set up credit monitoring** — fraudulent loans in your name are a real risk
6. **Prepare for targeted phishing** — the attackers now know how BoB communicates

## VI. The Accountability Question

Indian PSU banks have a poor track record of post-breach customer communication. Previous breaches at Canara Bank, SBI (2018 data leak), and multiple NBFCs were either denied, minimized, or handled with delayed, inadequate customer notifications.

This breach is orders of magnitude larger. The exposed data includes not just what customers gave the bank, but what the bank knew about its own security vulnerabilities and chose not to fix.

CashlessConsumer will track and report on:

- Whether BoB formally notifies affected customers (and when)
- Whether RBI mandates a sector-wide audit
- What compensation is offered (credit monitoring, liability coverage)
- Whether any regulatory penalties are imposed

---

*This report is based on a recursive crawl of Triple X's Tor hidden service conducted on July 26, 2026, covering 15,774 file names across 2,671 directories. No file contents were downloaded. Methodology: Python BFS via Tor SOCKS5 proxy, metadata-only collection. The complete inventory is available at `BoBHack/boob-dump-inventory.md`.*
