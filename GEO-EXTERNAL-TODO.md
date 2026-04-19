# GEO External Platform To-Do List

Brand Authority scored **32/100** in the April 2026 GEO audit. These non-code actions target **95+ GEO score**.

Last updated: 2026-04-19

---

## 1. LinkedIn Company Page (Critical — +3-5 GEO points)

LinkedIn (DA 98) is heavily weighted by ChatGPT and Bing Copilot for B2B SaaS.

- [ ] Verify the Company Page at linkedin.com/company/praxisverify — ensure it has logo, banner, description, website URL, industry (Medical Devices), and company size
- [ ] Publish 2 LinkedIn articles per week on regulatory topics (EU MDR lifecycle obligations, ISO 13485 common findings, 510(k) predicate device pitfalls). These enter ChatGPT's training data
- [ ] Cross-link: Company page → praxisverify.com. Personal profile → company page. Articles should link back to relevant site pages
- [ ] Engage on others' posts in MedTech/regulatory space — comments from your profile build entity association

## 2. YouTube Channel (+2-3 GEO points)

Gemini and Google AI Overviews heavily index YouTube transcripts. The VideoObject schema on the site is currently "orphaned" — it references a video on Leap Compliance's channel but there's no PraxisVerify channel.

- [ ] Create youtube.com/@praxisverify channel with company branding
- [ ] Upload the Leap Compliance video (or link/playlist it — check with Leap Compliance about cross-posting rights)
- [ ] Record 2-3 short videos (3-5 min each):
  - "What is Expert-in-the-Loop Verification?" — definitional content Gemini can cite
  - "How PraxisVerify Works" — screen walkthrough or animated explainer
  - "EU MDR Lifecycle Obligations Explained" — educational, positions you as thought leader
- [ ] Add captions/subtitles to all videos — YouTube auto-generates transcripts but manual captions are more accurate for AI indexing
- [ ] Update site schema `sameAs` links to include the YouTube channel URL once created

## 3. Bing Webmaster Tools + IndexNow (+2 GEO points)

Bing Copilot can't find you quickly without IndexNow. Currently zero Bing optimisation detected.

- [ ] Sign up at bing.com/webmasters — verify praxisverify.com ownership (DNS TXT record or CNAME)
- [ ] Submit sitemap.xml via the Bing dashboard
- [ ] Generate an IndexNow API key — Bing dashboard provides one. The key file can then be added to the site repo so every push triggers instant re-indexing
- [ ] Link your LinkedIn profile in Bing Webmaster Tools (social profiles section weights B2B content)

## 4. Wikipedia / Wikidata (+2-3 GEO points)

Google Knowledge Graph and ChatGPT use Wikidata for entity disambiguation. Without it, "PraxisVerify" gets confused with the Greek philosophical concept "praxis."

### Wikidata (do first — no notability requirement)

- [ ] Create a Wikidata item at wikidata.org for PraxisVerify:
  - Instance of: software company (Q638257) or technology company (Q18388277)
  - Country: Ireland (Q27)
  - Industry: medical device (Q170417)
  - Official website: https://praxisverify.com
  - Founded: 2025
  - Founder: Lisa Donlon (create a separate Wikidata item if one doesn't exist)

### Wikipedia (medium-term — needs notability)

- [ ] Assess notability — Wikipedia requires coverage in independent reliable sources. Prerequisites:
  - 2-3 press mentions in industry publications (e.g., Irish Medical Times, MedTech Europe news, Silicon Republic, Irish Times business)
  - A notable funding round or award (e.g., Enterprise Ireland HPSU, NDRC)
  - Then create a draft article via Wikipedia's Articles for Creation process
- [ ] Priority: get press coverage first — pitch to Irish tech/biopharma media. The "founded by former NSAI Notified Body decision maker" angle is genuinely newsworthy

## 5. Reddit Engagement (+1-2 GEO points)

Perplexity and ChatGPT heavily weight Reddit discussions. Organic mentions in regulatory subreddits provide authenticity signals.

- [ ] Create a Reddit account (personal, not branded — Reddit penalises corporate accounts)
- [ ] Engage authentically in these subreddits:
  - r/regulatoryaffairs (~15K members)
  - r/medicaldevices (~5K members)
  - r/qualitymanagement
  - r/biotech
- [ ] Answer questions about EU MDR, ISO 13485, 510(k) processes from your expertise. Don't promote PraxisVerify directly — build authority through helpful answers. When naturally relevant, mention the platform
- [ ] Post original content — e.g., "Lessons from reviewing 510(k) submissions as a former Notified Body decision maker" would get significant engagement

## 6. Industry Directories (+1 GEO point)

- [ ] Crunchbase — create a company profile (free tier) with founding date, industry, website, founder
- [ ] RAPS (Regulatory Affairs Professionals Society) — if there's a vendor directory, get listed
- [ ] Enterprise Ireland portfolio — ensure PraxisVerify appears in their supported companies list if applicable
- [ ] G2 / Capterra — create a product listing (even pre-launch, you can claim the profile)

---

## Estimated Impact by Timeline

| Phase | Actions | GEO Impact |
|-------|---------|-----------|
| **Week 1** | LinkedIn page + Bing Webmaster + Wikidata | +5-7 pts |
| **Week 2-4** | YouTube channel + 2 videos + LinkedIn articles | +3-5 pts |
| **Month 2-3** | Reddit engagement + press pitches + directories | +2-3 pts |
| **Month 3-6** | Wikipedia (after press coverage) + video library | +2 pts |
