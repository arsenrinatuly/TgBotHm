from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

CURRENCY = ["USD","RUB", "KZT"]

def get_currency_keyboard(currency_to_remove: str = None):
    if currency_to_remove:
        CURRENCY.remove(currency_to_remove)
    builder = InlineKeyboardBuilder()
    for item in CURRENCY:
        builder.row(InlineKeyboardButton(
            text=item, callback_data=item
        ))
    return builder.as_markup()