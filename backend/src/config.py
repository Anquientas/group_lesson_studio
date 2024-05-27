from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_TEST_NAME: str
    DB_TEST_USER: str
    DB_TEST_PASSWORD: str
    DB_TEST_HOST: str
    DB_TEST_PORT: int

    model_config = SettingsConfigDict(env_file='../.env')

    @property
    def DATABASE_TEST_URL(self):
        return (
            f'postgresql+asyncpg://{self.DB_TEST_USER}'
            f':{self.DB_TEST_PASSWORD}'
            f'@{self.DB_TEST_HOST}:{self.DB_TEST_PORT}/{self.DB_TEST_NAME}'
        )


settings = Settings()


print(
    'parameters = ',
    settings.DB_TEST_NAME,
    settings.DB_TEST_USER,
    settings.DB_TEST_PASSWORD,
    settings.DB_TEST_HOST,
    settings.DB_TEST_PORT,
)

print(
    'settings_async = ',
    settings.DATABASE_TEST_URL
)
