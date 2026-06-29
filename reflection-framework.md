# JRN209 Reflection — Writing Framework

## Assignment Requirements (verbatim from coursework)
- **2 pages**, double-spaced, Times New Roman 12pt, 1-inch margins, justified
- Discuss: experience, challenges, strategies, lessons learned
- Evaluate effectiveness: engaging audiences, delivering news, upholding journalistic principles
- Identify: areas for improvement + future development

---

## Suggested Structure (5 sections, ~2 pages)

### Section 1: Introduction — Project Overview (1 paragraph)
**What to cover:**
- What you built: a multi-page online news portal (BBC-style)
- Your role: full website design + development + multimedia integration + user engagement features
- Tech choice: pure HTML/CSS/JS (self-hosted fonts, zero external dependencies)
- Brief mention: 8 days of iterative design, 20+ revisions, 16 screenshots at 3 breakpoints for QA

**Connect to coursework:** Mention CLO 3 ("produce online news package") and how this project demonstrates it.

### Section 2: Design Process & Strategies (2-3 paragraphs)
**What to cover — use real examples from your git log:**

*Paragraph A — Design Philosophy:*
- Chose BBC-style because it's the gold standard for news UX: clean hierarchy, serif headlines for authority, sans-serif body for readability, red brand accent for urgency
- Reference your decision to study WIRED + The Verge design systems (via Open Design) before building
- Why self-hosted fonts matter: China accessibility, no Google CDN dependency, faster load

*Paragraph B — Iterative Approach:*
- V1→V3→V4→FINAL evolution (cite your commit messages)
- Example 1: weather module went from Apple glass-morphism → compact card design that matched site tokens (commit `f13fcb6`)
- Example 2: story image ratios went 16/9→3/2→16/9+max-height after testing (commits `400e87e`, `28d2d04`)
- Example 3: sidebar layout alignment took multiple commits to get right (`8fffeab`, `4d3e1e9`)
- Example 4: added a 10th story to fill sidebar whitespace (`53700f0`)

*Paragraph C — Mobile-First Strategy:*
- Designed for 390px mobile first, then 1440px tablet, then 1920px desktop
- Screenshots at every breakpoint to verify (mention your 16 PNG captures)
- Hamburger menu, touch targets ≥44px, scroll-padding for sticky header

### Section 3: Challenges & Solutions (2 paragraphs)
**Pick 3-4 real challenges from your experience:**

*Challenge 1 — BBC Standard Colour Alignment:*
- Getting the exact BBC red (#B80000) to work across all states (hover, active, focus, disabled)
- Solution: tested every interactive state, fixed with commit `a206e36` ("BBC-standard color alignment + nav type + card hover + :user-invalid cross-browser")

*Challenge 2 — Cross-Browser CSS Compatibility:*
- `:user-invalid` pseudo-class behaviour differs across browsers
- Solution: tested across Chrome, Firefox, Safari; added fallback patterns (commit `a206e36`)

*Challenge 3 — Layout Alignment:*
- Sidebar height not matching category grid → whitespace gaps
- Story column stretching to match sidebar → awkward proportions
- Solution: iterative CSS Grid adjustments with `align-items: start` and max-height constraints

*Challenge 4 — Real-Time Data Integration:*
- Weather API (Kuala Lumpur live data), stock ticker, World Cup scores via ESPN API
- Balancing real-time functionality with fallback states for failed API calls

### Section 4: Effectiveness Evaluation (2 paragraphs)
**Address the 3 dimensions the coursework specifically asks about:**

*Engaging Audiences:*
- Poll with trend chart ("How opinion shifted this week") — not just a vote, shows community opinion movement
- Live World Cup scores with green "Live" indicator — real-time sports engagement
- "Most Read" list ranked by read count numbers
- Watch & Listen sidebar with embedded BBC/Reuters videos + BBC World Service live audio
- Comment sections on every article page (moved from homepage per BBC convention)
- Stock ticker for business readers

*Delivering News Content:*
- Inverted pyramid structure: hero headline → top stories → 8 category sections
- Mono uppercase kickers on every story card (BBC convention for scannability)
- Read counts create social proof and content hierarchy
- Mobile-responsive: same content, reflowed layout

*Upholding Journalistic Principles:*
- Clear byline attribution on every story (accuracy + accountability)
- Separation of news from opinion (Opinion/Commentary section distinct from news feed)
- Advertisement clearly labelled "ADVERTISEMENT" with close button
- Proper source attribution in article body text
- Ethical considerations: no clickbait headlines, factual tone throughout

### Section 5: Areas for Improvement & Future Development (1-2 paragraphs)
**Be honest but constructive:**

*Current Limitations:*
- Headline story content and video still to be added (awaiting on-location reporting footage)
- Some secondary stories link to `#` anchors (article pages not yet created for all 42 stories)
- No backend/CMS; content is hardcoded HTML (acceptable for a course prototype, not production)
- Search panel is UI-only (no actual search index)
- Comments are client-side only (not persisted to a server)

*Future Development:*
- Integrate the live reporting video into the headline article page
- Build remaining article pages for category stories
- Add a simple CMS (e.g., WordPress headless or static site generator) for content management
- Implement server-side comment storage with moderation
- Add newsletter signup with email integration
- Explore WebP image format for faster page loads
- Add dark mode toggle

---

## Key Journalism Concepts to Weave In
(Use these naturally, not as a checklist)

| Concept | Where to mention |
|---------|-----------------|
| Inverted pyramid | Section 4 — how stories are structured on the page |
| News values (timeliness, proximity, impact) | Section 2 — why real-time data (weather, stocks, scores) matters |
| Attribution | Section 4 — bylines, source citations |
| Audience engagement | Section 4 — poll, comments, live scores |
| Mobile-first / responsive design | Section 2 or 3 — design strategy |
| Multimedia storytelling | Section 2 — video, audio, images, data viz |
| Digital journalism landscape | Section 1 or 5 — why online news packages matter |
| Ethical standards | Section 4 — ad labelling, accuracy, fairness |

---

## Writing Rules (from your CLAUDE.md)
- **No em dashes (破折号)** — use commas, colons, or parentheses instead
- **APA parenthetical citations** if referencing any sources — e.g., (Connell, 2024)
- **No AI-generated filler** — empty platitudes like "this was a valuable learning experience" without specifics will get flagged
- **Be specific**: name actual commits, actual CSS properties, actual design decisions you made
- **Voice**: professional but personal — this is YOUR reflection, use "I"

---

## Sample Opening Paragraph (for tone reference only — rewrite in your own words)

> This reflection examines the process of designing and developing an online news portal for the JRN209 final project. The website was built from the ground up using HTML, CSS, and JavaScript, following a BBC-inspired editorial design with self-hosted fonts and zero external dependencies. Over eight days of iterative development spanning more than twenty design revisions, the project evolved from a basic six-story homepage into a fully-featured news platform with 42 stories across eight category sections, real-time data modules, and multiple audience engagement features. This paper discusses the design strategies, technical challenges, and editorial decisions that shaped the final product, and evaluates its effectiveness in delivering news content, engaging readers, and upholding journalistic standards.

---

## Formatting Checklist (for submission)
- [ ] Times New Roman, 12pt
- [ ] Double-spaced (2.0 line spacing)
- [ ] 1-inch (2.54cm) margins on all sides
- [ ] Page numbers, bottom centre
- [ ] Justified alignment
- [ ] 2 pages exactly
- [ ] Softcopy in WORD (.docx) format
- [ ] Filename: GroupLeaderName_GroupLeaderStudentID
