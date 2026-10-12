from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = 'SmartSchool'
    DEBUG: bool = True
    API_V1_STR: str = '/api/v1'
    BACKEND_CORS_ORIGINS: List[str] = ['http://localhost:5173','http://localhost:8081','http://localhost:19006']
    DATABASE_URL: str = 'mysql+pymysql://smart:smart@localhost:3306/smartschool'
    SECRET_KEY: str = 'dev-secret-key-change'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = '.env'

settings = Settings()

