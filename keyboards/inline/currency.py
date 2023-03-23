from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class CurrencyCallbackData(CallbackData, prefix='currency'):
    currency: str


currency_list_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='💵 USD',
                callback_data=CurrencyCallbackData(currency='USD').pack()
            ),
            InlineKeyboardButton(
                text='💶 EUR',
                callback_data=CurrencyCallbackData(currency='EUR').pack()
            ),
            InlineKeyboardButton(
                text='🇷🇺 RUR',
                callback_data=CurrencyCallbackData(currency='RUR').pack()
            )
        ]
    ]
)
