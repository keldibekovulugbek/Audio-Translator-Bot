import logging
from loader import dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

languages = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🇺🇿 Uzbek", callback_data="uzbek_lang"),
        InlineKeyboardButton(text="🇬🇧 English", callback_data="enlish_lang"),
    ]
])