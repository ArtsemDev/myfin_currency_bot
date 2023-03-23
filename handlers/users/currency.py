from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.inline import CurrencyCallbackData, currency_list_ikb
from utils.myfin import MyfinAPI


currency_router = Router(name='currency')


@currency_router.callback_query(CurrencyCallbackData.filter())
async def currency(callback: CallbackQuery, callback_data: CurrencyCallbackData):
    data = await MyfinAPI.currency(currency=callback_data.currency)
    if data:
        text = f'***{callback_data.currency}\t|\tBUY\t|\tSELL***\n\n'
        for bank, values in data.items():
            text += f'***{bank} |*** ___{values[callback_data.currency]["buy"]}___ ***|*** ___{values[callback_data.currency]["sell"]}___\n'
        await callback.message.edit_text(
            text=text,
            reply_markup=currency_list_ikb
        )
    else:
        await callback.message.edit_text(
            text='Извините сервис временно не доступен!',
            reply_markup=currency_list_ikb
        )
