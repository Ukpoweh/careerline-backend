from typing import Dict

# Example pathways from your database
PATHWAYS = ["Data Analysis", "Cybersecurity", "Software Development", "Product Management", "Digital Marketing"]

def deterministic_scores(inputs: Dict) -> Dict[str, int]:
    """Apply rule-based scoring logic."""
    scores = {p: 0 for p in PATHWAYS}

    # Personality rules
    if inputs.get("personality") == "introvert":
        scores["Data Analysis"] += 15
        scores["Cybersecurity"] += 15
        scores["Software Development"] += 10
    elif inputs.get("personality") == "extrovert":
        scores["Digital Marketing"] += 15
        scores["Product Management"] += 15

    # Motive rules
    motive = inputs.get("motive")
    if motive == "migration":
        scores["Data Analysis"] += 15
        scores["Cybersecurity"] += 15
        scores["Software Development"] += 10
    elif motive == "side hustle":
        scores["Digital Marketing"] += 15
        scores["Software Development"] += 10
    elif motive == "money-making":
        scores["Digital Marketing"] += 15
    elif motive == "new career":
        scores["Software Development"] += 15
        scores["Data Analysis"] += 10

    # Age rules
    age = inputs.get("age")
    if age:
        if 18 <= age <= 25:
            scores["Software Development"] += 10
            scores["Data Analysis"] += 10
        elif 26 <= age <= 40:
            scores["Product Management"] += 10
            scores["Data Analysis"] += 15
        elif age > 40:
            scores["Product Management"] += 15
            scores["Digital Marketing"] += 10

    # Present job rules
    job = inputs.get("present_job")
    if job and "civil" in job.lower():
        scores["Data Analysis"] += 15
        scores["Cybersecurity"] += 15
    elif job and "teacher" in job.lower():
        scores["Digital Marketing"] += 15
        scores["Product Management"] += 10
    elif job and "accountant" in job.lower():
        scores["Data Analysis"] += 15
        scores["Product Management"] += 10

    # Industry rules
    industry = inputs.get("industry")
    if industry:
        if "health" in industry.lower():
            scores["Data Analysis"] += 10
            scores["Cybersecurity"] += 10
        elif "finance" in industry.lower():
            scores["Data Analysis"] += 15
            scores["Product Management"] += 10
        elif "media" in industry.lower():
            scores["Digital Marketing"] += 15

    return scores


def normalize_scores(scores: Dict[str, int]) -> Dict[str, int]:
    """Normalize to a 0–100 percentage scale."""
    vals = list(scores.values())
    if not vals or max(vals) == min(vals):
        return {k: 100 for k in scores}
    minv, maxv = min(vals), max(vals)
    return {k: int(100 * (v - minv) / (maxv - minv)) for k, v in scores.items()}
