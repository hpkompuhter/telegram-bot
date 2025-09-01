import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("API_TOKEN")
ADMIN_ID = 5508120539  # O'zingni Telegram ID'ingni yoz

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: Message):
    await message.answer("👋 Salom! Bot ishlayapti!")

@dp.message_handler(commands=["admin"])
async def admin_cmd(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("🔑 Admin panelga xush kelibsiz!")
    else:
        await message.answer("⛔ Siz admin emassiz!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)