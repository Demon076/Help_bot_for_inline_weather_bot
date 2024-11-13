from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет, я бот помощник для @inline_weather_bot здесь можно оставить обращение для этого бота!"
    )
