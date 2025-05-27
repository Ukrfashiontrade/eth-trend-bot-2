import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("🔮 Прогноз ETH та топ-5 монет: ВГОРУ ⬆️ на 1 день")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
