from fastapi import FastAPI

app = FastAPI(
    title="AI Study Assistant API",
    description="Backend API for the AI Study Assistant",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "AI Study Assistant API is running",
        "status": "success",
        "version": "1.0.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }