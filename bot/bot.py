from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram_dialog import DialogRegistry, DialogManager

from bot.bot_commands import *
from bot.common import bot
from bot.dialogs import main_dialog

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)
registry.register(main_dialog)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message, dialog_manager: DialogManager):
    await start_command(message, dialog_manager)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def process_add_file_command(message: types.Message, dialog_manager: DialogManager):
    await add_file_command(message, dialog_manager)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def process_add_protocol_command(message: types.Message, dialog_manager: DialogManager):
    await add_file_command(message, dialog_manager)
