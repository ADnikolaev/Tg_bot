from keyboards.to_main_menu import get_menu_kb
from aiogram import Router, F
from aiogram.types import Message,  FSInputFile, ReplyKeyboardRemove
from utils.photo_frame import Frame


router = Router()


@router.message(F.text.lower() == 'работа с фото')
async def photo_handler(message: Message)  -> None:
    await message.answer("Жду фашу фотографию")
#   await message.answer(reply_markup = ReplyKeyboardRemove())

@router.message(F.photo)
async def photoshop(message: Message)  -> None:
    photo_data = message.photo[-1]
    #Сделай более понятные названия методов. Типа create_frame
    frame_path = Frame(photo_data.file_id).frame()
    await message.answer("Вот ваша фотография")
    await message.answer_photo(FSInputFile(frame_path), reply_markup = get_menu_kb()) 
#    await message.answer(reply_markup = ReplyKeyboardRemove())
