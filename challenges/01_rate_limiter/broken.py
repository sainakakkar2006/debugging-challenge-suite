class RateLimiter:
    def __init__(self, limit: int, window_seconds: int):
        self.limit = limit
        self.window_seconds = window_seconds
        self.events: list[float] = []

    def allow(self, user_id: str, now: float) -> bool:
        self.events = [event for event in self.events if now - event <= self.window_seconds]
        if len(self.events) > self.limit:
            return False
        self.events.append(now)
        return True

