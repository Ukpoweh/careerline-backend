from typing import Dict, List
from app.db.models import Pathway
from sqlalchemy.orm import Session

def deterministic_scores(inputs: Dict, db: Session) -> Dict[str, int]:
    """Apply rule-based scoring logic dynamically to all pathways in the DB."""
    pathways = db.query(Pathway).all()
    scores = {p.name: 0 for p in pathways}

    # Personality rules
    if inputs.get("personality") == "introvert":
        for name in scores:
            if "data" in name.lower():
                scores[name] += 15
            if "cyber" in name.lower():
                scores[name] += 15
            if "software" in name.lower():
                scores[name] += 10
            if "machine" in name.lower():
                scores[name] += 15
            if "robotics" in name.lower():
                scores[name] += 10

    elif inputs.get("personality") == "extrovert":
        for name in scores:
            if "marketing" in name.lower():
                scores[name] += 15
            if "product" in name.lower():
                scores[name] += 15
            if "ui" in name.lower() or "ux" in name.lower():
                scores[name] += 10

    # Motive rules
    motive = inputs.get("motive")
    if motive == "migration":
        for name in scores:
            if "data" in name.lower():
                scores[name] += 10
            if "cyber" in name.lower():
                scores[name] += 10
            if "software" in name.lower():
                scores[name] += 10
            if "machine" in name.lower():
                scores[name] += 10
            if "cloud" in name.lower():
                scores[name] += 15

    elif motive == "side hustle":
        for name in scores:
            if "marketing" in name.lower():
                scores[name] += 15
            if "design" in name.lower():
                scores[name] += 10
            if "software" in name.lower():
                scores[name] += 10

    elif motive == "new career":
        for name in scores:
            if "software" in name.lower():
                scores[name] += 15
            if "data" in name.lower():
                scores[name] += 10
            if "ai" in name.lower():
                scores[name] += 10

    elif motive == "money-making":
        for name in scores:
            if "marketing" in name.lower():
                scores[name] += 15
            if "data" in name.lower():
                scores[name] += 10

    # Age rules
    age = inputs.get("age")
    if age:
        for name in scores:
            if 18 <= age <= 25:
                if "software" in name.lower() or "data" in name.lower():
                    scores[name] += 10
            elif 26 <= age <= 40:
                if "product" in name.lower() or "data" in name.lower():
                    scores[name] += 10
            elif age > 40:
                if "product" in name.lower() or "marketing" in name.lower():
                    scores[name] += 10

    return scores


def normalize_scores(scores: Dict[str, int]) -> Dict[str, int]:
    vals = list(scores.values())
    if not vals or max(vals) == min(vals):
        return {k: 100 for k in scores}
    minv, maxv = min(vals), max(vals)
    return {k: int(100 * (v - minv) / (maxv - minv)) for k, v in scores.items()}
