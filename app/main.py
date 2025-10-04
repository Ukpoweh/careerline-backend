from fastapi import FastAPI
from app.api import recommend

app = FastAPI(title="CareerLine AI Backend", version="1.0")

app.include_router(recommend.router)

@app.get("/health")
def health():
    return {"status": "ok"}

