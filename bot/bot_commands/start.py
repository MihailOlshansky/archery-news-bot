"""
Данная функция отвечает за обработку команды /start
Она запускает бота
"""
from aiogram import types


async def start_command(message: types.Message):
    await message.answer("Привет!\nНапиши /help, чтобы посмотреть список команд")
