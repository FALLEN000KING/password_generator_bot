from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from configanddata.fsm_data import FSM_pass
from data_base import db
from keyboards import yes_or_no

router = Router()

@router.callback_query(StateFilter(FSM_pass.is_caps), F.data == 'yes_da')
async def is_caps_yes_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    db[call.from_user.id][2] = True
    await state.set_state(FSM_pass.spec_simv)
    await call.message.answer('Последнее, будет ли твой пароль содержать специальные символы? (Это ?*. и т.д)', reply_markup=yes_or_no.yes_or_no)
    
    
@router.callback_query(StateFilter(FSM_pass.is_caps), F.data == 'no_net')
async def is_caps_no_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    db[call.from_user.id][2] = False
    await state.set_state(FSM_pass.spec_simv)
    await call.message.answer('Последнее, будет ли твой пароль содержать специальные символы? (Это ?*. и т.д)', reply_markup=yes_or_no.yes_or_no)
    
@router.message(StateFilter(FSM_pass.is_caps))
async def jsbdljvsdbv(message: Message):
    await message.answer('Твой пароль будет содержать заглавные буквы?', reply_markup=yes_or_no.yes_or_no)