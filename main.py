from parser import parse_all_transcripts
from scorer import scorer_with_negation
from market import get_earnings_reaction

TICKER = "NVDA"
CATEGORIES = ("positive", "slightly_positive", "slightly_negative", "negative")


def score_section(sentences):
    """Join a section's sentences back into one passage and score it."""
    text = " ".join(sentences)
    return scorer_with_negation(text)


def net_tone(scores):
    """Collapse the four categories into one signed score, weighting the
    strong categories more heavily than the slight ones."""
    return (
        scores["positive"] * 2
        + scores["slightly_positive"]
        - scores["slightly_negative"]
        - scores["negative"] * 2
    )


def print_report(transcript):
    print(f"\n{transcript['company'].upper()} - {transcript['date']}")
    print("-" * 40)

    prepared_tone = None
    for label, sentences in (("Prepared remarks", transcript["prepared"]), ("Q&A", transcript["qa"])):
        scores = score_section(sentences)
        tone = net_tone(scores)
        if label == "Prepared remarks":
            prepared_tone = tone

        print(f"  {label}:")
        for category in CATEGORIES:
            print(f"    {category:<18} {scores[category]:.4f}")
        print(f"    {'net tone':<18} {tone:+.4f}")

    print("  Market reaction:")
    reaction = get_earnings_reaction(TICKER, transcript["date"])
    if reaction is None:
        print("    could not fetch stock data for this date")
        return

    print(f"    {reaction['call_day']} close -> {reaction['target_day']} close")
    print(f"    {'price move':<18} {reaction['return']:+.2%}")

    agrees = (prepared_tone >= 0) == (reaction["return"] >= 0)
    print(f"    prepared-remarks tone {'agrees' if agrees else 'disagrees'} with the market's next-day move "
          f"(tone {prepared_tone:+.4f} vs return {reaction['return']:+.2%})")


def main():
    transcripts = parse_all_transcripts("resources")
    if not transcripts:
        print("No transcripts found in resources/")
        return

    for transcript in transcripts:
        print_report(transcript)


if __name__ == "__main__":
    main()
