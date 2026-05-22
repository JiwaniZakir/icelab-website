# World-Class Research Lab Websites: Deep Structural & Design Analysis

*Compiled 2026-05-22 for ICE Lab website design decisions*

---

## Executive Summary

After analyzing 15+ research lab websites spanning CS/AI, electrical engineering, and IC design, I identified **6 distinct archetypes** and **12 universal design patterns** that define how the best labs present themselves online.

---

## The 6 Lab Website Archetypes

### 1. The Institute (Stanford HAI, MIT CSAIL)
- **Nav:** About | Research | People | Education | Policy | News | Events
- **Hero:** Full-width video/image with mission statement
- **Key trait:** Mission-pillar organization (Research/Education/Policy)
- **People:** 300+ members, filterable by role, with rich cards
- **Best for:** Large multi-PI institutes with diverse missions

### 2. The Product-Research Hybrid (DeepMind, Google Research)
- **Nav:** Models | Research | Science | Responsibility | About | Blog
- **Hero:** Product showcase carousel with animated content
- **Key trait:** Research areas as taxonomy (17 areas at Google Research)
- **People:** Not prominent -- emphasis on work output and products
- **Best for:** Industry labs where research ships as products

### 3. The Blog-First Lab (BAIR Berkeley)
- **Nav:** Minimal -- just a hero splash + blog feed
- **Hero:** Animated gradient logo with institutional branding
- **Key trait:** Research communication via long-form blog posts
- **People:** Separate from main site
- **Best for:** Labs that prioritize public-facing research communication

### 4. The Classic IC Lab (Razavi/UCLA, NanoCAD/UCLA, CISL/Columbia)
- **Nav:** Director | Students | Alumni | Present Work | Past Work | Publications | Awards | Teaching | Sponsors
- **Hero:** PI headshot + lab description (1 paragraph)
- **Key trait:** Sidebar navigation, PI-centric, publication-heavy
- **People:** Simple list with photos and short bios
- **Best for:** Single-PI hardware/EE labs (traditional, functional)

### 5. The Modern Academic Group (Sailing Lab/CMU, al-folio sites)
- **Nav:** About | People | Publications | Open-Source | Sponsors | Talks
- **Hero:** Lab name + news feed on homepage
- **Key trait:** Card grid for members + project categories
- **People:** Grid of hoverable cards grouped by role (Faculty/Current/Alumni)
- **Best for:** Mid-size academic labs wanting modern aesthetics with low maintenance

### 6. The Research Center (BWRC Berkeley, Stanford VLSI)
- **Nav:** Research | People | News & Events | Sponsors | Resources | Contact
- **Hero:** News carousel + sponsor logos
- **Key trait:** Industry membership prominently featured, seminar series
- **People:** Filterable by role (Faculty Directors/GSR/Postdoc/Staff)
- **Best for:** Multi-PI centers with industry partnerships

---

## Deep Dive: How the Best Labs Present Each Section

### A. Homepage / Landing Page

| Lab | Hero Type | Content Below Hero | CTA |
|-----|-----------|-------------------|-----|
| **Stanford HAI** | Full-width video + mission statement | 3 pillars (Research/Education/Policy) with feature cards, then news carousel, then quote carousel | "Engage With HAI" |
| **DeepMind** | Product launch video carousel (7 slides) | Latest News (8 items), Models showcase (7 cards), Podcast section | "Learn more" / "Try" per product |
| **Google Research** | Impact narrative ("We're advancing knowledge") | 17 research area cards, Impact stories, Community resources | "Explore all research areas" |
| **BWRC** | News carousel | Seminar schedule, Sponsor logos, Quick links | "Join BWRC" |
| **Stanford VLSI** | Featured research card | Project cards, Contact sidebar | None (info-first) |
| **Razavi Lab** | PI headshot + 1-paragraph description | Link list (sidebar nav) | None |
| **Sailing Lab** | Lab name + news feed | Just news | None |
| **MIT Media Lab** | News feed | Group directory | None |

**Best practice pattern:**
```
Hero section (lab name + tagline + visual)
   ↓
Research highlights (2-3 featured cards)
   ↓
Recent news/announcements (3-5 items)
   ↓
Quick links (Join us / Contact / Sponsors)
```

### B. Team / People Page

This is where labs diverge most. Here's how each handles it:

| Lab | Layout | Grouping | Card Content | Linking |
|-----|--------|----------|--------------|---------|
| **Stanford HAI** | Card grid, filterable | Leadership > Associate Directors > Faculty > Staff > Students > Fellows | Photo, Name, Title, Department | Individual profile pages |
| **DeepMind** | Not prominent | N/A | N/A | N/A |
| **BWRC** | List/grid, filterable | Faculty Directors > GSR > Postdoc > Staff | Photo, Name, Research area | Profile pages |
| **Stanford VLSI** | Card grid | Faculty > Researcher > Student > Alumni | Photo, Name | Individual pages |
| **Sailing Lab** | Card grid (al-folio `_projects`) | Faculty > Current (CMU) > Current (MBZUAI) > Alumni | Photo, Name, Title, redirect to personal site | External redirect |
| **Razavi Lab** | Paragraph list | Current Students (inline) | Photo + bio paragraph | Email links |
| **MIT CoCoSci** | Dedicated page | PI first, then group | Photos, Names | Google Scholar link |
| **Greene Lab** | Portrait grid | PI > Team > Alumni > Funding | Circular photo, Name, Role, Affiliation, Social links | Individual member pages |
| **NanoCAD** | List | Members page | Names, Titles | N/A |
| **CISL Columbia** | Photo grid | Faculty only | Photo, Name, Title | Individual group websites |

