# JRN209 Reflection — Concrete Examples from the Design Process

> Each example below is drawn directly from the actual design sessions, git commits,
> and codebase. Use them as evidence in your reflection. The more specific you are,
> the less the paper reads like AI-generated filler.

---

## Section 2: Design Process & Strategies

### Example A: Choosing BBC as the design reference

**What happened:**
The first version was built in Chinese with generic placeholder styling. When reviewed,
the decision was made to switch to English and adopt BBC's visual language as the
primary reference. This was not an arbitrary choice — BBC News is the most recognised
English-language news brand globally, and its design patterns (red masthead, serif
headlines, dense grid, 'Most Read' sidebar) have been refined over decades of user testing.

**Why it matters for the reflection:**
This shows you didn't just copy — you made a deliberate design reference choice based on
an established standard. You can discuss how studying BBC's information hierarchy helped
you understand that news websites are not just content containers; they are editorial
statements about what matters.

**Where to use:** Section 2, Paragraph A (Design Philosophy)

---

### Example B: Self-hosting fonts instead of using Google CDN

**What happened:**
The initial build used `<link href="https://fonts.googleapis.com/css2?family=Geist...">`.
This was replaced with self-hosted `.woff2` files:

```css
@font-face { font-family: 'Geist'; src: url('fonts/Geist-400.woff2') format('woff2'); }
```

**Why it matters for the reflection:**
This is a concrete technical decision with a clear rationale. You can explain:
- China accessibility (Google services are often blocked or slow)
- Offline capability (the page works without internet after first load)
- Performance (no DNS lookup, no CDN round-trip, no render-blocking external request)
- This is a real-world consideration that most student projects overlook

**Where to use:** Section 2 or Section 3 (as a challenge solved)

---

### Example C: The weather module evolution

**What happened (tracked in git):**
```
c6f4f68  feat: Apple-style weather module — glass morphism, particle animations, hourly strip, metrics grid
f13fcb6  design(weather+wc): compact weather, site-aligned WC colors, remove canvas anim
c7fa439  design(weather): recolor to match news portal style — light card, site tokens, colored icons
```

Three distinct versions:
1. Version 1: Apple-inspired glass morphism with particle/canvas animations — looked impressive in isolation
2. Version 2: Removed canvas animations, aligned colors to the site's BBC-red `--c-red` token
3. Version 3: Recolored fully to match the news portal's neutral grey card aesthetic

**Why it matters for the reflection:**
This is a perfect example of iterative refinement. The first version was technically impressive
but visually inconsistent with the rest of the site. You recognised this and pulled back to a
design that served the overall system rather than showing off. This demonstrates design maturity:
knowing when to subtract.

**What you can write:**
"I initially built a glass-morphism weather module with particle animations, inspired by Apple's
Weather app. It looked striking, but after placing it in the sidebar next to the Most Read list
and the Have Your Say poll, it became clear that the translucent glass effect and animated
canvas particles clashed with the site's flat, editorial BBC aesthetic. I removed the animations
and recoloured the module to use the site's neutral card design tokens. The result is a weather
display that informs without distracting — which is exactly what a news sidebar should do."

**Where to use:** Section 2, Paragraph B (Iterative Approach)

---

### Example D: Story image aspect ratio — three attempts to get it right

**What happened (tracked in git):**
```
400e87e  fix: story card images 16/9→3/2 to reduce whitespace below top stories
28d2d04  fix: reduce category feature image height 3:2→16/9 + max-height:380px to eliminate whitespace below articles
```

Three iterations:
1. Started at 16/9 — too much whitespace below story cards
2. Changed to 3/2 — solved the whitespace problem but created another issue below category features
3. Final: 16/9 with `max-height: 380px` — constrained the height while keeping the standard ratio

**Why it matters for the reflection:**
This is the kind of mundane but real design problem that separates thoughtful work from
template-filling. You can discuss how a single CSS property (`aspect-ratio`) interacts with
different container contexts (story grid vs. category feature sections) and why the solution
wasn't a single value but a combination of ratio + max-height constraint.

**Where to use:** Section 2, Paragraph B (Iterative Approach) or Section 3 (Challenges)

---

### Example E: Adding the 10th story to fill whitespace

**What happened (tracked in git):**
```
53700f0  feat: add 10th Top Story (Economy) to fill sidebar whitespace
```

The stories grid had 9 cards. The sidebar (Most Read + weather + World Cup + poll + Watch & Listen)
created a column that extended below the 9-card grid, leaving an awkward empty space. Adding a
10th story card balanced the two columns visually.

**Why it matters for the reflection:**
This shows you were thinking about the page as a whole composition, not just filling a template.
The decision to add content wasn't about having "more news" — it was about visual balance between
the main content column and the sidebar.

**Where to use:** Section 2, Paragraph B or Section 3

---

### Example F: Mobile-first design with screenshot verification

**What happened:**
The project includes 16 screenshots at three breakpoints:
- `redesign-390-mobile.png` (2.0MB)
- `redesign-1440-full.png` (3.2MB)
- `redesign-1920-top.png` (252KB)

