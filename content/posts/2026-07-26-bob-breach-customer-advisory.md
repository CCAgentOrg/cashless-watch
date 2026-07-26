---
title: "BoB Data Breach: Your 8-Step Action Plan"
date: 2026-07-26T16:45:00+05:30
draft: false
tags: ["Security", "BoB", "Bank of Baroda", "Data Breach", "Triple X", "Ransomware", "Consumer Protection"]
categories: ["Security"]
description: "Triple X ransomware group has published 15,774 files from Bank of Baroda's internal servers. Here's what you need to do right now to protect your accounts and identity."
---

## BoB Data Breach: Your 8-Step Action Plan

Bank of Baroda customers are facing the largest breach of an Indian PSU bank's internal systems ever documented. On July 26, the Triple X ransomware group's Tor hidden server went live with the complete directory tree of Bank of Baroda's internal SharePoint file server — **15,774 files across 2,671 directories**, containing everything from individual customer CKYC records to database login credentials to the bank's complete vulnerability assessment database.

**If you are a BoB customer, act today. Here is your order of operations.**

### Step 1: Change Your bob World / Internet Banking Password Now

Do this before you do anything else. The dump includes mobile banking PIN records (MPIN/TPIN), VAPT reports showing how to break into BoB's apps, and the admin portal SOP — a guide for administering the bank's systems.

**What to do:** Log into bob World or Internet Banking, go to settings, change your password to something you have never used before. Do NOT reuse a password from another service.

### Step 2: Call Your Branch and Freeze Your Account

Account numbers with sufficient patterns to identify individual accounts are present in the dump. Transaction patterns from 5 months of CBS data are exposed, enabling fraudsters to mimic your actual banking behaviour.

**What to do:** Call your home branch or visit in person. Ask for a temporary freeze on any account that allows outbound digital transactions. The inconvenience of unfreezing later is far less than cleaning up a fraudulent transaction.

### Step 3: Report Your Debit and Credit Cards as Compromised

The breach includes NPCI card processing databases, card PIN records, and mobile app binaries that can be reverse-engineered to bypass security controls.

**What to do:** Call BoB's 24/7 customer care (1800 258 5678 / 1800 222 440) or log into Internet Banking and block your debit and credit cards. Request reissuance with new numbers. Yes, it takes 7–10 days. Do it anyway.

### Step 4: Enable Full SMS and Email Alerts on All Accounts

Turn on alerts for every transaction — debit, credit, balance inquiry, password change, beneficiary addition — at any value. Do not set a threshold.

**What to do:** Log into Internet Banking → Alerts → Enable ALL. Set minimum threshold to ₹1 or the lowest available option.

### Step 5: Lock Your Aadhaar

eKYC dumps and Aadhaar vault configuration docs were found in the exposed data. Your Aadhaar number and biometric linkage may have been compromised.

**What to do:** Go to [https://maskaadhaar.uidai.gov.in](https://maskaadhaar.uidai.gov.in) — mask your Aadhaar number. Then visit [https://myaadhaar.uidai.gov.in](https://myaadhaar.uidai.gov.in) and lock your biometrics. This prevents Aadhaar-based authentication without your explicit unlock.

### Step 6: Check Your CIBIL Score and Set Up Credit Monitoring

With full identity documents (CKYC, PAN, Aadhaar) in the hands of attackers, fraudulent loan applications in your name are a real possibility.

**What to do:** Check your credit report at [https://www.cibil.com/freecreditreport](https://www.cibil.com/freecreditreport) (one free report per year) or use any of the regulated credit bureaus. Set up alerts for any new credit inquiry. **Set up a credit freeze** if you don't plan to apply for credit in the next 3–6 months — this prevents anyone from opening new accounts in your name.

### Step 7: Beware of Phishing — Assume Any Call or Message Is Fake

The attackers now know what bank communications look like — transaction formats, notice templates, and branch contact lists were all in the dump.

**What to do:** Do not trust any call, SMS, or email claiming to be from "BoB security" or "BoB fraud prevention." The bank will never ask for OTPs, passwords, or PINs. If someone calls claiming to be from your branch, hang up and call back on the official number you know. **Assume the first wave of targeted phishing is imminent.**

### Step 8: Switch Payments to UPI on Other Banks

If you have a savings account elsewhere, shift your daily payment activity there until BoB communicates a clear all-clear.

**What to do:** Keep the BoB account open for the bank's formal response. But use your backup account for UPI payments, bill payments, and merchant transactions for the next 30 days.

## Why This Breach Is Different

This isn't a typical Indian bank data breach. Previous breaches (Dominos India, Air India, etc.) exposed database tables. This breach exposed an entire Windows file server — including:

- **The bank's own list of known vulnerabilities** (VAPT Mastersheet)
- **Database login credentials** for UAE operations
- **Mobile app binaries** (APKs and IPAs) ready for reverse engineering
- **Admin portal standard operating procedure** — a step-by-step guide to running BoB's internal systems
- **Network packet captures** — actual traffic from the bank's network

## What the Bank and Regulators Should Do

RBI and CERT-In have mandatory incident reporting obligations under the 2022 CERT-In directions and the DPDP Act 2023. The bank must:

1. Notify every affected customer formally within 30 days
2. Force-reset all digital banking credentials
3. Offer free credit monitoring for 24 months
4. Reissue all cards
5. Publish a transparent post-incident report

**We will track whether BoB meets these obligations.** Past form suggests Indian banks prefer silence. We intend to make silence impossible.

---

*Last updated: July 26, 2026. Crawl data and analysis at `BoBHack/` in the CashlessConsumer open workspace.*
