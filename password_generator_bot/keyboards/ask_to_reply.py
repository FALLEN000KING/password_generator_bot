from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

reply_kbs = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Перегенерировать пароль', callback_data='regenarate_passw')
    ],
    [
        InlineKeyboardButton(text='Начать генерацию заново', callback_data='start_generate_too')
    ]
])