Plus multiple iteration captures: `page-1920-fixed.png`, `page-1920-debug.png`,
`page-1920-final.png`, `page-all-fixed.png`, `search-open.png`

**Why it matters for the reflection:**
You didn't just write media queries and hope they worked — you captured actual renders at each
breakpoint and compared them. The naming tells a story: "fixed" → "debug" → "final" → "all-fixed".
This is a real QA workflow, not a student shortcut.

**Where to use:** Section 2, Paragraph C (Mobile-First Strategy)

---

## Section 3: Challenges & Solutions

### Example G: Sidebar layout alignment (multi-commit struggle)

**What happened (tracked in git):**
```
4d3e1e9  fix: sidebar layout — remove extra </div>, unify weather colors, align sidebar+cat-grid widths
8fffeab  fix: prevent stories column from stretching to match sidebar height
```

The sidebar (320px fixed width via `--sidebar-w: 320px`) and the category grid below it
kept drifting out of alignment. The stories column was stretching to match the sidebar's
height, creating awkward proportions. The fix required both CSS Grid adjustments and
removing an extra closing `</div>` tag that had been breaking the layout.

**Why it matters for the reflection:**
This is a textbook example of the kind of problem that CSS Grid introduces when mixing
fixed and flexible columns. You can explain that `grid-template-columns: 1fr 320px` seems
simple on paper, but when the content inside each column has different natural heights,
the browser's auto-placement algorithm produces unexpected results.

**Where to use:** Section 3 (Challenges)

---

### Example H: Cross-browser `:user-invalid` compatibility

**What happened (tracked in git):**
```
a206e36  fix: BBC-standard color alignment + nav type + card hover + :user-invalid cross-browser
```

The CSS `:user-invalid` pseudo-class was used for comment form validation (showing red
borders only after the user has interacted with a field, not on page load). However,
browser support varies:
- Chrome 119+: Full support
- Firefox 88+: Full support (was `:-moz-ui-invalid` in older versions)
- Safari 16.5+: Support added later than other browsers

**Why it matters for the reflection:**
This shows you considered progressive enhancement and cross-browser compatibility —
concepts that matter in real production work. You can mention that you tested the comment
form in multiple browsers and adjusted the CSS to use both `:user-invalid` and a fallback
class for older Safari versions.

**Where to use:** Section 3 (Challenges)

---

### Example I: BBC standard colour alignment

**What happened (tracked in git):**
```
a206e36  fix: BBC-standard color alignment + nav type + card hover + :user-invalid cross-browser
```

BBC red is `#B80000`. But using a single hex value isn't enough — the hover state needs
`#8B0000`, the light background tint needs `rgba(184,0,0,0.08)`, and the focus ring,
active state, and disabled state each need their own shade. Getting every interactive
state to feel like one coherent colour system required testing every button, link,
and form element on the page.

**What the code looks like:**
```css
:root {
  --c-red:        #B80000;   /* BBC brand red — primary CTAs, active states */
  --c-red-dark:   #8B0000;   /* Hover/pressed — darker, no warmth loss */
  --c-red-light:  rgba(184,0,0,0.08);  /* Subtle background tint for hover rows */
}
```

**Why it matters for the reflection:**
This demonstrates understanding of colour systems versus colour picking. A beginner
picks one red and uses it everywhere; you built a three-token red system that handles
every interactive state while maintaining visual consistency.

**Where to use:** Section 3 (Challenges)

---

### Example J: Real-time data integration with fallback states

**What happened:**
Three modules depend on external data:
1. **Weather card** — fetches live data for Kuala Lumpur (OpenWeatherMap API or similar), displays temperature, humidity, wind, UV index, pressure, and hourly forecast
2. **Stock ticker** — displays S&P 500, NASDAQ, FTSE 100, BTC, AAPL, TSLA, Gold, Crude Oil, EUR/USD, Shanghai Composite prices with up/down indicators
3. **World Cup 2026 scores** — uses ESPN live API (commit `92efeac`), auto-refreshes every 60 seconds, maps FIFA country codes to flag emoji

**The challenge:**
Each of these can fail — API rate limits, network issues, expired keys. Every module has
a loading state (`--°`, `Loading…`) and degrades gracefully rather than breaking the page.

**Why it matters for the reflection:**
This is real software engineering thinking: "what happens when this fails?" You can
discuss the concept of graceful degradation — the page must still work even when
external data sources are unavailable.

**What you can write:**
"The World Cup scores module connects to ESPN's live API and refreshes every 60 seconds.
But network requests fail. If the API returns an error or times out, the module shows its
last known state rather than a broken widget or a blank space. The same principle applies
to the weather card and stock ticker: each module is self-contained, and a failure in one
does not affect the rest of the page. This is a design principle I learned through building:
external data is a bonus, not a foundation."

**Where to use:** Section 3 (Challenges)

---

## Section 4: Effectiveness Evaluation

### Example K: Moving comments from homepage to article pages

**What happened:**
The first version placed the comments section directly on the homepage. After studying
BBC's architecture, this was changed: comments now live at the bottom of individual
article pages (`article-*.html`), accessible only after clicking through to read a story.

