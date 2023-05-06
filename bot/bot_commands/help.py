"""
Данная функция отвечает за обработку команды /help
Она выводит список команд
"""
from aiogram import types
from aiogram.utils.markdown import text


async def help_command(message: types.Message):
    commands = ['/help: Выводит список всех команд',
                '/add_protocol: Позволяет добавить новый протокол',
                '/get_protocols: Позволяет получить отчёты с соревнований по названию и году проведения']
    msg = text('У меня есть следующие команды:', *commands, sep='\n')
    await message.reply(msg)
