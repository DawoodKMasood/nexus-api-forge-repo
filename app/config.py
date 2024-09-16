from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str
    RATE_LIMIT: int = 100
    
    class Config:
        env_file = ".env"

settings = Settings()