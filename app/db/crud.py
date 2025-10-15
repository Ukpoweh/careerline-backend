from sqlalchemy.orm import Session
from .models import Pathway

def get_all_pathways(db: Session):
    """Fetch all career pathways from the database."""
    return db.query(Pathway).all()