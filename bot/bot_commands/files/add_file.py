"""
Данная функция отвечает за обработку команды /add_protocol
Она позволяет сохранить протокол в бд
"""
import re

from aiogram import types
from aiogram_dialog import DialogManager

from bot.common import send_wrong_file_info_format
from database import is_admin
from database.tables import FILE_TYPE
from database.tables.file import COMPETITION, COMPETITION_YEAR, FILE_ID, FILE_FORMAT
from database.database_commands import insert_file_data


async def add_file_command(message: types.Message):
    if not is_admin(message.from_user.username):
        return

    file_id: str = message.document.file_id
    file_format = message.document.file_name.split('.')[-1]
    try:
        parameters = re.sub(r"^/add_protocol\s*", '', message.html_text)
        parameters = re.sub(r"\s+", ' ', parameters).split()
    except Exception as e:
        print(e)
        await send_wrong_file_info_format(message)
        return

    if len(parameters) != 2:
        await send_wrong_file_info_format(message)
        return

    data = {
        COMPETITION: parameters[0],
        COMPETITION_YEAR: int(parameters[1]),
        FILE_ID: file_id,
        FILE_FORMAT: file_format,
        FILE_TYPE: 'Протокол'
    }
    insert_file_data(data)
    await message.answer('Done')
