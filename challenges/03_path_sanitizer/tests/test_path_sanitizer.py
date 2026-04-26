import importlib.util
import os
from pathlib import Path

import pytest


def load_candidate():
    path = Path(__file__).parents[1] / os.environ.get("CHALLENGE_IMPL", "fixed.py")
    spec = importlib.util.spec_from_file_location("candidate_path_sanitizer", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_allows_file_inside_root(tmp_path):
    root = tmp_path / "uploads"
    root.mkdir()

    result = load_candidate().safe_join(root, "images/avatar.png")

    assert result == (root / "images/avatar.png").resolve()


def test_rejects_parent_directory_escape(tmp_path):
    root = tmp_path / "uploads"
    root.mkdir()

    with pytest.raises(ValueError):
        load_candidate().safe_join(root, "../secret.txt")


def test_rejects_sibling_prefix_attack(tmp_path):
    root = tmp_path / "uploads"
    sibling = tmp_path / "uploads_evil"
    root.mkdir()
    sibling.mkdir()

    with pytest.raises(ValueError):
        load_candidate().safe_join(root, "../uploads_evil/payload.txt")


def test_rejects_absolute_path_outside_root(tmp_path):
    root = tmp_path / "uploads"
    root.mkdir()

    with pytest.raises(ValueError):
        load_candidate().safe_join(root, tmp_path / "outside.txt")

