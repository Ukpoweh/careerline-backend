from sqlalchemy import Column, String, Integer, Float, DateTime, JSON
from datetime import datetime
from .database import Base

class Pathway(Base):
    __tablename__ = "pathways"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    avg_learning_hours = Column(Integer)
    tags = Column(JSON)
    demand_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
