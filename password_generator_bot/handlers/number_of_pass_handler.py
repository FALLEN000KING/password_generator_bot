from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from configanddata.fsm_data import FSM_pass
from data_base import db
from keyboards import yes_or_no

router = Router()

@router.message(StateFilter(FSM_pass.number_of_pass))
async def gen_pass_too(message:Message, state: FSMContext):
    try:
        mess = int(message.text)
        if mess <= 100 and mess > 0:
            db[message.from_user.id][0] = mess
            await message.answer('Хорошо, теперь скажи будут ли цифры в твоем пароле?', reply_markup=yes_or_no.yes_or_no)
            await state.set_state(FSM_pass.number_yes_or_no)
        else:
            await message.answer('Число должно быть больше 0 и меньше 100')
    except:
        await message.answer('Вы должны отправить <strong>цифру</strong>', parse_mode='HTML')
        
        
@router.callback_query(StateFilter(FSM_pass.number_yes_or_no), F.data == 'yes_da')
async def yes_numbers_kb(call: CallbackQuery, state: FSMContext):
    await call.answer()
    db[call.from_user.id][1] = True
    await state.set_state(FSM_pass.yes_or_no_letters)
    await call.message.answer('Записал... Будет ли твой пароль содержать буквы?', reply_markup=yes_or_no.yes_or_no)
    
@router.callback_query(StateFilter(FSM_pass.number_yes_or_no), F.data == 'no_net')
async def no_numbers_kb(call: CallbackQuery, state: FSMContext):
    await call.answer()
    db[call.from_user.id][1] = False
    await state.set_state(FSM_pass.yes_or_no_letters)
    await call.message.answer('Тогда будет ли содержать твой пароль буквы?', reply_markup=yes_or_no.yes_or_no)
    
@router.message(StateFilter(FSM_pass.number_yes_or_no))
async def sdcsdcsdc(message: Message):
    await message.answer('Твой пароль будет содержать цифры?', reply_markup=yes_or_no.yes_or_no)