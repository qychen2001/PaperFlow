from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # API配置
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = False


settings = Settings()
