# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

GitHub Pages user site (`riccardorampon.github.io`), a personal CV site.

- Stack: plain `index.html` + `style.css` + `cv.pdf` at the repo root. No build step, no dependencies, no JavaScript.
- Preview: open `index.html` in a browser.
- Publishing: GitHub Pages serves the root of `main` as-is. Work happens on `develop`.
- Adding a project: copy the commented card template in the Projects section of `index.html` into `div.cards` (remove the "Coming soon" card once a real one exists).
- Privacy: never commit the phone number or date of birth. `docs/Developer_Resume.pdf` stays git-ignored; `cv.pdf` must be the redacted version: run `python3 scripts/check_cv.py cv.pdf` before committing a new one (must print `OK`; it also scans compressed link annotations, which a plain `grep` misses).
- Design spec and plans live in `docs/superpowers/specs/` and `docs/superpowers/plans/`.
