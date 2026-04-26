def normalize_events(events: list[dict]) -> list[dict]:
    normalized = []
    for event in events:
        event["user_id"] = event.get("user_id", "").lower()
        event["score"] = int(event.get("score", 0))
        event["tags"] = list(set(event.get("tags", [])))
        normalized.append(event)
    return normalized

