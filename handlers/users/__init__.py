from aiogram import Router

from .start import start_router
from .currency import currency_router


user_router = Router(name='user')
user_router.include_router(router=start_router)
user_router.include_router(router=currency_router)
