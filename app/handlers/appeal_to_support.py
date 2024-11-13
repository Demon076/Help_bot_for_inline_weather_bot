from datetime import datetime
from datetime import timezone
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from app.bot.bot import bot
from app.bot.settings import bot_settings
from app.middlewares.bot_info.update_to_str import general_to_str

router = Router()

users_limit = {}


class AppealState(StatesGroup):
    appeal_to_support = State()


@router.message(Command("appeal_to_support"))
async def appeal_to_support_cmd(
        message: types.Message,
        state: FSMContext
):
    await message.answer(f"ВНИМАНИЕ!"
                         f" После первого обращения надо ждать минимум минуту, чтобы отправить второе!!!!\n\n"
                         f"Напишите своё обращение, следующим сообщением:")
    await state.set_state(AppealState.appeal_to_support)


@router.message(AppealState.appeal_to_support)
async def appeal_to_support_state(
        message: types.Message,
        state: FSMContext
):
    if message.from_user.id in users_limit:
        time_difference = datetime.now(timezone.utc) - users_limit[message.from_user.id]
        if time_difference.total_seconds() < 60:
            return

    await bot.send_message(
        chat_id=bot_settings.ADMIN,
        text=general_to_str(message)
    )
    await bot.copy_message(
        chat_id=bot_settings.ADMIN,
        from_chat_id=message.from_user.id,
        message_id=message.message_id
    )

    users_limit[message.from_user.id] = datetime.now(timezone.utc)
    await message.answer(text="Спасибо, обращение отправлено!!")
    await state.clear()
