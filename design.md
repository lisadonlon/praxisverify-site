# praxisverify.com — Design Notes

A working reference for what's actually implemented on the marketing site. Not the brand system itself — that lives in the `pv-branding` skill (`~/.claude/skills/pv-branding/SKILL.md`), which is the canonical source for colour, typography, and component rules across all surfaces (website, MVP platform, admin tool, pitch decks). This file is the site-specific snapshot: the tokens, components, and conventions actually shipped to `praxisverify.com`.

If `pv-branding` and this file disagree, the brand skill wins and this file should be updated.

## Stack & conventions

| Item | Choice |
|---|---|
| Markup | Plain HTML, no framework |
| Styles | Inline `<style>` block per page — no external stylesheet, no preprocessor |
| Scripts | Inline `<script>` — fade-in IntersectionObserver (index), nav scroll-spy (index), cookie consent (all pages), nav hamburger toggle + Escape-to-close (all pages) |
| Hosting | GitHub Pages from `master`; Cloudflare in front for security headers and TLS |
| Build | None — files served as-is |
| Deploy | `git push origin master` → GitHub Pages rebuilds in ~1–2 min |

Pages: `index.html`, `experts.html`, `about.html`, `contact.html`, `privacy.html`, `terms.html`.

Each page carries its own copy of the CSS block. Changes to shared tokens or components must be repeated across all six files — there is no shared stylesheet. When changing a token, grep for it across the directory.

## Pillars

Per `pv-branding`, the site expresses two of the three brand pillars:

- **The Authority (dark)** — `index.html`, `about.html`, `contact.html`, `privacy.html`, `terms.html`. Deep Navy background, white glass cards, emerald actions. The index hero carries the dark→light "bridge" gradient behind its white card.
- **The Journal (light)** — `experts.html`. Light `#F3F4F6` surface, white cards, hairline borders, single faint navy-mark watermark. Light by design — do not darken.

> A full-page dark Authority hero + scrolling dark→light journey + motion layer was prototyped and **rejected by Lisa (2026-06-11)** — too dark, foil asset blocky. Do not reintroduce without a fresh brief.

## Colour tokens

Custom properties declared on `:root` in every page:

| Token | Value (dark pages) | Value (experts.html) | Use |
|---|---|---|---|
| `--bg` | `#0A192F` | `#F3F4F6` | Page background (Deep Navy / Journal light) |
| `--surface` | `#FFFFFF` | `#FFFFFF` | Card surface |
| `--border` | `#10B981` | `#E2E4E9` | Card border (emerald on dark pages, hairline on Journal) |
| `--card-text` | `#0A192F` | `#0A192F` | Headings on cards |
| `--card-text-muted` | `#3F4654` | `#3F4654` | Body text on cards |
| `--text` | `#E5E9F0` | `#0A192F` | Body text on page background |
| `--text-muted` | `#8892A6` | `#5C6473` | Secondary text on page background |
| `--btn-bg` | `#10B981` | `#10B981` | Primary CTA fill (brand emerald) |
| `--btn-text` | `#0A192F` | `#0A192F` | Button text — Deep Navy, **never white** (white on `#10B981` fails AA at 2.54:1) |
| `--link` | `#047857` | `#047857` | Link/text emerald on white cards (5.48:1 — `#10B981` fails AA as text on white) |
| `--link-hover` | `#065F46` | `#065F46` | Link hover |
| `--accent-platform` | — | `#10B981` | Emerald accent on Journal page (subtitle keel, FAQ chevron) |

Supporting values used directly (not tokenised): Elevated Navy `#112240` (audit ledger), Navy Hairline `#233554` (ledger borders), Emerald hover `#059669`, Emerald Soft `rgba(16,185,129,0.15)` (seal/tints).

**Purple/indigo is retired** across the system — with one granted exception: the `/experts` specialism chips (see *Chip palette* below; Lisa, 2026-06-11). No purple anywhere else.

### Chip palette (experts page only)

