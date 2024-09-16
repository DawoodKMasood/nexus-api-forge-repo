from pydantic import BaseModel

class DistilBERTSST2Request(BaseModel):
    user_id: str
    text: str