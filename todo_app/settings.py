import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = "localhost"
    server_port: int = 8000
    db_url: str = os.environ.get("DATABSE_URL", "sqlite://../db.db")
    secret_key: str = os.environ.get("SECRET_KEY", "1234567890")
    reload: bool = True
    workers: int = 4
    jwt_token_expiration: int = 1800
    jwt_algorithm: str = os.environ.get("JWT_ALGORITHM", "HS256")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
