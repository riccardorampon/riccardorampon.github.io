# CV site — design

## Intent

A personal site at `riccardorampon.github.io` that presents Riccardo's CV and, over time, his
personal projects. Audience: recruiters and anyone who wants to approach him. In under a minute a
visitor should know who he is (AI/ML Engineer: production GenAI, MLOps on AWS, backend), see what
he has built, and know how to reach him.

## Goals

- Show the CV content from `docs/Developer_Resume.pdf`: profile, experience, education, skills,
  languages, hobbies.
- Projects section of short cards (name, one-line description, tech tags, link to the GitHub repo).
  While there are no projects, show a single "coming soon" card.
- Contact always reachable: GitHub, LinkedIn, email, downloadable CV.
- Works on phones.

## Non-goals

- Project write-up pages, blog, multiple languages, contact form, analytics, CMS.

## Anti-goals

- Publishing phone number or date of birth (scraping risk). They appear nowhere on the site or in
  the repo.
- A build pipeline or dependencies for what is one static page.

## Constraints

- GitHub Pages user site, served from `main`, repo root. Public repo: anything committed is public.
- `docs/Developer_Resume.pdf` (contains phone and date of birth) is never committed; it goes in
  `.gitignore`.

## Approaches

1. **Plain HTML + CSS, no build** — chosen. Edit `index.html` directly; preview by opening the file.
   Content and markup live together.
2. **Jekyll with `_data/*.yml`** — projects as data, rendered by GitHub Pages. Rejected for now: Liquid
   and a Ruby toolchain for local preview aren't worth it for one rarely-changing page. Easy move later
   if projects grow numerous.
3. **JS framework (Astro/Vite) + Actions deploy** — dropped: build pipeline for a single static page.

## Decided

- **Layout B, fixed sidebar** (chosen from mockups). Left sidebar: name, "AI/ML Engineer", Padua IT,
  section nav (About, Experience, Projects, Skills, Education), links GitHub · LinkedIn · Email
  (`mailto:`) · CV ↓. Right column scrolls.
- **Section order:** About → Experience → Projects → Skills → Education → Languages & hobbies.
- **CV download:** Riccardo provides a redacted PDF (no phone, no date of birth), committed as `cv.pdf`
  at the repo root, linked from the sidebar.
- **Stack:** `index.html`, `style.css`, `cv.pdf` at repo root. No JavaScript, no dependencies.
- **Language:** English only.

## Builder's calls (Claude's proposals, correctable)

- Look follows mockup B: dark sidebar, light content area, one blue accent; system font stack, no web
  fonts.
- Experience bullets shown in full (already short). Skills as tag chips per group.
- Under ~800px the sidebar becomes a top header and sections stack.
- Accessibility basics: semantic landmarks (`nav`, `main`, `section`), visible focus, sufficient
  contrast, external links labelled.
- `<title>` and `<meta name="description">`; no Open Graph/favicon until wanted.
- Each project card is a self-contained block with an HTML comment template above the grid so adding
  one is copy-and-edit.
- `CLAUDE.md` updated with the stack and "open `index.html` to preview".
