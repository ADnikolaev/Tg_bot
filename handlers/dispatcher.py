from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, CallbackQuery
from keyboards.for_start import get_start_kb
from middlewares.actions import SaveMessageInLogMiddleware
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state




dispatcher = Dispatcher()
dispatcher.message.middleware(SaveMessageInLogMiddleware())
#dispatcher.message.middleware(ChatActionMiddleware())


@dispatcher.message(F.text.lower() == "главное меню")
@dispatcher.message(Command("start"))
async def start(message: Message, state: FSMContext) -> None:
        await state.clear()
        await message.answer("Выберите действие:",reply_markup = get_start_kb())


@dispatcher.callback_query(F.data == "Главное меню")
async def start_callback(callback: CallbackQuery, state: FSMContext) -> None:
        await callback.message.answer("Выберите действие:", reply_markup = get_start_kb())
#        await callback.answer(reply_markup = ReplyKeyboardRemove())
        

@dispatcher.message(StateFilter(None), Command(commands=["cancel"]))
@dispatcher.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({})
    await message.answer(
        text="Нечего отменять",
        reply_markup=ReplyKeyboardRemove()
    )
        
@dispatcher.message(Command(commands=["cancel"]))
@dispatcher.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )