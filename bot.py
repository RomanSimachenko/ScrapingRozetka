import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink
import os


def post_to_telegram(products):
    API_TOKEN = os.getenv('API_TOKEN')

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)

    @dp.message_handler(commands='start')
    async def start(message: types.Message):
        await message.answer("Все товары: ")
        for product in products:
            card = f"{hlink(product['title'], product['link'])}\n" \
                f"{hbold('Price: ')} {product['price']}\n" \
                f"{hbold('Status: ')} {product['status']}\n" \
                f"{hbold('Defect: ')} {product['defect']}"
            await message.answer(card)

    executor.start_polling(dp)
