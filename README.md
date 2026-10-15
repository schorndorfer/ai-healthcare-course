# AI and Large Language Models in Healthcare

Open, **R-first** Quarto course book for the proposed Feinberg PPH Spring 2027 course. The [syllabus proposal](docs/AI_LLM_Healthcare_Syllabus_Proposal_Spring2027_R.pdf) guides the 10-week structure; it is not the final approved syllabus. Canvas will hold official course materials, submissions, permissions and updates.

## Local preview

Install [Quarto 1.10+](https://quarto.org/docs/get-started/). For optional Python companions, install [uv](https://docs.astral.sh/uv/); for the R example, install R 4.4+ separately.

```sh
quarto render                 # book → _site/
quarto render slides          # Reveal.js decks → _site/slides/
quarto preview                # live preview of the book
uv sync
uv run python examples/python/evaluate_extraction.py
uv run marimo run notebooks/01-attention.py
uv run marimo run notebooks/02-evaluation.py
Rscript examples/r/evaluate_extraction.R
```

Marimo runs locally; GitHub Pages hosts the static book, slides and downloadable notebook source, **not** a marimo server. None of the examples call hosted models or require paid API access. R labs in the syllabus use instructor-provided templates, data, packages and credentials via Canvas; the public repo does not replace them.

## GitHub Pages

Push to `main` and, in the GitHub repository settings, select **Settings → Pages → Build and deployment → Source: GitHub Actions**. The workflow at `.github/workflows/pages.yml` renders the book and decks and deploys `_site/`. The deployment URL will be shown in the Actions run / Pages settings. Relative links work on both project and user sites without hardcoding a repository name.

## Structure

- `weeks/`: weekly chapters and R lab directions
- `slides/`: three Reveal.js teaching decks, built separately after the book
- `notebooks/`: optional offline marimo companions
- `examples/r/`, `examples/python/`: parallel synthetic evaluation examples
- `project.qmd`: proposal, evaluation and submission checklists

**Safety:** only invented examples belong in the public repo. Never commit PHI, restricted or patient-derived data, credentials, API keys, or provider responses containing them. De-identification alone does not grant permission for external processing.
