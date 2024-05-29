import asyncio
import logging

from aiogram import Bot, Dispatcher
from configanddata import fsm_data
from handlers import start_handler, number_of_pass_handler, letter_for_pass, is_caps_handler, spec_simv_handler, ending_handler
from datatoken import token
# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')


    # Инициализируем бот и диспетчер
    bot = Bot(token=token)
    dp = Dispatcher(storage=fsm_data.storage)

    # Регистриуем роутеры в диспетчере
    dp.include_router(start_handler.router)
    dp.include_router(number_of_pass_handler.router)
    dp.include_router(letter_for_pass.router)
    dp.include_router(is_caps_handler.router)
    dp.include_router(spec_simv_handler.router)
    dp.include_router(ending_handler.router)


    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())