def normalize_events(events: list[dict]) -> list[dict]:
    normalized: list[dict] = []

    for event in events:
        user_id = str(event.get("user_id", "")).strip().lower()
        if not user_id:
            continue

        score = int(event.get("score") or 0)
        tags = sorted(
            {
                str(tag).strip().lower()
                for tag in event.get("tags", [])
                if str(tag).strip()
            }
        )

        normalized.append(
            {
                "user_id": user_id,
                "score": max(score, 0),
                "tags": tags,
            }
        )

    return normalized

