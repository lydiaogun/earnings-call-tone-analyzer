def scorer(text, phrase_list):
    """Count how often phrases from phrase_list appear in text,
    normalised by passage length so long passages aren't unfairly high."""

    text_lower = text.lower()
    word_count = len(text_lower.split())

    if word_count == 0:
        return 0.0

    count = 0
    for phrase in phrase_list:
        count += text_lower.count(phrase.lower())

    return count / word_count

