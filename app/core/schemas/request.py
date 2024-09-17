from pydantic import BaseModel

class DistilBERTSST2Request(BaseModel):
    text: str

class RoBERTaSentimentRequest(BaseModel):
    text: str