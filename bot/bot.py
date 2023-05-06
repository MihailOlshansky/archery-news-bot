from aiogram import types
from aiogram.dispatcher import Dispatcher

from bot.bot_commands import *
from bot.common import bot


dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await start_command(message)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await help_command(message)


@dp.message_handler(commands=['get_protocols'])
async def process_get_protocols_command(message: types.Message):
    await get_files_command(message)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def process_add_protocol_command(message: types.Message):
    await add_file_command(message)


