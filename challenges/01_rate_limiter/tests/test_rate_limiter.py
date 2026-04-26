import importlib.util
import os
from pathlib import Path

import pytest


def load_candidate():
    path = Path(__file__).parents[1] / os.environ.get("CHALLENGE_IMPL", "fixed.py")
    spec = importlib.util.spec_from_file_location("candidate_rate_limiter", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_allows_up_to_limit_per_user():
    limiter = load_candidate().RateLimiter(limit=2, window_seconds=10)

    assert limiter.allow("alice", 0.0) is True
    assert limiter.allow("alice", 1.0) is True
    assert limiter.allow("alice", 2.0) is False


def test_users_have_independent_quotas():
    limiter = load_candidate().RateLimiter(limit=1, window_seconds=10)

    assert limiter.allow("alice", 0.0) is True
    assert limiter.allow("bob", 1.0) is True
    assert limiter.allow("alice", 2.0) is False


def test_exact_window_boundary_expires_old_events():
    limiter = load_candidate().RateLimiter(limit=1, window_seconds=10)

    assert limiter.allow("alice", 0.0) is True
    assert limiter.allow("alice", 10.0) is True


def test_rejects_invalid_limits():
    with pytest.raises(ValueError):
        load_candidate().RateLimiter(limit=0, window_seconds=10)

