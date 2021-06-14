from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    db_url:str = 'sqlite:///./db.sqlite3'


settings = Settings()