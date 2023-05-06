from aiogram import types, Bot

from config import TG_TOKEN


bot = Bot(token=TG_TOKEN)


async def send_wrong_file_info_format(message: types.Message):
    await message.answer('Неверный формат. Введите информацию о файле в виде:\n' +
                         'Название соревнования\n' +
                         'Год проведения соревнования'
                         )


async def send_wrong_file_request_format(message: types.Message):
    await message.answer('\n'.join([
        'Неверный формат. Введите информацию о файле в виде:',
        'Соревнование: <название соревнования>',
        'Год: <диапазон лет>',
        '========================================',
        'Пример:',
        'Соревнование: Русская зима',
        'Год: 2019-2021, 2023'
    ]))
