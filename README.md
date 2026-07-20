# Debugging Challenge Suite

**Name:** Saina Kakkar

## Design and Implementation

This repo is a small set of debugging problems. I made it because debugging
is a big part of software engineering, and it is also useful for code
evaluation. A good challenge should test behavior, not just whether code
looks nice.

## Files

Each challenge folder has:

- `broken.py`, which has a real bug
- `fixed.py`, which shows one correct solution
- tests that catch the bug
- a short README explaining what the code is supposed to do

## Challenges

| Challenge | Bug Theme | What The Tests Check |
| --- | --- | --- |
| `01_rate_limiter` | Boundary conditions and per-user state | independent users, exact window expiry, limit rejection |
| `02_json_normalizer` | Input mutation and data cleanup | immutability, tag normalization, invalid records |
| `03_path_sanitizer` | Path traversal | safe path joins, sibling-prefix attacks, absolute paths |

## Run

Setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Run a specific challenge against the broken implementation:

```bash
CHALLENGE_IMPL=broken.py pytest challenges/01_rate_limiter
```

Run the same challenge against the reference fix:

```bash
CHALLENGE_IMPL=fixed.py pytest challenges/01_rate_limiter
```

Or use the helper script:

```bash
python scripts/run_challenge.py challenges/02_json_normalizer --impl fixed.py
```

## Verify

```bash
pytest
```

If the tests fail on `broken.py` and pass on `fixed.py`, each challenge is
doing its job.

## Trying a Challenge Yourself

1. Open a challenge README.
2. Inspect `broken.py`.
3. Make a candidate implementation, usually by copying `broken.py` to `candidate.py`.
4. Run `CHALLENGE_IMPL=candidate.py pytest challenges/<challenge_name>`.
5. Compare behavior with `fixed.py` only after attempting the fix.

## Notes

The `CHALLENGE_IMPL` environment variable is what makes the suite work. The
same tests run against the broken code, the reference fix, or your own
attempt, so the tests define correctness and the implementation is
swappable.

My favorite of the three is the path sanitizer. A naive check like
`path.startswith(base_dir)` looks safe, but `/safe/../etc/passwd` and the
sibling-prefix case `/safe-evil` (which starts with `/safe`) both slip
through it. The tests include those exact attacks. Building these
challenges taught me as much about writing edge-case tests as it did about
the bugs themselves.
