from fastapi import APIRouter, HTTPException
from app.core.models.distilbert_sst2 import distilbert_sst2
from app.core.models.roberta_sentiment import roberta_sentiment
from app.core.schemas.request import DistilBERTSST2Request, RoBERTaSentimentRequest
from app.core.schemas.response import DistilBERTSST2Response, RoBERTaSentimentResponse, SentimentLabel

router = APIRouter()

@router.post("/general-sentiment", response_model=DistilBERTSST2Response)
async def sentiment_distilbert_sst2(request: DistilBERTSST2Request):
    try:
        sentiment = distilbert_sst2.predict(request.text)
        return DistilBERTSST2Response(sentiment=sentiment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/twitter-sentiment", response_model=RoBERTaSentimentResponse)
async def sentiment_roberta(request: RoBERTaSentimentRequest):
    try:
        sentiments = roberta_sentiment.predict(request.text)
        return RoBERTaSentimentResponse(sentiments=[SentimentLabel(label=s['label'], score=s['score']) for s in sentiments])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))