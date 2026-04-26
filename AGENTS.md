# AGENTS.md

This file gives coding agents the working context for the Australian Math Coach website.

## Project Snapshot
- Stack: Astro 5, Tailwind CSS v4 (via `@tailwindcss/vite`), optional React deps present.
- Package manager: npm.
- Site type: static output (`astro build`).
- Brand direction: clean, minimal, blue/white (#204585 brand blue), education-focused.
- Primary conversion action: Book a free session.
- Primary contact: `hamish@australianmathcoach.com`.
- Availability: Mon–Fri 9:00 AM – 6:00 PM, Sat–Sun 8:00 AM – 8:00 PM.
- Proprietor: Hamish MacDonald (senior data platform and engineering consultant).

## Core Messaging: Two Learning Pathways
The site now clearly communicates two distinct pathways:

1. **Build strong maths foundations** (For students improving school maths and confidence)
   - Core concepts explained clearly
   - Problem-solving techniques
   - Exam and test preparation
   - Small group or 1:1 sessions
   - Outcome: better understanding, improved confidence, stronger school results

2. **Advanced problem-solving & competitions** (For students aiming deeper and toward AMC/AIMO/AMO)
   - Structured problem-solving training
   - AMC-style questions and strategies
   - Mathematical reasoning and pattern recognition
   - Small group learning environment
   - Outcome: strong problem-solving ability, competition readiness, advanced thinking

## Current Site Structure
- Shared layout: `src/layouts/Layout.astro` (with page-specific `showCornerLogo` prop, defaults true)
- Shared components:
  - `src/components/SiteHeader.astro` (sticky, path-aware Home button for sub-pages)
  - `src/components/HeroSection.astro`
  - `src/components/CTASection.astro` (reusable final CTA block)
  - `src/components/SiteFooter.astro`
- Main pages (all active):
  - `src/pages/index.astro` (landing page, no corner logo)
  - `src/pages/about.astro` (mission-driven, introduces Hamish MacDonald)
  - `src/pages/coaching.astro` (pathway placeholder)
  - `src/pages/extension-amc.astro` (competition pathway, no corner logo, refactored 2026-04)
  - `src/pages/sessions.astro` (session info placeholder)
  - `src/pages/services.astro` (Programs page, redesigned two-pathway layout, no corner logo)
  - `src/pages/contact.astro` (contact form and info, refactored 2026-04, no corner logo)

## Brand Assets
Located in `public/images/brand/`:
- `AustralianMathCoach-logo.png` (displayed top-right on internal pages via Layout corner logo)
- `AustralianMathCoach-banner.png` (for future hero sections if needed)

## Design System (Current)
All pages now use a consistent blue/white system:

**Colors:**
- Brand blue: `#204585` (primary CTA buttons, links, accents)
- Hover blue: `#1a3a70` (darker blue for button hover states)
- White backgrounds: primary content areas
- Slate-50: secondary/alternating section backgrounds (subtle contrast)
- Slate text: typography hierarchy (slate-900 headings, slate-700 body, slate-600 secondary)

**Spacing & Layout:**
- Section padding: `py-16 md:py-20` (consistent vertical rhythm)
- Container max-widths: `max-w-5xl` or `max-w-6xl` for content, `max-w-3xl` for readable text width
- Grid gaps: `gap-8` for main layouts, `gap-5` for cards/form fields
- Component padding: `p-6 md:p-8` for cards and containers

**Typography:**
- Headings: bold, tracking-tight (`text-4xl md:text-5xl` for h1, `text-3xl md:text-4xl` for h2)
- Body: `text-lg` with `leading-relaxed` for readability
- Links: `text-[#204585] hover:text-[#1a3a70]`

**Components:**
- Cards: white background, `border border-slate-200`, `rounded-2xl`, `shadow-sm`
- Buttons: solid brand blue, `rounded-lg`, `px-6 py-3` or larger
- Forms: `border border-slate-300 rounded-xl`, `focus:ring-2 focus:ring-blue-600`

**Removed (Legacy):**
- All purple/pink gradient styling
- Multicolor category cards
- Heavy shadow treatments and animations

## Styling Pipeline Notes
- Tailwind v4 is compiled through Vite plugin in `astro.config.mjs`.
- Global CSS entrypoint: `src/styles/global.css`.
- Canonical Tailwind import (v4): `@import "tailwindcss";`
- Static build output: `dist/` folder generated via `npm run build`.
- If styling appears default: verify CSS bundle in generated HTML, hard refresh browser, check class names in markup.

## Shared Components & Patterns
- **Layout wrapper** with `showCornerLogo={false}` prop (disabled on `/services`, `/extension-amc`, `/contact`)
- **SiteHeader** with:
  - Sticky positioning (`sticky top-0 z-50`)
  - Path-aware Home button (appears on sub-pages only)
  - Responsive nav (hidden on mobile, visible on desktop)
  - Desktop and mobile CTA buttons
- **CTASection** (reused on all pages):
  - White container, centered content, standard spacing
  - Consistent messaging: "Start with a free first session"
  - Brand-blue button to `hamish@australianmathcoach.com` mailto
- **Form pattern** (Contact page):
  - FormSubmit.co service for email handling
  - Responsive grid layout, consistent field styling
  - Dropdowns updated to pathway + subject context

## Deployment & CI/CD
- **Hosting:** GitHub Pages (static deployment)
- **Workflow:** `.github/workflows/deploy.yml`
  - Triggers on push to `main` branch or manual `workflow_dispatch`
  - Node 20, npm ci install, `npm run build`, uploads `dist/` artifacts
  - Auto-deploys via GitHub Pages (live within 1-2 minutes)
- **Repository:** `github.com/elusivenode/amc`
- Check deployment status: GitHub Actions tab in repository

## Commands
- Install: `npm install`
- Dev server: `npm run dev`
- Build: `npm run build` (generates `dist/` for deployment)
- Preview: `npm run preview` (local preview of built site)
- Deploy: `git push origin main` (triggers GitHub Actions)

## Page-Specific Details

**Landing (`/`)**
- Two-column pathway showcase
- Corner logo: **disabled** (`showCornerLogo={false}`)
- Final CTA section
- Hero-first layout

**About (`/about`)**
- Mission-driven intro
- "Why mathematical thinking matters" section (AI-age context)
- Hamish MacDonald introduction (first person, senior consultant, father of two)
- Teaching philosophy: 4 principles
- Shared CTA at bottom
- Corner logo: **enabled** (defaults true)

**Programs (`/services`)**
- Heading: "Programs"
- Two-column pathway cards (mobile-stacked)
  - Left: "Build strong maths foundations"
  - Right: "Advanced problem-solving & competitions"
- Each card has: Who it's for / What's included / Outcome sections
- Left card CTA: "Book a free session" (mailto)
- Right card CTA: "Explore extension maths" (links to `/extension-amc`)
- Shared CTA section at bottom
- Corner logo: **disabled**

**Extension & AMC (`/extension-amc`)**
- Heading: "Extension & Competition Maths"
- Sections:
  1. Hero intro
  2. "Why competition maths?" (engagement, deep thinking vs memorization)
  3. "A pathway for advanced students" (AMC → AIMO → AMO progression, invitation-based note)
  4. "Learn through guided group problem-solving"
  5. "Skills developed" (pattern recognition, reasoning, problem-solving, confidence)
- Shared CTA at bottom
- Corner logo: **disabled**

**Contact (`/contact`)**
- Heading: "Get in touch"
- Two-column layout:
  - Left: Contact info card (phone, email, location, hours)
  - Right: Contact form card
- Phone: 0418 764 798
- Hours: Mon–Fri 9:00 AM – 6:00 PM, Sat–Sun 8:00 AM – 8:00 PM
- Location: 6 Turner Street, Corinda, Brisbane Q4075
- Form fields: name, email, phone, student pathway (dropdown), subject (dropdown), message
- FAQ section (4 common questions)
- Shared CTA at bottom
- Corner logo: **disabled**

**Coaching & Sessions**
- Placeholder pages with pathway intro and CTA
- Minimal content (for future expansion)
- Corner logo: **enabled** (defaults true)

## UX/Content Guardrails
- Keep copy concise and parent-readable.
- Avoid overengineering and unnecessary abstractions.
- Prefer reusable sections/components only when clearly useful.
- Do not introduce purple/pink visual identity (legacy removed in April 2026).
- Use blue/white visual system aligned to logo/banner.
- All CTAs should default to `hamish@australianmathcoach.com` or `/extension-amc` as appropriate.
- Header always shows "Book a free session" button on desktop; mobile shows "Book now" (compact).
- Sub-page headers show "Home" button (path-aware) to aid navigation.

## Conversion Guardrails
- Keep a clear booking CTA visible in header and key sections.
- Booking target defaults to `mailto:hamish@australianmathcoach.com`.
- If a booking URL or calendar widget is introduced later, update all CTA targets consistently.
- Landing page and each detail page should have a final CTA section (via CTASection component).
- Forms use FormSubmit.co; verify hidden fields (subject) and email recipient on any changes.

## Safe Refactor Approach
1. Make small, reviewable changes.
2. Avoid changing unrelated pages/components.
3. Run `npm run build` locally to test.
4. Commit focused, descriptive messages.
5. Push to `main` to trigger GitHub Actions deployment.
6. Report exact files changed and assumptions.

## Recent Work (April 2026)
- ✅ Removed all purple/pink gradients and multicolor styling.
- ✅ Implemented blue/white design system across all pages.
- ✅ Refactored Programs page into two-pathway layout.
- ✅ Enhanced Extension & AMC page with structured sections and competition pathway clarity.
- ✅ Redesigned Contact page with brand alignment, form updates, FAQ consolidation.
- ✅ Updated About page to introduce Hamish MacDonald by name (first person).
- ✅ Added shared CTASection component for consistency.
- ✅ Added path-aware Home button in header on sub-pages.
- ✅ Enlarged corner logo (w-72 md:w-96) on internal pages.
- ✅ Updated phone availability to Sat–Sun 8:00 AM – 8:00 PM.
- ✅ All pages tested with `npm run build`; deployed via GitHub Actions.

## Known Cleanup Candidates (Non-blocking)
- Legacy components in `src/components/` (Features.astro, Hero.astro, MathShowcase.astro) can be removed if confirmed unused.
- `tailwind.config.json` exists but Tailwind v4 setup is plugin/CSS-driven; remove if not used.
- Root `404.html` and `robots.txt` are legacy-era top-level files and should be reviewed for either migration into `public/` or removal.
- Global CSS legacy classes can be cleaned up if no longer referenced.
