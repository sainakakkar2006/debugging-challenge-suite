from pathlib import Path


def safe_join(root: str | Path, requested_path: str | Path) -> Path:
    root_path = Path(root).absolute()
    candidate = (root_path / requested_path).absolute()
    if not str(candidate).startswith(str(root_path)):
        raise ValueError("path escapes root")
    return candidate

