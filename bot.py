
import logging

from aiogram import Bot, Dispatcher, executor, types
from test_file import checkWord, has_cyrillic, checkLatin

API_TOKEN = '5231171012:AAEFThS7lsVGDjlVBzGIWDBrAJ4aHI1JAJo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("uz_imlo Botiga Xush Kelibsiz!")

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring.")

@dp.message_handler()
async def checkImlo(message: types.Message):
    global response
    words = message.text.split()
    for word in words:
        if has_cyrillic(word):
            result = checkWord(word)
        else:
            result = checkLatin(word)
        if result['available']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌{word.capitalize()}\n"
            for text in result['matches']:
                response += f"✅ {text.capitalize()}\n"
        await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)