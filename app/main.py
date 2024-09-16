from fastapi import FastAPI, Depends
from fastapi.security import APIKeyHeader
from app.api.endpoints import text_classification
from app.security import get_api_key

app = FastAPI(
    title="Nexus API Forge",
    description="This repo is for nexus-api-forge project.",
    version="1.0.0"
)

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

app.include_router(
    text_classification.router,
    prefix="/api/v1/text-classification",
    tags=["text-classification"],
    dependencies=[Depends(get_api_key)]
)

@app.get("/")
async def root():
    return {"message": "Service is running!"}