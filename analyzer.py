def extract_keywords(trends):
    keywords = []

    for trend in trends:
        words = trend.lower().split()
        for word in words:
            if word not in ["the", "and", "in", "for", "my", "i"]:
                keywords.append(word)

    return list(set(keywords))