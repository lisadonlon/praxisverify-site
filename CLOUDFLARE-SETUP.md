# Cloudflare Setup for praxisverify.com

These security headers cannot be set via GitHub Pages alone. Cloudflare (free plan) acts as a reverse proxy to add them.

## Step 1 — Create Cloudflare Account

1. Go to [dash.cloudflare.com](https://dash.cloudflare.com)
2. Add Site → `praxisverify.com` → select **Free** plan

## Step 2 — DNS Records

Add these A records (all **Proxied** / orange cloud):

| Type  | Name  | Content            | Proxy   |
|-------|-------|--------------------|---------|
| A     | `@`   | `185.199.108.153`  | Proxied |
| A     | `@`   | `185.199.109.153`  | Proxied |
| A     | `@`   | `185.199.110.153`  | Proxied |
| A     | `@`   | `185.199.111.153`  | Proxied |
| CNAME | `www` | `praxisverify.com` | Proxied |

## Step 3 — Update Nameservers

At your domain registrar, replace the current nameservers with the two Cloudflare assigns you.

**Important:** DNS propagation can take up to 48 hours (usually 15-30 minutes).

## Step 4 — SSL/TLS Settings

- SSL/TLS → Overview → set mode to **Full** (NOT Full/Strict — Strict can break Let's Encrypt renewal on GitHub Pages)
- Edge Certificates → enable **Always Use HTTPS**
- Edge Certificates → enable **Automatic HTTPS Rewrites**

## Step 5 — Security Headers via Transform Rules

Go to Rules → Transform Rules → Modify Response Header → create rule for "All incoming requests":

| Header                       | Value                                         |
|------------------------------|-----------------------------------------------|
| `Strict-Transport-Security`  | `max-age=31536000; includeSubDomains`         |
| `X-Frame-Options`            | `DENY`                                        |
| `X-Content-Type-Options`     | `nosniff`                                     |
| `Referrer-Policy`            | `strict-origin-when-cross-origin`             |
| `Permissions-Policy`         | `camera=(), microphone=(), geolocation=()`    |

## Gotchas

- **Keep the `CNAME` file** in the repo — GitHub Pages uses it independently of Cloudflare DNS
- **Initial setup:** Temporarily set DNS records to DNS-only (grey cloud) until GitHub issues the SSL cert, then re-enable proxy (orange cloud)
- **After git push:** Cloudflare caches aggressively. If changes are urgent, manually purge via Caching → Purge Everything
- **HSTS:** Only configure in ONE place — either Edge Certificates panel OR Transform Rules, not both
- **GitHub Pages custom domain:** After switching nameservers, GitHub may briefly show a certificate error. Re-save the custom domain in repo Settings → Pages to trigger re-provisioning
