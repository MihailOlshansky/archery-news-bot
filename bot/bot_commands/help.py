"""
Данная функция отвечает за обработку команды /help
Она выводит список команд
"""
from aiogram import types


async def help_command(message: types.Message):
    await message.reply('Напиши /start, чтобы начать')
