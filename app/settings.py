from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Из database.py
    MONGO_URI: str = "mongodb://mongo:27017"
    # [cite_start]Из вашего .env [cite: 3]
    DB_NAME: str = "notdb"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

# Синглтон-экземпляр настроек
settings = Settings()