from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

history_exchanges_router = Router()

exchange_history = []

@history_exchanges_router.message(Command("history"))
async def show_exchange_history(message: Message):
    if exchange_history:
        history_text = "\n".join([f"{i['current_currency']} -> {i['new_currency']} | {i['text']} = {i['result']}"
                                for i in exchange_history])
    else:
        history_text = "История обменов пуста."

    await message.answer(text=history_text)





