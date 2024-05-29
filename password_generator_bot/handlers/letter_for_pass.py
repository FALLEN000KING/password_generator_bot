from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from configanddata.fsm_data import FSM_pass
from data_base import db
from keyboards import yes_or_no

router = Router()

@router.callback_query(StateFilter(FSM_pass.yes_or_no_letters), F.data == 'yes_da')
async def yes_da_buckva(call: CallbackQuery, state: FSMContext):
    await call.answer()
    db[call.from_user.id][1] = True
    await state.set_state(FSM_pass.is_caps)
    await call.message.answer('Прекрасно, в твоем пароле будет содержаться заглавные буквы?', reply_markup=yes_or_no.yes_or_no)


@router.callback_query(StateFilter(FSM_pass.yes_or_no_letters), F.data == 'no_net')
async def no_net_buckva(call: CallbackQuery, state: FSMContext):
    await call.answer()
    db[call.from_user.id][2] = False
    db[call.from_user.id][3] = False
    await state.set_state(FSM_pass.spec_simv)
    await call.message.answer('Будет ли содержаться в твоем пароле спец символы? (Такие как ?.* и т.д)', reply_markup=yes_or_no.yes_or_no)

@router.message(StateFilter(FSM_pass.yes_or_no_letters))
async def yes_or_no_i_dont_know(message: Message):
    await message.answer('Твой пароль будет содержать буквы?', reply_markup=yes_or_no.yes_or_no)