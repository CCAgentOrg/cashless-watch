---
title: "India's .bank.in Domains Are Leaking Secrets — And It Shouldn't Be This Easy"
date: 2026-08-19T12:30:00+05:30
draft: false
tags: ['Security', 'RBI', 'IDRBT', 'bank.in', 'CERT-In', 'Banking', 'Vulnerability']
categories: ["Research"]
description: "A systematic scan of 1,393 .bank.in domains reveals env files, Spring Boot actuator endpoints, phpinfo pages, composer.json, and Laravel logs exposed in plain sight — no authentication bypass, just GET requests."
---

# India's .bank.in Domains Are Leaking Secrets — And It Shouldn't Be This Easy

*An anonymised security scan of RBI's banking TLD reveals env files, debug endpoints, and framework metadata exposed in plain sight.*

---

## What happened

Prompted by a [recent post on X](https://x.com/DarthKermi72747/status/2089641015116526064) noting that sensitive files on `.bank.in` domains were trivially accessible, I ran a systematic scan across the entire `.bank.in` namespace.

**Scope:** 1,393 unique `.bank.in` hostnames — built from prior DNS/CT logging, Wayback Machine CDX expansion, and HackerTarget subdomain enumeration. Every major bank, cooperative bank, payments bank, and DCCB with a `.bank.in` domain was covered.

**Method:** A single read-only `GET` request to common sensitive paths (`.env`, `/phpinfo.php`, `/composer.json`, `/actuator/env`, `/actuator/heapdump`, `/storage/logs/laravel.log`) with a 6-second timeout per request. No authentication was bypassed. No data was modified. No credentials were stored — only key names and response metadata were logged.

## What was found

### 1. `.env` files served at the web root (2 banks)

Two banks — one a licensed payments bank, the other a cooperative bank in Rajasthan — are serving their **production `.env` files** directly at `https://<domain>/.env`. No authentication, no WAF block, no 403. Just a clean HTTP 200.

The payments bank's `.env` contains:
- `APP_ENV=prod`
- A Google API key
- A 128-character secret key for a geolocation service
- A full public/private key pair for the same service

The cooperative bank's `.env` contains:
- SMTP credentials (mail host, username, password, from/to addresses)
- A reCAPTCHA secret key

These are not cached pages or soft-404 HTML responses. They are real, parseable dotenv files served as `application/octet-stream`. Both were re-verified as live hours after the initial scan.

### 2. Spring Boot Actuator endpoints exposed (1 bank)

A major private-sector bank's credit card application subdomain exposes:
- **`/actuator/env`** — The full Spring Boot environment property source listing, including internal service URLs, configuration property names, and potentially sensitive application config.
- **`/actuator/heapdump`** — A downloadable JVM heap dump of the running application. This is the memory snapshot of a **live production credit card application system**. Heap dumps can contain session tokens, decrypted data in memory, database connection strings, and partial customer data processed during requests.

Both endpoints returned HTTP 200 with no authentication challenge.

### 3. `phpinfo()` exposed (2 banks)

Two banks — one a major private-sector bank, the other a district cooperative central bank — have `phpinfo.php` accessible at the web root. This PHP diagnostic page reveals:
- Exact PHP version and all loaded extensions
- Server software version (Apache/Nginx)
- Document root paths and server configuration
- All environment variables
- Database driver versions
- Loaded ini files and their paths

This is the kind of information that turns a generic vulnerability into a targeted exploit.

### 4. `composer.json` exposed (15 banks)

Fifteen `.bank.in` domains — a mix of cooperative banks, DCCBs, and a few scheduled banks — serve their `composer.json` at the web root. This file reveals:
- Exact framework and dependency versions (Laravel, Symfony, etc.)
- All project dependencies with version constraints
- Package names that hint at the application's architecture and third-party integrations

An attacker with a list of specific dependency versions can cross-reference known CVEs and identify which vulnerabilities the application is *actually* vulnerable to, rather than guessing.

### 5. Laravel application logs exposed (5 banks)

Five banks are serving their Laravel `storage/logs/laravel.log` file publicly. Application logs can contain:
- Stack traces with full file paths
- Database query errors (potentially leaking schema or data)
- Authentication failure messages (confirming valid usernames)
- Session tokens or request details
- Third-party API error responses with internal information

## Why this matters

These are not theoretical risks. Each of these exposures lowers the barrier for attacks on India's banking infrastructure in concrete ways:

- **Exposed `.env` files give attackers the keys to the kingdom.** SMTP credentials enable business email compromise. API keys and cryptographic key pairs allow impersonation of the bank's integrations. The payments bank exposure is particularly concerning — it holds a valid RBI licence and processes real customer transactions.
- **Heap dumps from a credit card application system can contain in-memory customer data.** Even partial card numbers, names, or session tokens extracted from a heap dump could be used for fraud or further infiltration.
- **phpinfo() and composer.json together give attackers a precise attack surface.** Instead of blindly probing for vulnerabilities, an attacker knows exactly what's running, at what version, with what extensions, and what known CVEs apply.
- **Laravel logs can reveal operational secrets.** Database errors, API failures, and authentication attempts paint a picture of the bank's internal architecture and security posture.

The `.bank.in` TLD was created by RBI/IDRBT specifically to provide a **trusted, verified namespace** for Indian banks — a signal to customers that they're on the real, official website. That trust is undermined when the same domains serve secrets to anyone who types `/.env` in their browser.

## The fix

These are not sophisticated attacks to defend against. Every single exposure is a basic deployment hygiene failure with a straightforward fix:

1. **Remove `.env` files from the web root.** In every major framework (Laravel, Spring Boot, Express, Django), the `.env` file should live *outside* the document root. If it must be in the project directory, the web server must be configured to deny access (e.g., Apache `<FilesMatch>`, Nginx `location = /\.env { deny all; }`). Better yet, use environment variables or a secrets manager.

2. **Secure or disable Spring Boot Actuator endpoints.** If actuator endpoints are needed for monitoring, they must be behind authentication (Spring Security). The `/actuator/heapdump` endpoint should be **disabled in production** — there is almost no legitimate reason to serve a memory dump over HTTP on a credit card application system. A simple `management.endpoint.heapdump.enabled=false` in `application.properties` would have prevented this.

3. **Remove `phpinfo()` from production.** Delete `phpinfo.php` from the web root. It should never have been deployed there. If it's needed for debugging, it should be on a staging server behind auth, never on a production banking domain.

4. **Block `composer.json` and similar metadata files.** Add rules to deny access to `.json`, `.lock`, `.yml`, `.xml` metadata files that aren't part of the application's API. Alternatively, move them outside the document root.

5. **Block application log files from web access.** Laravel's `storage/` directory should never be web-accessible. The default `.htaccess` in Laravel's `public/` directory doesn't cover this — it requires explicit web server configuration to deny access to `../storage`.

6. **Deploy a WAF or at least basic path-blocking rules.** A simple request-filtering rule that blocks requests for `/.env`, `/phpinfo.php`, `/.git`, `/.svn`, `/actuator/*`, and other known-sensitive paths would have prevented **every single finding** in this scan. Cloud-hosted WAFs (AWS WAF, Cloudflare, etc.) have managed rule sets for exactly this.

7. **IDRBT should run proactive security scanning.** As the custodian of the `.bank.in` TLD, IDRBT has a list of every registered domain. A quarterly automated scan for common exposures — not just DNS availability — would catch these issues before researchers do. This is standard practice in other country-code banking TLDs.

## Disclosure

All findings have been reported to CERT-In, RBI, CSIRT-FIN, and the affected banks' registered security/IT contacts. This post deliberately does not name individual banks. The purpose is to highlight a systemic problem, not to single out specific institutions.

The `.bank.in` namespace is supposed to signal safety. Right now, for too many domains, it signals the opposite.

---

*Scan methodology: read-only GET requests to 1,393 `.bank.in` hostnames across 6 sensitive paths. No authentication bypass. No data stored beyond key names and response metadata. Full responsible disclosure to regulators and affected institutions completed prior to publication.*
