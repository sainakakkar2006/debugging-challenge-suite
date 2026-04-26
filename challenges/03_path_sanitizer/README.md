# Challenge 03: Path Sanitizer

## Task

Fix `safe_join(root, requested_path)` so it returns a path inside `root` and rejects traversal attempts.

## Bug Class

The broken implementation relies on string prefix checks, which can be bypassed by sibling directories with similar names.

## Expected Behavior

- Resolve relative path segments.
- Reject paths outside the root directory.
- Reject absolute paths outside the root directory.
- Return a resolved `Path`.

