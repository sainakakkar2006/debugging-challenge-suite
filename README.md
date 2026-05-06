# Debugging Challenge Suite

This repo is a small set of debugging problems.

Each challenge has:

- `broken.py`, which has a real bug
- `fixed.py`, which shows one correct solution
- tests that catch the bug
- a short README explaining what the code is supposed to do

I made this because debugging is a big part of software engineering. It is also useful for code evaluation because a good challenge should test behavior, not just whether code looks nice.

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

## What I Practiced

- writing tests for edge cases
- finding bugs by reading behavior carefully
- making small coding challenges
- thinking about security bugs like path traversal
- building a simple runner script
- organizing code so another person can try the challenges
