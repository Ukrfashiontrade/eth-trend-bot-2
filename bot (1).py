import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode

BOT_TOKEN = "7625720096:AAGUKIPmKFF5Oy7V6GCa1oL0AkNiLtM8p4E"
OWNER_ID = 762572009  # Твій Telegram ID (вказаний правильно)

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

@dp.message()
async def handle_message(message: Message):
    if str(message.chat.id) != str(OWNER_ID):
        await message.answer("⛔️ Цей бот приватний.")
        return

    # Тут буде відповідь бота
    await message.answer(
        "📊 <b>Прогноз по ETH:</b>\n🔺 Напрям: Вгору\n⏱️ Період: 1 день\n\n"
        "🐋 <b>ТОП 5 монет з активністю китів:</b>\n"
        "1. PEPE — 🔻 вниз\n"
        "2. WIF — 🔺 вгору\n"
        "3. ETH — 🔺 вгору\n"
        "4. ARB — 🔻 вниз\n"
        "5. DOGE — 🔺 вгору\n"
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
