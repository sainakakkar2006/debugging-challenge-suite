from collections import defaultdict, deque


class RateLimiter:
    def __init__(self, limit: int, window_seconds: int):
        if limit <= 0:
            raise ValueError("limit must be positive")
        if window_seconds <= 0:
            raise ValueError("window_seconds must be positive")
        self.limit = limit
        self.window_seconds = window_seconds
        self.events_by_user: dict[str, deque[float]] = defaultdict(deque)

    def allow(self, user_id: str, now: float) -> bool:
        events = self.events_by_user[user_id]
        while events and now - events[0] >= self.window_seconds:
            events.popleft()

        if len(events) >= self.limit:
            return False

        events.append(now)
        return True

