import glob
import re
import os

def parse_all_transcripts(folder="resources"):
    """Parse every .txt transcript in the folder.

    Returns a list of transcript dicts, one per file.
    """
    filepaths = sorted(glob.glob(os.path.join(folder, "*_*.txt")))
    # sorted so files always come back in the same order
    # (only "<company>_<date>.txt" files are transcripts; other .txt files
    # in this folder, e.g. word lists, are skipped)
    results = []
    for filepath in filepaths:
        results.append(parse_transcript(filepath))
    return results


def parse_transcript(filepath):
    """Read a stripped transcript and split it into prepared remarks and Q&A.

    Returns a dict:
    {
        "company": "nvidia",
        "date": "2025-08-27",
        "prepared": [list of sentences],
        "qa":       [list of sentences],
    }
    """
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # --- pull company + date out of the filename (e.g. nvidia_2025-08-27.txt) ---
    filename = os.path.basename(filepath)          # "nvidia_2025-08-27.txt"
    name_part = filename.replace(".txt", "")        # "nvidia_2025-08-27"
    company, date = name_part.split("_")            # "nvidia", "2025-08-27"

    # --- split on the Q&A marker ---
    marker = "QUESTION AND ANSWER SECTION"
    if marker in text:
        prepared_text, qa_text = text.split(marker, 1)
        # prepared text means the script the speaker wrote for themselves
        # qa text means what the speaker actually said 
    else:
        # no marker found: treat the whole thing as prepared, warn, leave Q&A empty
        print(f"WARNING: no Q&A marker found in {filename}")
        prepared_text, qa_text = text, ""

    return {
        "company": company,
        "date": date,
        "prepared": split_into_sentences(prepared_text),
        "qa": split_into_sentences(qa_text),
    }


def split_into_sentences(text):
    """Break a chunk of text into a list of sentences."""
    # collapse all whitespace (newlines, double spaces) into single spaces
    text = " ".join(text.split())

    # split after . ! or ? when followed by a space
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # drop empty strings and tiny fragments
    sentences = [s.strip() for s in sentences if len(s.strip()) > 3]
    return sentences


# --- quick test ---
if __name__ == "__main__":
    transcripts = parse_all_transcripts("resources")
    print(f"Parsed {len(transcripts)} transcripts\n")
    for t in transcripts:
        print(f"{t['company']} {t['date']}: "
              f"{len(t['prepared'])} prepared, {len(t['qa'])} Q&A sentences")