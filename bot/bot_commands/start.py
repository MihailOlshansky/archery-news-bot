"""
Данная функция отвечает за обработку команды /start
Она запускает бота
"""
from aiogram import types
from aiogram_dialog import DialogManager, StartMode

from bot.stategroups import MainSG


async def start_command(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.main_start, mode=StartMode.NEW_STACK)
