from aiogram import Router

from .users import user_router


router = Router()
router.include_router(router=user_router)
