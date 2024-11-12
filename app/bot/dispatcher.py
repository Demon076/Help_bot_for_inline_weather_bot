from aiogram import Dispatcher

from app.handlers import base
from app.middlewares.bot_info.LogMiddleware import LogMiddleware

dp = Dispatcher()


def registration_dispatcher(dispatcher: Dispatcher) -> None:
    dispatcher.update.middleware(LogMiddleware())
    dispatcher.include_router(base.router)
