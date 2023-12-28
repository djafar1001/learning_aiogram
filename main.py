from aiogram import Bot, Dispatcher, executor, types
from setings_test import AIOGRAM_TOKEN, HELP_AIOGRAM
from string import ascii_letters
from random import choice


bot = Bot(AIOGRAM_TOKEN['token'], parse_mode='HTML')
dp = Dispatcher(bot=bot)

global count_run


@dp.message_handler(commands=['start', 'help', 'description', 'count'])
async def start_react(message: types.Message):
    if message.text.lstrip('/') == 'start':
        await  message.answer(text='Добро пожаловать в телеграм бот')
        await  message.delete()
    elif message.text.lstrip('/') == 'help':
        await message.reply(text=HELP_AIOGRAM)
    elif message.text.lstrip('/') == 'description':
        await message.answer(text='Этот бот создан для помощи в изучении библиотеки <b>AIOgram 2.x</b>')
    elif message.text.lstrip('/') == 'count':
        global count_run
        count_run += 1
        await  message.answer(text=f'Эта команда была вызвана {count_run} '
                                   f'{"раза" if count_run % 10 in [2, 3, 4] else "раз"} ')

@dp.message_handler(content_types=['text'])
async def random_letters(message: types.Message):
    if message.text.isdigit():
        await message.answer(text='YES')
    else:
        await message.answer(text='NO')

    await message.answer(text=choice(ascii_letters))

@dp.message_handler()
async def echo(message: types.Message):
    if len(message.text.split()) > 1:
        await  message.answer(text=message.text.upper())
    else:
        await  message.answer(text='В сообщении должно быть больше одного слова')


if __name__ == '__main__':
    executor.start_polling(dp)
