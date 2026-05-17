# praxisverify.com — Design Notes

A working reference for what's actually implemented on the marketing site. Not the brand system itself — that lives in the `pv-branding` skill (`~/.claude/skills/pv-branding/SKILL.md`), which is the canonical source for colour, typography, and component rules across all surfaces (website, MVP platform, admin tool, pitch decks). This file is the site-specific snapshot: the tokens, components, and conventions actually shipped to `praxisverify.com`.

If `pv-branding` and this file disagree, the brand skill wins and this file should be updated.

## Stack & conventions

| Item | Choice |
|---|---|
| Markup | Plain HTML, no framework |
| Styles | Inline `<style>` block per page — no external stylesheet, no preprocessor |
| Scripts | Inline `<script>` — fade-in IntersectionObserver, cookie consent, nav hamburger toggle |
| Hosting | GitHub Pages from `master`; Cloudflare in front for security headers and TLS |
| Build | None — files served as-is |
| Deploy | `git push origin master` → GitHub Pages rebuilds in ~1–2 min |

Pages: `index.html`, `experts.html`, `about.html`, `contact.html`, `privacy.html`, `terms.html`.

Each page carries its own copy of the CSS block. Changes to shared tokens or components must be repeated across all six files — there is no shared stylesheet. When changing a token, grep for it across the directory.

## Colour tokens

Custom properties declared on `:root` in every page:

| Token | Value | Use |
|---|---|---|
| `--bg` | `#0f172a` | Page background (Slate 950) |
| `--surface` | `rgba(235, 238, 248, 0.82)` | Glass-card surface |
| `--border` | `rgba(255, 255, 255, 0.08)` | Card / nav border on dark |
| `--card-text` | `#1e293b` | Headings on glass cards (Deep Navy) |
| `--card-text-muted` | `#35353f` | Body text on glass cards |
| `--text` | `#e2e2ea` (`#c8c8d0` on some pages) | Body text on dark background |
| `--text-muted` | `#b8b8c8` (`#8a8a98` on some pages) | Secondary text on dark |
| `--btn-bg` | `#166534` | Primary CTA — Deep Bottle Green |
| `--btn-text` | `#ffffff` | Button text |
| `--accent-platform` | `#6366f1` | Indigo accent (zoning only — see below) |

**Inconsistency to note:** `--text` and `--text-muted` differ between `index.html` (lighter) and `about.html` / `contact.html` (darker). Either intentional and should be documented per page, or drift — flag if standardising.

### Chip palette (experts page only)

Specialism chips use low-saturation cool tones — chips themselves are not interactive, so colour conveys category, not status:

| Group | Background | Border |
|---|---|---|
| Quality systems & audit | `rgba(99, 102, 241, 0.12)` | `rgba(99, 102, 241, 0.28)` |
| Regulatory submissions (`.chip-regulatory`) | `rgba(139, 92, 246, 0.12)` | `rgba(139, 92, 246, 0.30)` |
| Product safety (`.chip-safety`) | `rgba(6, 182, 212, 0.13)` | `rgba(6, 182, 212, 0.32)` |
| Design / software / clinical (`.chip-design`) | `rgba(59, 130, 246, 0.12)` | `rgba(59, 130, 246, 0.30)` |
| Standalone disciplines (`.chip-standalone`) | `rgba(100, 116, 139, 0.15)` | `rgba(100, 116, 139, 0.32)` |

### Indigo usage rule

`--accent-platform: #6366f1` is the MVP platform's action colour. On the marketing site it is used **only for zoning** — never as a primary CTA. Specifically:
- Left border on `experts.html` page-subtitle
- Border on the indicative-terms banner at the top of `/experts`
- `?` badge next to the FAQ heading on `/experts`
- Chevron tint when a FAQ accordion is open
- Quality-systems chip group accent

The primary CTA stays Bottle Green `#166534` — the indigo `#6366f1` fails WCAG AA on the light glass-card surface for action elements.

