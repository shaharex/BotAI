from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from typing import ClassVar


class Settings(BaseSettings):
    bot_token: SecretStr
    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


config = Settings()