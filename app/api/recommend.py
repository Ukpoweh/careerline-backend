from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.recommend import RecommendRequest
from app.services.scoring import deterministic_scores, normalize_scores
from app.db.database import get_db
from app.db.crud import get_all_pathways

router = APIRouter()

@router.post("/v1/recommend")
def recommend(request: RecommendRequest, db: Session = Depends(get_db)):
    # 1️⃣ Get user inputs
    inputs = request.dict()

    # 2️⃣ Fetch all available pathways from the database
    pathways = get_all_pathways(db)
    pathway_names = [p.name for p in pathways]

    # 3️⃣ Run deterministic scoring
    raw_scores = deterministic_scores(inputs)
    normalized = normalize_scores(raw_scores)

    # 4️⃣ Sort and get top 3
    top3 = sorted(normalized.items(), key=lambda x: x[1], reverse=True)[:3]

    # 5️⃣ Build the response with DB details
    recommendations = []
    for name, score in top3:
        # Find the matching pathway object
        match = next((p for p in pathways if p.name == name), None)
        if match:
            recommendations.append({
                "pathway": match.name,
                "fitness_pct": score,
                "description": match.description,
                "avg_learning_hours": match.avg_learning_hours,
                "tags": match.tags,
                "demand_score": match.demand_score
            })

    # 6️⃣ Return JSON response
    return {
        "user_inputs": inputs,
        "recommendations": recommendations
    }
