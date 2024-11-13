import logging

from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update

from app.middlewares.bot_info.update_to_str import update_to_str


class LogMiddleware(BaseMiddleware):
    @staticmethod
    def bot_log(update: Update):
        try:
            log = update_to_str(update)
            if log is not None:
                logging.info(log)
        except Exception as ex:
            text = (f'Ошибка при записи логов!!\n'
                    f'{ex}\n')
            logger = logging.getLogger(__name__)
            logger.error(text)

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            update: Update,
            data: Dict[str, Any]
    ) -> Any:
        self.bot_log(update)

        return await handler(update, data)
