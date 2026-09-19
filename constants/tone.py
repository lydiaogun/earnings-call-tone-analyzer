# ---- SENTIMENT ----

POSITIVE = [
  "strong", "robust", "solid", "record", "outperformed", "accelerating",
  "resilient", "healthy", "exceptional", "favorable", "encouraging",
  "sustainable", "expanding", "improving", "confident", "optimistic",
  "momentum", "growth", "upside", "beat", "exceeded", "outstanding",
  "thriving", "buoyant", "advantageous",
  # added from training transcripts:
  "exceeding", "fastest", "leadership", "extraordinary", "revolutionary",
  "surging", "home run", "great", "fantastic", "excited", "proud", "seamless"
]

SLIGHTLY_POSITIVE = [
  "modest", "gradual", "stabilizing", "promising", "incremental",
  "reasonable", "cautiously optimistic", "steady", "constructive",
  "tentative", "measured", "supportive", "manageable", "workable",
  "adequate", "satisfactory", "recovering", "leveling", "firming",
  "tracking", "aligned", "hopeful"
]

SLIGHTLY_NEGATIVE = [
  "soft", "softening", "mixed", "uneven", "muted", "pressured",
  "challenging", "cautious", "uncertain", "moderating", "sluggish",
  "inconsistent", "constrained", "tempered", "subdued", "choppy",
  "volatile", "weakening", "lagging", "underwhelming", "strained",
  "tepid", "shaky", "wobbly", "fragile",
  # added from training transcripts:
  "constraints", "unable to", "limited"
]

NEGATIVE = [
  "weak", "declining", "deteriorating", "disappointing", "adverse",
  "unfavorable", "shortfall", "underperformed", "severe",
  "concerning", "troubling", "unsustainable", "eroding",
  "contracting", "distressed", "impaired", "unstable", "dire",
  "pronounced", "prolonged", "unpredictable", "bleak",
  # added from training transcripts (finance-specific negatives):
  "charge", "write-down", "write-off", "decline", "loss",
  "material adverse", "headwind"
]

# ---- HEDGING ----

STRONG_HEDGING = [
  "hard to say", "difficult to say", "hard to predict", "difficult to predict",
  "hard to know", "too early to say", "too early to tell", "remains to be seen",
  "we'll see", "time will tell", "puts and takes", "it depends", "depends on",
  "dependent on", "no guarantee", "can't be certain", "not sure", "we don't know",
  "up in the air", "wait and see", "case by case", "one way or the other",
  # added from training transcripts:
  "we're not exactly sure", "we're considering", "limited options", "nothing to announce"
]

MILD_HEDGING = [
  "we believe", "we think", "we feel", "in our view", "our sense is",
  "we're comfortable", "cautiously", "somewhat", "relatively", "fairly",
  "roughly", "approximately", "generally", "largely", "mostly",
  "kind of", "sort of", "more or less", "to some extent", "potentially",
  "possibly", "hopefully", "we hope", "we expect", "we anticipate",
  "likely", "probably", "perhaps", "at this point", "at this time",
  "for now", "in the near term", "subject to", "assuming", "preliminary",
  "tentative", "plus or minus", "give or take", "our best estimate", "if things",
  # added from training transcripts:
  "i think", "i believe", "in a lot of ways", "somewhere in the range of", "at the moment"
]

NEGATIONS = ["not", "no", "never", "without", "n't", "hardly", "cannot",
             "isn't", "wasn't", "aren't", "don't", "doesn't", "didn't",
             "won't", "couldn't", "wouldn't", "shouldn't", "none", "nor"]