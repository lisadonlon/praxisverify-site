# CLAUDE.md — praxisverify-site

Marketing website for PraxisVerify. Live at **https://praxisverify.com** via GitHub Pages.

## What This Is

The public face of the company — single-page landing site plus social/SEO assets. Not a web app. No build step, no framework.

## Stack

| Layer | Choice | Notes |
|-------|--------|-------|
| Markup | Plain HTML | `index.html` (~920 lines) + `about.html`, `contact.html`, `privacy.html` |
| Styles | Inline CSS | No external stylesheet, no Tailwind, no preprocessor |
| Scripts | Inline JS | Nav show/hide on scroll, fade-in observer, cookie consent |
| Hosting | GitHub Pages | `CNAME` file points to `praxisverify.com` |
| CDN | GitHub Pages default | Cloudflare recommended — see `CLOUDFLARE-SETUP.md` |

## File Map

| File | Purpose |
|------|---------|
| `index.html` | Main page (hero, stats, trust, solution, about, beta CTA, contact footer) |
| `about.html` | Dedicated about page (AboutPage schema, founder bio, mission, services) |
| `contact.html` | Contact page (ContactPage schema, demo CTA, email, LinkedIn, expert signup) |
| `privacy.html` | GDPR-compliant privacy/cookie policy (dark theme, glass cards) |
| `CNAME` | Custom domain: `praxisverify.com` |
| `robots.txt` | Crawler rules |
| `sitemap.xml` | Search engine sitemap (index, about, contact, privacy) |
| `CLOUDFLARE-SETUP.md` | Instructions for adding Cloudflare security headers |
| `favicon-{32,64,180}.png` | Favicons (standard + Apple touch icon) |
| `social-card-1200x630.png` | Open Graph card for link previews |
| `logo-stacked-*.png`, `mark-*.png`, `pvlogowhitebg.png` | Logo variants |
| `BrandKit/` | **Duplicate** of brand assets — see Brand Coupling below |
| `img/` | Photography and illustration assets |
| `squirrel.toml` | Config for SquirrelScan SEO audit tool (optional) |

## Brand Coupling

Brand assets (logos, colours, favicons, social card) are **shared** with the PraxisVerify admin tool's email wrapper (`services/gmail_service.py::wrap_email_html`). This site holds a local copy at `BrandKit/` — the admin tool has its own copy.

**Portfolio plan (Decision 010):** BrandKit will be promoted to a top-level `brand/` slot in the umbrella workspace (`~/Projects/praxisverify/brand/`) during the Mac migration, and both this site and the admin tool will consume from the single source. Until then, keep the two copies in sync manually — any brand change must land in both.

## Deployment

1. Commit to `master` branch
2. Push to `origin` (GitHub)
3. GitHub Pages redeploys within a few minutes
4. Verify at https://praxisverify.com

No CI. No build. No preview environment. GitHub Pages serves `index.html` directly from the repo root.

## Security

- **CSP meta tag** in `index.html` `<head>` — covers inline scripts/styles, GA4, Google Fonts
- **Cloudflare** enabled — HTTP security headers (HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, CSP) via Transform Rules

## SEO / E-E-A-T

- Fixed nav bar (appears on scroll) with links: Problem → Solution → About → Beta → Contact
- Dedicated pages: about.html (AboutPage), contact.html (ContactPage), privacy.html (WebPage)
- About section on homepage with founder bio (Lisa Donlon)
- Visible author byline + datePublished on all pages
- Structured data: Organization, WebPage, WebSite, FAQPage, AboutPage, ContactPage schemas
- `llms.txt` at site root for AI crawler guidance
- All pages cross-linked via footer and sitemap

## Working on the Site

- Edit `index.html` directly — the CSS is in the `<style>` block, the JS is inline at the bottom.
- `about.html`, `contact.html`, `privacy.html` each have their own inline CSS (subset of index.html styles). Keep visual consistency across all pages.
- Check the site still renders on mobile (hero breaks below ~640px need the existing media queries).
- If adding a new page, remember to update `sitemap.xml` and add internal links from `index.html`.
- Run `squirrelscan` for an SEO audit if making substantive content changes (see `squirrel.toml`).

## Related Projects

| Project | Relationship |
|---------|--------------|
| `PraxisVerify` (admin tool) | Shares BrandKit assets — email wrapper must match site visual identity |
| `praxis-mvp` (SaaS platform) | Sign-up links on this site point at the platform's registration flow |
| `AIfirst` | No direct coupling; marketing content ideas sometimes flow from vault research |

## Portfolio Context

This project lives at `C:\Projects\praxisverify-site` today. Post–Mac migration it moves to `~/Projects/praxisverify/products/site/` per Decision 010. Git remote is preserved across the move.