## Typography

| Element | Font | Weight | Size |
|---|---|---|---|
| Hero `<h1>` | EB Garamond | 700 | `clamp(2.6rem, 6vw, 3.8rem)` |
| Page title (sub-pages) | EB Garamond | 700 | `clamp(2.2rem, 5vw, 3.2rem)` |
| Section heading (`.section-heading`) | EB Garamond | 700 | `clamp(1.8rem, 4vw, 2.6rem)` |
| Card `<h2>` | EB Garamond | 700 | `clamp(1.4rem, 3vw, 1.8rem)` |
| Body | Inter | 400 | `0.95rem` |
| CTA / nav | Inter | 500 | `0.9rem`–`0.95rem` |

### Page-title vertical stretch

`.page-title` and `.section-heading` use `transform: scaleY(1.15)` for serif elegance. Because the transform stretches glyphs but not the layout box, multi-line titles **must** carry an enlarged `line-height` (currently `1.5`) and increased `margin-bottom` to prevent descender/ascender collisions. Original `line-height: 1.25` is broken under the transform — do not regress.

## Layout

- Single column. `.container { max-width: 880px; margin: 0 auto; padding: 0 2rem; }`
- Page background fills viewport; isometric cube SVG grid pattern at 18% opacity sits behind content (`.bg-pattern`, fixed, `inset: 0`).
- Vertical rhythm: `.content-section { padding: 1.5rem 0; }` and `.content-card { margin-bottom: 1.5rem; }`. Gap-spacers `.section-gap` (2rem) and `.section-gap-lg` (3.5rem) for hero-to-stats and similar transitions on `index.html`.

### Breakpoints

| Width | Behaviour |
|---|---|
| `≤ 736px` (index only) | Stats grid collapses to single column; CTA grid collapses; glass-card padding reduces. |
| `≤ 640px` | Mobile breakpoint. Hamburger nav engages, glass-card padding reduces to `2.5rem 1.5rem`, flow steps go vertical, FAQ touch targets size up. |
| `≤ 480px` | Hero `h1` shrinks; brand name `<span>` hides next to the nav logo (leaves the logo only); chip type size reduces. |
| `≤ 360px` | Hero `h1` shrinks further; CTA button padding reduces. |

## Components

### Glass card

```css
.glass-card {
    background: var(--surface);
    backdrop-filter: blur(20px) saturate(1.2);
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.06);
    padding: 4rem 3.5rem;
    color: var(--card-text);
    box-shadow: 0 8px 40px rgba(0, 0, 0, 0.15);
}
```

`.content-card` adds `margin-bottom: 1.5rem`. On `≤640px`, padding reduces to `2.5rem 1.5rem` and radius to `18px`.

### Primary CTA button

```css
.cta-btn {
    background: var(--btn-bg);          /* #166534 */
    color: var(--btn-text);
    padding: 0.9rem 2rem;
    border-radius: 50px;                /* full pill */
    font-weight: 500;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}
.cta-btn:hover { background: #14532d; transform: translateY(-1px); }
```

Outline variant (`.cta-btn.cta-outline`) on `contact.html` for secondary actions: transparent background, `1.5px` solid bottle-green border, fills on hover.

### Nav + hamburger (≤640px)

Same nav across all six pages (except `experts.html`, which uses an expert-context variant: `Apply | Rates | FAQ | Back to main site`).

Hamburger button hidden on desktop. At `≤640px` the nav links list collapses to a `position: absolute` dropdown beneath the nav bar, animated via `max-height` transition. `aria-expanded` toggled by `toggleNav(btn)` inline JS; outside-click closes the menu. Native semantics — no library.

### Flow steps (`.flow`)

Four-step numbered horizontal flow on desktop (`grid-template-columns: repeat(4, 1fr)`), collapses to vertical on mobile with the connector line rotated to a left-rail. Numbered circles `48px`, Bottle Green background. Used on `index.html` and `experts.html`.

