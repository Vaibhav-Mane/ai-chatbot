def estimate_token(messages):
    total = 0
    for m in messages:
        words = len(m["content"].split())
        total += words
        return total