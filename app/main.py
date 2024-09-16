from fastapi import FastAPI
from app.api.endpoints import text_classification

app = FastAPI()

app.include_router(text_classification.router, prefix="/api/v1/text-classification", tags=["text-classification"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API service"}