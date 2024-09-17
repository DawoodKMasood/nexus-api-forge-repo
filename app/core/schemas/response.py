from typing import List
from pydantic import BaseModel

class DistilBERTSST2Response(BaseModel):
    sentiment: str

class SentimentLabel(BaseModel):
    label: str
    score: float

class RoBERTaSentimentResponse(BaseModel):
    sentiments: List[SentimentLabel]