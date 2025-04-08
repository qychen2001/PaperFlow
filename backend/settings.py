from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # API配置
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = False

    # casdoor配置
    CASDOOR_ENDPOINT: str = ""
    CASDOOR_CLIENT_ID: str = ""
    CASDOOR_CLIENT_SECRET: str = ""
    CASDOOR_CERTIFICATE: str = ""
    CASDOOR_ORG_NAME: str = ""
    CASDOOR_APPLICATION_NAME: str = ""


settings = Settings()
