from .database import SessionLocal
from .models import Pathway
import uuid

def seed_pathways():
    db = SessionLocal()
    data = [
        Pathway(
            id=str(uuid.uuid4()),
            name="Data Analysis",
            description="Collect, clean, and analyze data to make informed decisions.",
            avg_learning_hours=120,
            tags=["data", "analytics", "excel", "python"],
            demand_score=0.90
        ),
        Pathway(
            id=str(uuid.uuid4()),
            name="Cybersecurity",
            description="Protect digital systems from cyber threats and attacks.",
            avg_learning_hours=150,
            tags=["security", "network", "ethical-hacking"],
            demand_score=0.88
        ),
        Pathway(
            id=str(uuid.uuid4()),
            name="Software Development",
            description="Design and build software applications for web and mobile.",
            avg_learning_hours=200,
            tags=["coding", "web", "apps", "python"],
            demand_score=0.95
        )
    ]

    db.add_all(data)
    db.commit()
    db.close()
    print("✅ Sample pathways added successfully!")

if __name__ == "__main__":
    seed_pathways()
