from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message
from configanddata.fsm_data import FSM_pass
from keyboards import start_kb
from data_base import db

router = Router()

@router.message(StateFilter(default_state), CommandStart())
async def start(message: Message):
    db[message.from_user.id] = [0, False, False, False, False]
    await message.answer('Привет я бот, который поможет тебе сгенерировать сложный и уникальный пароль! Чтобы начать нажми на кнопку ⬇️', reply_markup=start_kb.start_kb)
    
@router.message(StateFilter(default_state))
async def als0(message: Message):
    await message.answer('Ты хочешь создать пароль?', reply_markup=start_kb.start_kb)
    
@router.callback_query(StateFilter(default_state), F.data == 'start_genegation')
async def start_generations(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer('Какое количество символов пароля ты хочешь? (До 100)')
    await state.set_state(FSM_pass.number_of_pass)