from aiogram import Dispatcher

from app.handlers import base, appeal_to_support
from app.middlewares.bot_info.LogMiddleware import LogMiddleware

dp = Dispatcher()


def registration_dispatcher(dispatcher: Dispatcher) -> None:
    dispatcher.update.outer_middleware(LogMiddleware())
    dispatcher.include_routers(
        base.router,
        appeal_to_support.router
    )
