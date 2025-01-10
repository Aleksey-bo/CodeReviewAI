from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerConfig(BaseSettings):
    GITHUB_TOKEN: str

    model_config = SettingsConfigDict(env_file=".env")


server_config = ServerConfig()