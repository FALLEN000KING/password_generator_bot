from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

generate_pass_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Получить пароль', callback_data='generate_pass')
    ]
])