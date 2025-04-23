from dotenv import load_dotenv
import os

# Carga automáticamente el .env si no estás en producción
load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL") or ""
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"


settings = Settings()
