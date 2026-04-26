# AGENTS.md

This file gives coding agents the working context for the Australian Math Coach website.

## Project Snapshot
- Stack: Astro 5, Tailwind CSS v4 (via `@tailwindcss/vite`), optional React deps present.
- Package manager: npm.
- Site type: static output (`astro build`).
- Brand direction: clean, minimal, blue/white, education-focused.
- Primary conversion action: Book a free session.
- Primary contact: `hamish@australianmathcoach.com`.

## Current Site Structure
- Shared layout: `src/layouts/Layout.astro`
- Shared components:
  - `src/components/SiteHeader.astro`
  - `src/components/HeroSection.astro`
  - `src/components/CTASection.astro`
  - `src/components/SiteFooter.astro`
- Main pages:
  - `src/pages/index.astro` (landing page)
  - `src/pages/coaching.astro`
  - `src/pages/extension-amc.astro`
  - `src/pages/sessions.astro`
  - legacy pages still present: `about.astro`, `contact.astro`, `services.astro`

## Brand Assets
Expected location:
- `public/images/brand/AustralianMathCoach-logo.png`
- `public/images/brand/AustralianMathCoach-banner.png`

When changing hero/header visuals, preserve compatibility with those filenames unless intentionally migrating.

## Styling Pipeline Notes
- Tailwind is active and compiled through Vite plugin in `astro.config.mjs`.
- Global CSS entrypoint: `src/styles/global.css`.
- Tailwind import uses v4 style:
  - `@import "tailwindcss";`
- If styling appears default in browser, first verify:
  1. CSS bundle is linked in generated HTML.
  2. Hard refresh/no-cache in browser.
  3. Class names are present in rendered markup.

## Commands
- Install: `npm install`
- Dev server: `npm run dev`
- Build: `npm run build`
- Preview build: `npm run preview`

## UX/Content Guardrails
- Keep copy concise and parent-readable.
- Avoid overengineering and unnecessary abstractions.
- Prefer reusable sections/components only when clearly useful.
- Do not introduce purple/pink visual identity unless explicitly requested.
- Use blue/white visual system aligned to logo/banner.

## Conversion Guardrails
- Keep a clear booking CTA visible in header and key sections.
- For now, booking target defaults to `mailto:hamish@australianmathcoach.com`.
- If a booking URL is introduced later, update all CTA targets consistently.

## Safe Refactor Approach
1. Make small, reviewable changes.
2. Avoid changing unrelated pages/components.
3. Run `npm run build` after edits.
4. Report exact files changed and any assumptions.

## Known Cleanup Candidates (Non-blocking)
- Legacy unused components may remain in `src/components/` from prior iterations.
- `tailwind.config.json` exists but Tailwind v4 setup is plugin/CSS-driven; keep only if intentionally used.
- Legacy pages and old content can be phased out after nav/content migration is complete.
