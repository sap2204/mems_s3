from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class for sensitive data"""

    DB_HOST : str
    DB_PORT : int
    DB_USER : str
    DB_PASS : str
    DB_NAME : str

    @property
    def get_database_url(self):
        """Method for generate url for database"""
        return (
            f'postgresql+asyncpg://{self.DB_USER}:'
            f'{self.DB_PASS}@{self.DB_HOST}:'
            f'{self.DB_PORT}/{self.DB_NAME}'
        )


    model_config = SettingsConfigDict(env_file=".env")


setting = Settings()
