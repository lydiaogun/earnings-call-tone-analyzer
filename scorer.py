from constants.tone import (
    POSITIVE, SLIGHTLY_POSITIVE, SLIGHTLY_NEGATIVE, NEGATIVE,
    NEGATIONS, MILD_HEDGING, STRONG_HEDGING,
)

# a negated match flips to its opposite category rather than just
# being dropped, e.g. "not strong" reads as negative, not neutral
CATEGORY_PHRASES = {
    "positive": POSITIVE,
    "slightly_positive": SLIGHTLY_POSITIVE,
    "slightly_negative": SLIGHTLY_NEGATIVE,
    "negative": NEGATIVE,
}

INVERSE_CATEGORY = {
    "positive": "negative",
    "negative": "positive",
    "slightly_positive": "slightly_negative",
    "slightly_negative": "slightly_positive",
}

HEDGING = STRONG_HEDGING + MILD_HEDGING

def scorer_with_negation(text, window=3):
    """Score each tone category, flipping a match to its opposite category
    when a negation word appears within `window` words before it (e.g.
    "not strong" counts as negative). If a hedging phrase appears in that
    same window instead, the match is dropped entirely rather than
    counted or flipped, since hedged language isn't a confident signal
    either way.

    Returns a dict of {category: normalised_score}.
    """
    words = text.lower().split()
    word_count = len(words)
    if word_count == 0:
        return {category: 0.0 for category in CATEGORY_PHRASES}

    counts = {category: 0 for category in CATEGORY_PHRASES}

    for category, phrase_list in CATEGORY_PHRASES.items():
        for phrase in phrase_list:
            phrase_words = phrase.lower().split()
            span = len(phrase_words)
            # slide through the text looking for the phrase
            for i in range(len(words) - span + 1):
                if words[i:i + span] != phrase_words:
                    continue

                # found the phrase at position i; check the words before it
                start = max(0, i - window)
                preceding = words[start:i]
                preceding_text = " ".join(preceding)

                if any(hedge in preceding_text for hedge in HEDGING):
                    continue  # hedged: too uncertain to count either way
                elif any(neg in preceding for neg in NEGATIONS):
                    counts[INVERSE_CATEGORY[category]] += 1  # negated: inverse
                else:
                    counts[category] += 1

    return {category: count / word_count for category, count in counts.items()}
