
from pydantic import BaseSettings


class Settings(BaseSettings):
    PG_DSN: str


settings = Settings()
