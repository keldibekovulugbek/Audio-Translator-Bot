from aiogram import types
from loader import dp
from aiogram.types import ContentType
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from keyboards.inline.language import languages
from pathlib import Path

from utils import eng


@dp.message_handler(content_types=ContentType.VOICE)
async def save_audio(message: types.voice):
    file_id = message.voice.file_id
    await message.voice.download()
    await message.answer("Qaysi tilga tarjima qilish kerak?", reply_markup=languages)

@dp.callback_query_handler(text="uzbek_lang")
async def eng_to_uz(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=20)
    path_audio = sorted([str(x) for x in Path('voice/').glob('*.oga')])[-1]
    await call.message.answer(path_audio)
    path_audio = await eng.any2mp(path_audio)
    eng_text = await eng.stt(path_audio)
    await call.message.answer(eng_text)
    await call.message.answer("Uz tilini tanladingiz")

@dp.callback_query_handler(text="enlish_lang")
async def eng_to_uz(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=20)
    await call.message.answer("Ingliz tilini tanladingiz")

    path_audio = sorted([str(x) for x in Path('voice/').glob('*.oga')])[-1]
    await call.message.answer(path_audio)

    # STT uzbek
    
    files = {
                'file': open(path_audio, 'rb'),
                    }

    response = requests.post('http://213.230.107.46:9998/uploadfile/', files=files)
    natija = response.json()
    natija = natija.replace("ʻ", "'")
    await call.message.answer(natija)