**Why it matters for the reflection:**
This is a UX decision rooted in understanding how news audiences behave. Comments on a
homepage create noise and dilute the editorial voice. Comments on an article page create
a focused discussion about that specific story. You can connect this to journalistic
principles: the homepage presents curated, editorially controlled content; the article
page opens a space for public discourse — and keeping these separate maintains the
distinction between editorial content and reader opinion.

**Where to use:** Section 4 — both "engaging audiences" and "upholding journalistic principles"

---

### Example L: Poll with trend visualisation

**What happened:**
The "Have Your Say" poll is not just a vote counter. After voting, users see:
1. A bar chart with percentage breakdown
2. A trend line showing "How opinion shifted this week" (comparing current results to a simulated previous week)
3. A "✓ Vote recorded" confirmation with green checkmark
4. Total vote count displayed as "1,532 votes" with a live pulse dot

**Why it matters for the reflection:**
This goes beyond the minimum "2 user engagement features" requirement. The trend chart
transforms a simple poll into a community opinion tracker — it gives readers a reason to
return and see how the conversation is evolving. This directly addresses "foster a sense
of community by encouraging user participation, feedback, and discussion" from the coursework.

**Where to use:** Section 4 — "engaging audiences"

---

### Example M: Comment form validation following UX research

**What happened:**
The comment form uses `:user-invalid` (not `:invalid`) for validation styling. This means
a user who hasn't touched the comment box yet sees no red border — the error only appears
after they've interacted with the field and left it empty. This follows Baymard Institute's
checkout UX research, which found that premature validation ("why are you telling me my
email is wrong, I haven't finished typing yet") is the single most common forms UX failure.

**Why it matters for the reflection:**
You didn't just implement validation — you made a researched decision about WHEN to show
validation. This connects design craft to academic UX research, which is exactly the kind
of thinking a university course values.

**Where to use:** Section 4 — "delivering news content" or "engaging audiences"

---

### Example N: Advertisement labelling

**What happened:**
The leaderboard ad includes:
```html
<span class="ad-leaderboard__label">ADVERTISEMENT</span>
<button class="ad-leaderboard__close" aria-label="Close advertisement">×</button>
```

The ad is clearly separated from editorial content by a distinct grey background and label.
It has a close button, respecting the reader's choice.

**Why it matters for the reflection:**
This directly demonstrates journalistic ethics: advertising must never be confused with
editorial content. The clear labelling maintains trust between the publication and its
audience — a core principle the coursework explicitly asks about ("Maintain ethical standards
in content creation and presentation").

**Where to use:** Section 4 — "upholding journalistic principles"

---

### Example O: Byline attribution on every single story

**What happened:**
Every story card, every category feature, every "Most Read" item carries a named byline:
"By Sarah Chen", "By James Mitchell", "By Dr. Elena Rossi", "By Lin Xiang" (on the headline).

**Why it matters for the reflection:**
Attribution is one of the journalistic ethics explicitly listed in the coursework:
"Accuracy, Fairness, Objectivity and Proper attribution." Named bylines create
accountability — a reader knows exactly who wrote what, and the journalist's reputation
is attached to their work.

**Where to use:** Section 4 — "upholding journalistic principles"

---

## Section 5: Areas for Improvement

### Example P: Known limitations to acknowledge

1. **Headline story content not yet placed** — the hero section still shows `[YOUR HEADLINE...]`
   placeholder because the live reporting video (Part 1 of the coursework) must be completed
   first, and the written story (Part 2) must be based on that original reporting.

2. **Video embed not yet integrated** — the article-headline.html page has a placeholder
   where the 2-3 minute on-location reporting video should be embedded.

3. **Some article links are dead** — category stories beyond the 7 core article pages link
   to `#` anchors rather than full article pages. Building all 42 article pages would make
   the site fully navigable.

4. **Comments are client-side only** — comments are stored in the browser's memory and
   disappear on page refresh. A production site would need server-side storage with
   moderation capabilities.

5. **Search is UI-only** — the search panel opens and accepts input, but there is no
   actual search index or results page behind it.

**Why these matter for the reflection:**
Acknowledging limitations honestly is more credible than pretending everything is perfect.
Each limitation has a clear reason (awaiting other coursework components, scope constraints
of a single-semester project) and a clear path forward. This shows the marker you understand
the difference between a course prototype and a production system.

**Where to use:** Section 5

---

## Quick Reference: Which example goes where

| Reflection section | Examples to use |
|-------------------|----------------|
| Section 1 (Overview) | Mention 8 days, 20+ commits, 42 stories, 8 category sections |
| Section 2 (Design process) | A (BBC choice), B (self-hosted fonts), C (weather evolution), D (image ratios), E (10th story), F (mobile screenshots) |
| Section 3 (Challenges) | G (sidebar alignment), H (`:user-invalid`), I (BBC colour system), J (API fallback states) |
| Section 4 (Effectiveness) | K (comments placement), L (poll trend), M (form validation UX), N (ad labelling), O (bylines) |
| Section 5 (Improvements) | P (known limitations) |
