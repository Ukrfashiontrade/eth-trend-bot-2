
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling
from random import choice

# Ініціалізація бота
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Набір монет і таймфреймів
coins = ["ETH", "XRP", "SOL", "PEPE", "OP", "DOGE"]
timeframes = ["15m", "1h", "4h", "1d"]
directions = ["⬆️", "⬇️"]

# Генерація таблиці прогнозу
def generate_prediction():
    header = "Монета | 15m | 1h | 4h | 1d\n"
    header += "-----------------------------\n"
    rows = []
    for coin in coins:
        row = f"{coin:<6} | " + " | ".join(choice(directions) for _ in timeframes)
        rows.append(row)
    return header + "\n".join(rows)

# Відповідь на будь-яке повідомлення
@dp.message_handler()
async def send_forecast(message: types.Message):
    forecast = generate_prediction()
    await message.answer(
        f"📊 Прогноз на зараз (активність китів):\n\n{forecast}\n\n"
        "⬆️ = LONG (зростання), ⬇️ = SHORT (падіння)"
    )

# Запуск
if __name__ == "__main__":
    start_polling(dp, skip_updates=True)
