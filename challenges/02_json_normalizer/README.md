# Challenge 02: JSON Normalizer

## Task

Fix `normalize_events(events)` so it returns clean event records without mutating the input list.

## Bug Class

The broken implementation mutates caller-owned dictionaries, preserves invalid records, and leaves inconsistent tag casing.

## Expected Behavior

- Skip records without a usable `user_id`.
- Convert `score` to an integer and clamp negative values to zero.
- Lowercase, strip, deduplicate, and sort tags.
- Do not mutate the original input.

