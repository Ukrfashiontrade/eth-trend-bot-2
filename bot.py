
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling
from random import choice

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Імітація даних китової активності
coins = ["ETH", "XRP", "SOL", "PEPE", "OP", "DOGE"]
timeframes = ["15m", "1h", "4h", "1d"]
directions = ["⬆️", "⬇️"]

# Функція генерації фейкової таблиці (для демонстрації)
def generate_prediction():
    header = "Монета | 15m | 1h | 4h | 1d\n"
    header += "-----------------------------\n"
    rows = []
    for coin in coins:
        row = f"{coin:<6} | " + " | ".join(choice(directions) for _ in timeframes)
        rows.append(row)
    return header + "\n".join(rows)

# Обробка будь-якого повідомлення — автоматичний прогноз
@dp.message_handler()
async def auto_reply(message: types.Message):
    forecast = generate_prediction()
    await message.answer(
        f"📊 Прогноз на зараз (на основі активності китів):\n\n{forecast}\n\n"
        "⬆️ = LONG (зростання), ⬇️ = SHORT (падіння)"
    )

if __name__ == "__main__":
    start_polling(dp, skip_updates=True)
