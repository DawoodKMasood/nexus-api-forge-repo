from pydantic import BaseModel

class DistilBERTSST2Response(BaseModel):
    sentiment: str