from pydantic import BaseModel, Field

class DistilBERTSST2Request(BaseModel):
    text: str = Field(default="I love you", description="The text to analyze for sentiment")

class RoBERTaSentimentRequest(BaseModel):
    text: str = Field(default="I love you", description="The text to analyze for sentiment")

class MultilingualSentimentRequest(BaseModel):
    text: str = Field(default="I love you", description="The text to analyze for sentiment")