from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = "localhost"
    server_port: int = 8000
    db_url: str = "sqlite:///./db.db"


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
