from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from configanddata.fsm_data import FSM_pass
from data_base import db
from services import generate_pass_from_ids as gen
from keyboards import ask_to_reply

router = Router()

@router.callback_query(StateFilter(FSM_pass.ending), F.data == 'generate_pass')
async def gen_p(call: CallbackQuery):
    await call.answer()
    true_password = gen.get_random_pass(db_user=db[call.from_user.id])
    await call.message.answer(f'Твой пароль готов!\n <code>{true_password}</code>', parse_mode='HTML', reply_markup=ask_to_reply.reply_kbs)
    
@router.callback_query(StateFilter(FSM_pass.ending), F.data == 'regenarate_passw')
async def regenerate_pass_w(call: CallbackQuery):
    await call.answer()
    regeneran_passw = gen.get_random_pass(db_user=db[call.from_user.id])
    await call.message.edit_text(f'Вот перегенерированный пароль:\n\n<code>{regeneran_passw}</code>', reply_markup=ask_to_reply.reply_kbs, parse_mode='HTML')
    
@router.callback_query(StateFilter(FSM_pass.ending), F.data == 'start_generate_too')
async def and_to_genetation(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(FSM_pass.number_of_pass)
    
    await call.message.answer('Ок, напиши сколько символов с своем пароле ты хочешь? (До 100)')