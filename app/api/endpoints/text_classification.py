from fastapi import APIRouter, HTTPException, Depends
from app.core.models.distilbert_sst2 import distilbert_sst2
from app.core.schemas.request import DistilBERTSST2Request
from app.core.schemas.response import DistilBERTSST2Response
from app.services.rate_limiting import rate_limiter
from app.services.usage_tracking import track_usage

router = APIRouter()

@router.post("/sentiment", response_model=DistilBERTSST2Response)
@rate_limiter(limit=10, period=60)
async def sentiment_distilbert_sst2(request: DistilBERTSST2Request):
    try:
        await track_usage(request.user_id, "distilbert_sst2_sentiment")

        sentiment = distilbert_sst2.predict(request.text)

        return DistilBERTSST2Response(sentiment=sentiment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))