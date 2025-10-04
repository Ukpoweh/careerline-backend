from fastapi import FastAPI

# Create the app
app = FastAPI(title="CareerLine AI Backend", version="1.0")

# A simple test route
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "CareerLine AI backend running"}
