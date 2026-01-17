from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os

# Загружаем токен из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Это твой бот. Нажми /tap, чтобы начать!")

# Команда /tap
@dp.message(Command("tap"))
async def tap(message: types.Message):
    await message.answer("Ты тапнул! +1 очко 🎯")

# Запуск бота
if __name__ == '__main__':
    dp.run_polling(bot)