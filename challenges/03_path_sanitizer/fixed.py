from pathlib import Path


def safe_join(root: str | Path, requested_path: str | Path) -> Path:
    root_path = Path(root).resolve()
    candidate = (root_path / requested_path).resolve()

    try:
        candidate.relative_to(root_path)
    except ValueError as exc:
        raise ValueError("path escapes root") from exc

    return candidate

