from .database import SessionLocal
from .models import Pathway
import uuid

def seed_pathways():
    db = SessionLocal()

    # 🧠 All 15 Tech Pathways
    data = [
        {
            "name": "Data Analytics",
            "description": "Collect and interpret data to support decision-making using Excel, SQL, and Python.",
            "avg_learning_hours": 120,
            "tags": ["data", "excel", "sql", "python", "analytics"],
            "demand_score": 0.9
        },
        {
            "name": "Software Development",
            "description": "Build web and mobile apps using modern programming languages and frameworks.",
            "avg_learning_hours": 200,
            "tags": ["coding", "web", "apps", "python", "javascript"],
            "demand_score": 0.95
        },
        {
            "name": "Cybersecurity",
            "description": "Protect computer systems and networks from digital attacks.",
            "avg_learning_hours": 150,
            "tags": ["security", "ethical-hacking", "network", "linux"],
            "demand_score": 0.88
        },
        {
            "name": "Machine Learning Engineering",
            "description": "Build models that allow computers to learn from data and make predictions.",
            "avg_learning_hours": 250,
            "tags": ["ai", "ml", "python", "tensorflow", "pytorch"],
            "demand_score": 0.96
        },
        {
            "name": "Data Science",
            "description": "Combine statistics, machine learning, and domain expertise to extract insights.",
            "avg_learning_hours": 220,
            "tags": ["data", "ml", "python", "pandas", "analytics"],
            "demand_score": 0.94
        },
        {
            "name": "UI/UX Design",
            "description": "Design intuitive user interfaces and experiences for web and mobile products.",
            "avg_learning_hours": 140,
            "tags": ["design", "figma", "user-experience", "ui", "ux"],
            "demand_score": 0.89
        },
        {
            "name": "Product Management",
            "description": "Oversee tech product strategy, roadmap, and execution.",
            "avg_learning_hours": 180,
            "tags": ["business", "agile", "leadership", "tech", "strategy"],
            "demand_score": 0.91
        },
        {
            "name": "Cloud Computing",
            "description": "Design and manage applications deployed on cloud platforms (AWS, Azure, GCP).",
            "avg_learning_hours": 180,
            "tags": ["cloud", "aws", "azure", "devops", "docker"],
            "demand_score": 0.93
        },
        {
            "name": "DevOps Engineering",
            "description": "Integrate development and operations to automate software delivery.",
            "avg_learning_hours": 200,
            "tags": ["devops", "ci/cd", "cloud", "kubernetes", "automation"],
            "demand_score": 0.9
        },
        {
            "name": "Blockchain Development",
            "description": "Build decentralized applications and smart contracts.",
            "avg_learning_hours": 200,
            "tags": ["blockchain", "solidity", "crypto", "web3"],
            "demand_score": 0.87
        },
        {
            "name": "Digital Marketing",
            "description": "Use SEO, content, and social media to grow online presence.",
            "avg_learning_hours": 100,
            "tags": ["seo", "ads", "social-media", "content"],
            "demand_score": 0.92
        },
        {
            "name": "Artificial Intelligence",
            "description": "Build systems that can perceive, reason, and act intelligently.",
            "avg_learning_hours": 260,
            "tags": ["ai", "deep-learning", "nlp", "vision"],
            "demand_score": 0.95
        },
        {
            "name": "Robotics",
            "description": "Design and program autonomous robots and control systems.",
            "avg_learning_hours": 250,
            "tags": ["hardware", "python", "ai", "electronics", "automation"],
            "demand_score": 0.85
        },
        {
            "name": "Game Development",
            "description": "Design, code, and test interactive games across platforms.",
            "avg_learning_hours": 200,
            "tags": ["unity", "csharp", "game-design", "3d"],
            "demand_score": 0.84
        },
        {
            "name": "Cloud Security",
            "description": "Focus on protecting cloud infrastructures and data.",
            "avg_learning_hours": 180,
            "tags": ["cloud", "security", "aws", "azure"],
            "demand_score": 0.9
        },
    ]

    # 🧩 Prevent duplicates — check before adding
    for p in data:
        exists = db.query(Pathway).filter_by(name=p["name"]).first()
        if not exists:
            new_pathway = Pathway(
                id=str(uuid.uuid4()),
                name=p["name"],
                description=p["description"],
                avg_learning_hours=p["avg_learning_hours"],
                tags=p["tags"],
                demand_score=p["demand_score"]
            )
            db.add(new_pathway)

    db.commit()
    db.close()
    print("✅ All 15 tech pathways added successfully (no duplicates)!")

if __name__ == "__main__":
    seed_pathways()
