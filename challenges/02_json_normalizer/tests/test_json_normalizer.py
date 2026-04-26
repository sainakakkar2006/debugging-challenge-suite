import copy
import importlib.util
import os
from pathlib import Path


def load_candidate():
    path = Path(__file__).parents[1] / os.environ.get("CHALLENGE_IMPL", "fixed.py")
    spec = importlib.util.spec_from_file_location("candidate_json_normalizer", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_normalizes_and_filters_records():
    events = [
        {"user_id": " Alice ", "score": "7", "tags": ["Prod", " prod ", "API"]},
        {"user_id": "", "score": "99", "tags": ["drop"]},
        {"user_id": "BOB", "score": "-3", "tags": [None, " Ops "]},
    ]

    assert load_candidate().normalize_events(events) == [
        {"user_id": "alice", "score": 7, "tags": ["api", "prod"]},
        {"user_id": "bob", "score": 0, "tags": ["none", "ops"]},
    ]


def test_does_not_mutate_input():
    events = [{"user_id": "Alice", "score": "1", "tags": ["One"]}]
    original = copy.deepcopy(events)

    load_candidate().normalize_events(events)

    assert events == original

