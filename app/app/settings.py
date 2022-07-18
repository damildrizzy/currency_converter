import fastapi_plugins
from pydantic import BaseSettings


class Settings(fastapi_plugins.RedisSettings, BaseSettings):
    DATABASE_URL: str
    EXCHANGE_RATE_API_URL: str
    SECRET_KEY: str
    redis_host: str = "redis"

    class Config:
        env_file = "../../.env"


settings = Settings()
