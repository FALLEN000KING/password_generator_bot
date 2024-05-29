from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from configanddata.fsm_data import FSM_pass
from data_base import db
from keyboards import generate_pass
from keyboards import yes_or_no

router = Router()

@router.callback_query(StateFilter(FSM_pass.spec_simv), F.data == 'yes_da')
async def spec_simv_yes_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    db[call.from_user.id][4] = True
    await state.set_state(FSM_pass.ending)
    await call.message.answer('Отлично, нажми на кнопку чтобы сгенерировать пароль', reply_markup=generate_pass.generate_pass_kb)

@router.callback_query(StateFilter(FSM_pass.spec_simv), F.data == 'no_net')
async def spec_simv_no_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    db[call.from_user.id][4] = False
    await state.set_state(FSM_pass.ending)
    await call.message.answer('Отлично, нажми на кнопку чтобы сгенерировать пароль', reply_markup=generate_pass.generate_pass_kb)
    
@router.message(StateFilter(FSM_pass.spec_simv))
async def ldknfvdkfvsddf(message: Message):
    await message.answer('Будет ли твой пароль содержать спец. символы?', reply_markup=yes_or_no.yes_or_no)