### FAQ accordion (experts.html)

Native `<details>/<summary>` — no JS. Each `<details class="faq-item">` is a pill-shaped card with a chevron indicator that rotates on open. The whole FAQ card carries an indigo `?` badge next to the heading. Open state gets a brighter background and an indigo border tint.

### Chips (experts.html)

Pill-shaped (`border-radius: 999px`), small (`font-size: 0.82rem`), used in `.chip-grid` flexbox rows. Group-specific accent classes listed above. Non-interactive — colour conveys category only.

### Stat cards (index.html)

Grid of three on desktop, single column on `≤736px`. Each is a smaller `border-radius: 16px` glass card with a large EB Garamond numeral.

### Cookie banner (index.html)

Fixed at bottom, glass surface, two-button (Accept / Decline) consent. Gates GA4 via Consent Mode v2. Choice persists in `localStorage`. Banner hides once a choice is made.

## Accessibility

- All nav toggles carry `aria-expanded` and `aria-controls`.
- Hamburger uses a real `<button>` element.
- `:focus-visible` outline on FAQ summaries uses `--accent-platform` at `2px` with `2px` offset.
- Skip link `.skip-link` on `index.html` jumps to `#main-content`.
- Colour contrast: body text on glass cards passes AA at 13:1+. CTA bottle-green on glass passes AA at 4.1:1.
- Hero `<h1>` and section headings use real semantic tags; serif treatment is visual only.

## Page patterns

Every page follows the same skeleton:

1. `<head>` — meta, Schema.org JSON-LD (WebPage/Organization/Person/Breadcrumbs/FAQPage/JobPosting as relevant), inline `<style>`.
2. `<svg class="bg-pattern">` — fixed background cube grid.
3. `<nav class="site-nav">` — fixed top bar with brand, hamburger, links.
4. `<header class="page-header">` — first glass card with title and subtitle.
5. `<main>` → `<section class="content-section">` → `<div class="container">` → one or more `<div class="glass-card content-card">`.
6. `<footer class="footer-section">` — copyright, footer links, last-updated `<time>`.
7. Inline `<script>` at end of body for nav toggle (and on `index.html` for fade-in observer and cookie banner).

## Conventions

- **Datestamps:** every page carries `<meta name="date">`, JSON-LD `dateModified`, and a visible footer `<time datetime>`. Update all three together when shipping a content change.
- **Schema.org:** changes to visible FAQ or specialism content must be reflected in the FAQPage / JobPosting JSON-LD on the same page.
- **Abbreviations:** expand on first use per page (e.g. "Quality Management System (QMS)") then use the abbreviation. Industry abbreviations explained: see `experts.html` for the canonical list.
- **UK English** spelling throughout. Currency: € first, $ second.
- **No emojis** in copy unless explicitly approved.
- **No light mode** without explicit approval — dark navy + glass cards is the intended primary experience.

## Anti-patterns (don't do)

- Don't introduce indigo `#6366f1` as a CTA colour on the marketing site (fails WCAG on glass cards).
- Don't wrap the logo in a white container.
- Don't use `rounded-md` (6px) on interactive elements — `rounded-lg` (8px) minimum, full pills for CTAs.
- Don't use semantic status colours (success/warning/danger/info) for non-status decoration.
- Don't add a build step or extract CSS to a stylesheet without a clear migration plan — the inline-CSS-per-page constraint is intentional (zero build, edits land directly).
- Don't drop `transform: scaleY(1.15)` from page titles without also dropping the `line-height: 1.5` compensation — they're paired.

## When this file should be updated

- New component pattern lands on any page.
- A CSS custom property is added, removed, or its meaning changes.
- A new breakpoint is introduced.
- An accessibility convention changes.
- A page-level deviation from these patterns is introduced and should be documented (or reverted).
