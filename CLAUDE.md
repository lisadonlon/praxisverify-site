# CLAUDE.md — praxisverify-site

Marketing website for PraxisVerify. Live at **https://praxisverify.com** via GitHub Pages.

## What This Is

The public face of the company — single-page landing site plus social/SEO assets. Not a web app. No build step, no framework.

## Stack

| Layer | Choice | Notes |
|-------|--------|-------|
| Markup | Plain HTML | `index.html` + `about.html`, `contact.html`, `experts.html`, `privacy.html`, `terms.html` |
| Styles | Inline CSS | No external stylesheet, no Tailwind, no preprocessor. `index.html` carries the full block; the five interior pages share an identical smaller block |
| Scripts | Inline JS | Fade-in observer + nav scroll-spy + ledger clock (index), hamburger toggle, cookie consent |
| Hosting | GitHub Pages | `CNAME` file points to `praxisverify.com` |
| CDN | GitHub Pages default | Cloudflare recommended — see `CLOUDFLARE-SETUP.md` |

## File Map

| File | Purpose |
|------|---------|
| `index.html` | Main page (two-door hero, stat strip, the gap, how it works, audit ledger, early access, footer) |
| `about.html` | Dedicated about page (AboutPage schema, founder bio, mission, services) |
| `contact.html` | Contact page (ContactPage schema, demo CTA, email, LinkedIn, expert signup) |
| `experts.html` | Expert recruitment page (credentialing, rates, vetting, FAQ) |
| `privacy.html` | GDPR-compliant privacy/cookie policy |
| `terms.html` | Terms of service |
| `design.md` | **Design system as shipped** — tokens, components, breakpoints, anti-patterns. Read before any visual change |
| `llms.txt` | AI crawler guidance |
| `serve.py` | Local preview server mirroring GitHub Pages clean URLs (`python3 serve.py`) |
| `CNAME` | Custom domain: `praxisverify.com` |
| `robots.txt` | Crawler rules |
| `sitemap.xml` | Search engine sitemap (all six pages) |
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

- Sticky nav bar on every page: The gap → How it works → Audit trail → For experts → About → Contact, plus a pill CTA
- Dedicated pages: about.html (AboutPage), contact.html (ContactPage), experts.html, privacy.html, terms.html
- About section on homepage with founder bio (Lisa Donlon)
- Visible author byline + datePublished on all pages
- Structured data: Organization, WebPage, WebSite, FAQPage, AboutPage, ContactPage schemas
- `llms.txt` at site root for AI crawler guidance
- All pages cross-linked via footer and sitemap

## Working on the Site

- **Read `design.md` first** — it is the site-specific record of tokens, components and anti-patterns actually shipped. `pv-branding` wins if the two disagree.
- Edit `index.html` directly — the CSS is in the `<style>` block, the JS is inline at the bottom.
- The five interior pages each carry their own inline CSS (an identical shared block). There is no stylesheet — a token change must be repeated across all six files; grep for the token.
- Check the site still renders on mobile. Breakpoints: 860px (hamburger), 760px (stat strip), 736px (band padding), 480px (container padding). Multi-column blocks use `auto-fit` grids and reflow without breakpoints.
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
