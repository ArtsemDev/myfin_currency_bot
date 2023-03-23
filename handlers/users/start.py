from aiogram import Router, F
from aiogram.types import Message

from keyboards.inline import currency_list_ikb


start_router = Router(name='start')


@start_router.message(F.text == '/start')
async def start_command(message: Message):
    await message.delete()
    await message.answer(
        text=f'Привет {message.from_user.username}!\n Выбери валюту!',
        reply_markup=currency_list_ikb
    )
