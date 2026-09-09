from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "REST Engine"
    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
