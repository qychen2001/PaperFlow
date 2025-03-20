from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    # 数据库配置
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "ainterview"

    # API配置
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000

    # CORS配置
    CORS_ORIGINS: List[str] = ["http://localhost:5173"]

    # Casdoor配置
    CASDOOR_ENDPOINT: str
    CASDOOR_CLIENT_ID: str
    CASDOOR_CLIENT_SECRET: str
    CASDOOR_CERTIFICATE: str
    CASDOOR_ORG_NAME: str
    CASDOOR_APPLICATION_NAME: str

    # API配置
    OPENAI_BASE_URL: str
    OPENAI_API_KEY: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
