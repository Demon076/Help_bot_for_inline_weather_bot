from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    TOKEN: str
    ADMIN: int


bot_settings = BotSettings()

if __name__ == "__main__":
    print(bot_settings.TOKEN)
