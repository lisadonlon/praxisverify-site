# CLAUDE.md — praxisverify-site

Marketing website for PraxisVerify. Live at **https://praxisverify.com** via GitHub Pages.

## What This Is

The public face of the company — single-page landing site plus social/SEO assets. Not a web app. No build step, no framework.

## Stack

| Layer | Choice | Notes |
|-------|--------|-------|
| Markup | Plain HTML | `index.html` — 825 lines, inline `<style>` block |
| Styles | Inline CSS | No external stylesheet, no Tailwind, no preprocessor |
| Scripts | Inline JS | Minimal — nav toggle, smooth scroll |
| Hosting | GitHub Pages | `CNAME` file points to `praxisverify.com` |
| CDN | GitHub Pages default | No Cloudflare, no custom CDN |

## File Map

| File | Purpose |
|------|---------|
| `index.html` | Single-page site (hero, features, pricing, contact) |
| `CNAME` | Custom domain: `praxisverify.com` |
| `robots.txt` | Crawler rules |
| `sitemap.xml` | Search engine sitemap |
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

## Working on the Site

- Edit `index.html` directly — the CSS is in the `<style>` block, the JS is inline at the bottom.
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