**Best practice pattern for IC labs:**
```
1. Faculty/PI section: Large photo + full bio + social links
2. Current students: Grid of cards (photo, name, degree, research topic)
3. Staff: Simple list
4. Alumni: Compact grid with name + current position + destination
```

### C. Research / Projects Page

| Lab | Organization | Presentation |
|-----|-------------|--------------|
| **Stanford HAI** | By mission pillar + grants | Feature cards with rich descriptions, tagged by topic |
| **Google Research** | 17 research area taxonomy | Area cards with descriptions, each linking to dedicated page |
| **DeepMind** | By product/system | Rich product pages with interactive demos |
| **BWRC** | By research area (3 themes) | Card grid with project thumbnails |
| **Stanford VLSI** | By project name (8 projects) | Card grid with thumbnails + descriptions |
| **Razavi Lab** | Present Work / Past Work split | Publication-style list with figures |
| **Sailing Lab** | Projects as cards | al-folio card grid with repo links |
| **NanoCAD** | Current Themes / Past Themes | Hierarchical sub-pages per theme |

**Best practice pattern for IC labs:**
```
1. Active research areas (2-4 themes, each with:)
   - 1-paragraph description
   - Representative figure/chip photo
   - Key publications
   - Involved students
2. Completed/past projects section
3. Research facilities & tools (EDA, measurement, fab access)
```

### D. Publications Page

| Lab | Format | Features |
|-----|--------|----------|
| **Stanford HAI** | Filterable list | Topic tags, date range, search |
| **Google Research** | Searchable database | 17 area filters, author search, year range |
| **BWRC** | Filterable list | Author links, year grouping |
| **Razavi Lab** | Year-grouped list (journals separate from conferences) | Separate pages: journal.html, conf.html, books.html |
| **al-folio** | BibTeX-powered, searchable | Author highlighting, venue badges, PDF/DOI links |
| **NanoCAD** | Single page, thesis reports separate | Chronological |

**Best practice for IC labs (Razavi pattern is standard):**
```
1. Journals & Transactions (grouped by year, most recent first)
2. Conference Papers (grouped by year)
3. Books & Book Chapters
4. Patents
Each entry: authors (bold lab members), title, venue, year, [DOI] [PDF]
```

### E. Contact / Join Page

| Lab | What They Include |
|-----|-------------------|
| **Stanford HAI** | "Get Involved" mega-menu, "Support HAI" (donations), mailing list |
| **BWRC** | "Join BWRC" for industry, "Become a Member" with questionnaire |
| **Razavi Lab** | "How to Apply" with detailed PhD admission requirements |
| **NanoCAD** | Simple contact info page |
| **Sailing Lab** | Not prominent (community page instead) |
| **CISL** | Building locations in footer |

**Best practice for IC labs:**
```
1. Location + map + building/room number
2. PI contact info
3. "Prospective Students" section with:
   - Open positions
   - Requirements
   - Application instructions
   - What to include in email
4. Industry collaboration info (if applicable)
```

---

## 12 Universal Design Patterns Across Top Lab Websites

### Structure & Navigation
1. **5-7 top-level nav items max** (Research | People | Publications | News | Contact is the standard)
2. **"Join Us" / "Openings" prominent** -- either in nav or homepage CTA
3. **Breadcrumb navigation** on deeper pages (HAI, BWRC, CSAIL)
4. **Search functionality** (all major sites)

### Visual Design
5. **University/institutional branding** in header + footer (Stanford red, Berkeley blue, Drexel gold)
6. **Card-based layouts** for projects and people (grid of hoverable cards)
7. **Generous whitespace** -- content max-width 800-1000px, padding 2-4rem
8. **Hero section** with lab identity: name + tagline + visual (not a wall of text)

### Content Strategy
9. **News/blog feed on homepage** -- shows lab is active and alive
10. **Research organized by theme, not by publication** -- visitors care about "what" before "which paper"
11. **Alumni section with current positions** -- proves lab trains people well (social proof)
12. **Sponsor/partner logos** for labs with industry relationships (BWRC, VLSI)

---

## Specific Recommendations for ICE Lab

Based on this analysis, the ICE Lab website should follow the **Modern Academic Group** archetype (al-folio based, like Sailing Lab) with elements borrowed from the **Classic IC Lab** (Razavi) and **Research Center** (BWRC) patterns.

### Priority improvements to make:

| Priority | What | Inspired By | Current State |
|----------|------|-------------|--------------|
| P0 | Hero section with lab photo + clear tagline | HAI, BWRC | Text-only about page |
| P0 | PI bio section on about page (not just lab description) | Razavi, all IC labs | Missing |
| P1 | Publications split: Journals / Conferences / Patents | Razavi model | Single empty bib |
| P1 | Alumni with current positions (social proof) | HAI, Sailing Lab | Placeholder with 1 alumni |
| P1 | Lab group photo on team page | BWRC, most labs | Missing |
| P2 | Sponsor/partner logos section | BWRC, Stanford VLSI | Missing |
| P2 | Seminar/reading group page | BWRC, CISL | Missing |
| P2 | Research facilities photos | BWRC | Text-only in research page |
| P3 | Chip gallery / selected designs showcase | Razavi (past work figures) | Missing |
| P3 | Teaching/courses page | NanoCAD, Razavi | Removed |

### Ideal nav for ICE Lab:
```
Home | Team | Research | Publications | Projects | Openings | Contact | News
```
(This matches our current structure -- we're already aligned with best practices!)
