from fastapi import APIRouter
from app.schemas.recommend import RecommendRequest
from app.services.scoring import deterministic_scores, normalize_scores

router = APIRouter()

@router.post("/v1/recommend")
def recommend(request: RecommendRequest):
    inputs = request.dict()
    raw_scores = deterministic_scores(inputs)
    normalized = normalize_scores(raw_scores)

    # Sort and pick top 3
    top3 = sorted(normalized.items(), key=lambda x: x[1], reverse=True)[:3]
    recommendations = [{"pathway": p, "fitness_pct": s} for p, s in top3]

    return {
        "user_inputs": inputs,
        "recommendations": recommendations
    }

