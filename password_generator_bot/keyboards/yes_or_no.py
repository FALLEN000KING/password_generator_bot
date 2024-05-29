from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

yes_or_no = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Да', callback_data='yes_da')
    ],
    [
        InlineKeyboardButton(text='Нет', callback_data='no_net')
    ]
])