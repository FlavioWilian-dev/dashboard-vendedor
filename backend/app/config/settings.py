import sys
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parents[3]


ENV_FILE = BASE_DIR / ".env"

load_dotenv(
    ENV_FILE,
    override=False
)


class Settings(BaseSettings):
    db_server: str
    db_port: int
    db_user: str
    db_password: str

    db_shalon: str
    db_veracci: str

    app_host: str = "127.0.0.1"
    app_port: int = 8000

    model_config = SettingsConfigDict(
        case_sensitive=False
    )


settings = Settings()