# Debugging Challenge Suite

A curated set of small, realistic debugging tasks for humans or coding agents. Each challenge includes broken code, a reference fix, public tests, and a short explanation of the bug class.

## Why This Project Exists

Good evaluation work is not only about writing solutions. It is also about designing failures that reveal reasoning quality. This repo demonstrates:

- compact broken programs with realistic edge cases
- tests that catch behavioral regressions, not formatting trivia
- reference fixes for maintainers
- a runner script that can evaluate either the broken implementation or a candidate fix

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Run a specific challenge against the broken implementation:

```bash
CHALLENGE_IMPL=broken.py pytest challenges/01_rate_limiter
```

Run a specific challenge against the reference fix:

```bash
CHALLENGE_IMPL=fixed.py pytest challenges/01_rate_limiter
```

Use the helper script:

```bash
python scripts/run_challenge.py challenges/02_json_normalizer --impl fixed.py
```

## Challenges

| Challenge | Bug Theme | What The Tests Check |
| --- | --- | --- |
| `01_rate_limiter` | Boundary conditions and per-user state | independent users, exact window expiry, limit rejection |
| `02_json_normalizer` | Input mutation and data cleanup | immutability, tag normalization, invalid records |
| `03_path_sanitizer` | Path traversal | safe path joins, sibling-prefix attacks, absolute paths |

## Candidate Workflow

1. Open a challenge README.
2. Inspect `broken.py`.
3. Make a candidate implementation, usually by copying `broken.py` to `candidate.py`.
4. Run `CHALLENGE_IMPL=candidate.py pytest challenges/<challenge_name>`.
5. Compare behavior with `fixed.py` only after attempting the fix.

## What This Shows

This repo is built to signal careful test design, debugging judgment, security awareness, and the ability to create evaluation tasks that are small but meaningful.

