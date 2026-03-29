
def easy_grader(processed):
    return 1.0 if any("spam" in e for e in processed) else 0.0

def medium_grader(processed):
    score = 0.0
    if any("spam" in e for e in processed):
        score += 0.5
    if any("urgent" in e for e in processed):
        score += 0.5
    return score

def hard_grader(processed):
    correct = ["spam", "urgent", "meeting"]
    score = sum(any(c in e for e in processed) for c in correct)
    return score / 3.0
