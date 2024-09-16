from pydantic import BaseModel

class DistilBERTSST2Request(BaseModel):
    text: str