Original low-saturation multi-hue scheme, retained by **explicit operator decision (Lisa, 2026-06-11)** as a bounded exception to the brand's "no purple anywhere" rule — decorative, non-interactive category colour only:

| Group | Background | Border |
|---|---|---|
| Quality systems & audit (base `.chip`) | `rgba(99, 102, 241, 0.12)` | `rgba(99, 102, 241, 0.28)` |
| Regulatory submissions (`.chip-regulatory`) | `rgba(139, 92, 246, 0.12)` | `rgba(139, 92, 246, 0.30)` |
| Product safety (`.chip-safety`) | `rgba(6, 182, 212, 0.13)` | `rgba(6, 182, 212, 0.32)` |
| Design / software / clinical (`.chip-design`) | `rgba(59, 130, 246, 0.12)` | `rgba(59, 130, 246, 0.30)` |
| Standalone disciplines (`.chip-standalone`) | `rgba(100, 116, 139, 0.15)` | `rgba(100, 116, 139, 0.32)` |

Chip text is `--card-text` (passes AA on all tints). These hues must not migrate to any other component or surface.

## Typography

| Element | Font | Weight | Size |
|---|---|---|---|
| Hero `<h1>` (`.hero-bridge-headline`) | EB Garamond | 700 | `clamp(2.6rem, 7vw, 4.5rem)` |
| Page title (sub-pages) | EB Garamond | 700 | `clamp(2.2rem, 5vw, 3.2rem)` |
| Section heading (`.section-heading`) | EB Garamond | 700 | `clamp(1.8rem, 4vw, 2.6rem)` |
| Card `<h2>` | EB Garamond | 700 | `clamp(1.4rem, 3vw, 1.8rem)` |
| Body | Inter | 400 | `0.95rem` |
| CTA / nav | Inter | 500–600 | `0.8rem`–`0.95rem` |
| Audit timestamps, footer sign-off | JetBrains Mono / Fira Code / monospace | 400 | `0.72rem` |

### Page-title vertical stretch

`.page-title` and `.section-heading` use `transform: scaleY(1.15)` for serif elegance. Because the transform stretches glyphs but not the layout box, multi-line titles **must** carry an enlarged `line-height` (currently `1.5`) and increased `margin-bottom` to prevent descender/ascender collisions. Original `line-height: 1.25` is broken under the transform — do not regress.

## Layout

- Single column. `.container { max-width: 880px; margin: 0 auto; padding: 0 2rem; }`
- Dark pages: isometric cube SVG grid pattern at 18% opacity behind content (`.bg-pattern`), plus one `.authority-watermark` (white mark at 7%/5%) per page header. Journal page: single fixed `.journal-bg-mark` (navy mark, greyscaled, 5%).
- `html { scroll-behavior: smooth; scroll-padding-top: 4.5rem; }` on every page — the fixed nav is ~52px; anchor jumps land below it.
- Vertical rhythm: `.content-section { padding: 1.5rem 0; }` and `.content-card { margin-bottom: 1.5rem; }`. Gap-spacers `.section-gap` (2rem) and `.section-gap-lg` (3.5rem) on `index.html`.

### Breakpoints

| Width | Behaviour |
|---|---|
| `≤ 736px` (index only) | Stats grid collapses to single column; CTA grid collapses; glass-card padding reduces. |
| `≤ 640px` | Mobile breakpoint. Hamburger nav engages, glass-card padding reduces, flow steps go vertical. |
| `≤ 480px` | Hero `h1` shrinks; nav brand `<span>` hides; chip type reduces; regulatory-gap list rows stack vertically; cookie banner stacks. |
| `≤ 360px` | Hero `h1` shrinks further; CTA button padding reduces. |

## Components

### Bridge hero (`.hero-bridge`, index.html)

