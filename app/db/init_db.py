from .database import Base, engine
from .models import Pathway

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
