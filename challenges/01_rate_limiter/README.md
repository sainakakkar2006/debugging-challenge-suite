# Challenge 01: Rate Limiter

## Task

Fix `RateLimiter.allow(user_id, now)` so it permits at most `limit` events per user inside a rolling time window.

## Bug Class

The broken implementation mixes all users into one shared event list and mishandles the exact expiry boundary.

## Expected Behavior

- Different users should not consume each other's quota.
- Events exactly `window_seconds` old should expire.
- A rejected event should not be stored.

## Run

```bash
CHALLENGE_IMPL=broken.py pytest challenges/01_rate_limiter
CHALLENGE_IMPL=fixed.py pytest challenges/01_rate_limiter
```