White hero card (2px emerald border, 20px radius) centred on the dark→light "bridge" gradient (`#0A192F` → `#F3F4F6`, 125deg; steeper 160deg variant ≤736px). EB Garamond headline in navy with `scaleY(1.12)`, italic emerald eyebrow below it, two watermark layers (white mark top-left at 7%, greyscaled navy mark bottom-right at 5%). CTA row: primary emerald `.scroll-btn` + `.scroll-btn-outline` (transparent, navy text, faint navy border).

### Glass card

White `#FFFFFF` surface, `border-radius: 24px` (16px on Journal), 2px emerald border on dark pages / 1px hairline on Journal, `padding: 4rem 3.5rem`, soft shadow. `.content-card` adds `margin-bottom: 1.5rem`. On `≤640px`, padding reduces and radius drops to 18px.

### Primary CTA button

Emerald `#10B981` fill, **Deep Navy `#0A192F` text**, full pill (50px radius), hover `#059669`. Outline variant (`.cta-btn.cta-outline`, contact page): transparent, `1.5px` solid `--link` border, `--link` text, fills emerald on hover. Hero secondary (`.scroll-btn-outline`, index): transparent, navy text, faint navy border.

### Nav (all six pages)

Fixed translucent bar (navy-tinted on dark pages, light-tinted on Journal), brand mark + wordmark left, links right, hamburger `≤640px`. Standard link set everywhere: Problem · Solution · About · For Experts · Early Access · Contact, plus a `.nav-cta` emerald pill — "Book a demo" (cal.eu) on index/about/contact, "Apply" (#apply) on experts.

- Current page marked with `aria-current="page"`, styled as an inset emerald underline; index runs an IntersectionObserver scroll-spy that applies the same `.is-active` style to in-page anchors.
- `aria-expanded`/`aria-controls` on the toggle; outside-click and **Escape** close the menu (Escape returns focus to the toggle).
- Nav logo: **white mark on dark navs, navy mark on the Journal nav** — never navy-on-navy.

### Breadcrumbs (sub-pages)

`.breadcrumbs` line above each sub-page title (`Home / <Page>`, 0.78rem muted, emerald `/` separator), mirroring the BreadcrumbList JSON-LD.

### Audit seal (`.audit-seal`)

Signature trust chip: Emerald Soft pill with `✓` prefix. Text `#047857` on white cards; `#10B981` inside the dark audit ledger (`.audit-ledger .audit-seal`). Used on the index Security feature, the audit-ledger header ("Audit Ready"), and as credential badges on `about.html`.

### Footer (all six pages)

Copyright ("PraxisVerify Limited"), `.footer-legal` line "Registered in Ireland · CRO 812849", standard link set (Home · About · For Experts · Contact · Privacy Policy · Terms of Service · LinkedIn), and a monospace `.footer-updated` sign-off: `Reviewed: YYYY-MM-DD · Lisa Donlon`.

### Flow steps (`.flow`)

Four-step numbered horizontal flow on desktop, vertical with left-rail connector on mobile. Numbered circles 48px, emerald background, navy numerals. Used on `index.html` and `experts.html`.

### FAQ accordion (experts.html)

Native `<details>/<summary>` — no JS. Emerald accents: open-state border, chevron tint, and a `?` badge (emerald fill, **navy** glyph) next to the heading.

### Stat cards (index.html)

Grid of three on desktop, single column `≤736px`. Smaller 16px-radius cards with large EB Garamond numerals in `#0A192F`.

### Cookie banner (all six pages)

Fixed at bottom, two-button (Accept / Decline) consent gating GA4 via Consent Mode v2. Choice persists in `localStorage` (`cookie_consent`), so the banner shows at most once per visitor across the site. GA4 head block + CSP meta replicated on every page.

## Accessibility

- WCAG 2.1 AA is a brand requirement. Emerald `#10B981` is never used as text on white (2.54:1) — `--link: #047857` covers that role. Button/badge text on emerald fills is Deep Navy.
- `a:focus-visible`/`button:focus-visible`: 2px emerald outline, 2px offset; `#047857` override inside white cards (3:1 non-text minimum); pill radius on buttons.
- Skip link (`.skip-link` → `#main-content`) on every page; `<main id="main-content">` everywhere.
- All nav toggles carry `aria-expanded` and `aria-controls`; hamburger is a real `<button>`; Escape closes the mobile menu.
- `prefers-reduced-motion` disables the stamp animation.
- Hero `<h1>` and section headings use real semantic tags; serif treatment is visual only.

## Assets

- Favicons: `img/brand/mark-adaptive.svg` (navy mark that flips white via `prefers-color-scheme: dark`), `img/pvlogo.png` PNG fallback, `/favicon-180.png` apple-touch icon (white mark on solid `#0A192F` — iOS composites transparency onto black).
- Social card: `img/social-card.png` (1200×630, exact `#0A192F`, white stacked logo, emerald italic tagline). Duplicates kept in sync: `img/brand/social-card-1200x630.png`, root `social-card-1200x630.png`. Template: `drafts/social-card.html`, rendered via headless Chrome at 1200×630.
- Brand asset source of truth pending the BrandKit → `~/Projects/praxisverify/brand/` promotion (Decision 010).

## Page patterns

Every page follows the same skeleton:

1. `<head>` — meta, CSP, GA4 + Consent Mode v2, Schema.org JSON-LD (WebPage/Organization/Person/Breadcrumbs/FAQPage/JobPosting as relevant), inline `<style>`.
2. Background layer — cube grid SVG (dark pages) or `.journal-bg-mark` (experts).
3. Skip link → `<nav class="site-nav">` fixed top bar.
4. `<header class="page-header">` — first glass card with breadcrumbs, title and subtitle.
5. `<main id="main-content">` → `<section>` → `<div class="container">` → glass cards.
6. `<footer class="footer-section">` — copyright, CRO line, links, monospace reviewed date.
7. Cookie banner + inline `<script>` (nav toggle, Escape handler, banner display; index adds fade-in observer and scroll-spy).

## Conventions

- **Datestamps:** every page carries `<meta name="date">`, JSON-LD `dateModified`, and a visible footer `<time datetime>`. Update all of them together (plus `sitemap.xml` lastmod and `llms.txt`) when shipping a content change.
- **Schema.org:** changes to visible FAQ or specialism content must be reflected in the FAQPage / JobPosting JSON-LD on the same page.
- **Legal entity:** "PraxisVerify Limited" in legal-weight contexts (footers, terms, privacy, schema `legalName`); plain "PraxisVerify" elsewhere. CRO 812849.
- **Abbreviations:** expand on first use per page, then abbreviate.
- **UK English** spelling throughout. Currency: € first, $ second.
- **No emojis** in copy unless explicitly approved.
- **Pillar discipline:** dark pages stay dark (Authority); `experts.html` stays light (Journal). Don't collapse the modes.

## Anti-patterns (don't do)

- No purple/indigo anywhere — retired with the old palette. (Granted exception: `/experts` chips only.)
- No white text on emerald `#10B981` (2.54:1 AA failure) — Deep Navy text, or `#047857` fill if white text is unavoidable.
- No emerald `#10B981` as *text* on white cards — use `--link: #047857`.
- Don't wrap the logo in a white container; don't put the navy mark on a dark nav.
- Don't use `rounded-md` (6px) on interactive elements — 8px minimum, full pills for CTAs.
- Don't use semantic status colours for non-status decoration.
- Don't add a build step or extract CSS to a stylesheet without a clear migration plan — the inline-CSS-per-page constraint is intentional.
- Don't drop `transform: scaleY(1.15)` from page titles without also dropping the `line-height: 1.5` compensation — they're paired.

## When this file should be updated

- New component pattern lands on any page.
- A CSS custom property is added, removed, or its meaning changes.
- A new breakpoint is introduced.
- An accessibility convention changes.
- A page-level deviation from these patterns is introduced and should be documented (or reverted).
