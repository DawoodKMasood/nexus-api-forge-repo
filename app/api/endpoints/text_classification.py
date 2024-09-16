from fastapi import APIRouter, HTTPException, Request
from app.core.models.distilbert_sst2 import distilbert_sst2
from app.core.schemas.request import DistilBERTSST2Request
from app.core.schemas.response import DistilBERTSST2Response

router = APIRouter()

@router.post("/sentiment", response_model=DistilBERTSST2Response)
async def sentiment_distilbert_sst2(request: DistilBERTSST2Request):
    try:
        sentiment = distilbert_sst2.predict(request.text)
        return DistilBERTSST2Response(sentiment=sentiment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))