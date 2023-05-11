"""
Данная функция отвечает за обработку команды /add_protocol
Она позволяет сохранить протокол в бд
"""
from aiogram import types
from aiogram_dialog import DialogManager

from bot.bot_commands.common import get_from_dm
from bot.common import get_file_type_by_state, user_req_data
from database import is_admin
from database.tables import FILE_TYPE
from database.tables.file import COMPETITION, COMPETITION_YEAR, FILE_ID, FILE_FORMAT
from database.database_commands import insert_file_data


async def add_file_command(message: types.Message, manager: DialogManager):
    if not is_admin(message.from_user.username):
        return

    (user, chat) = get_from_dm(manager)
    file_data = user_req_data[chat][user]

    params = {
        FILE_ID: file_data[FILE_ID],
        FILE_FORMAT: file_data[FILE_FORMAT],
        FILE_TYPE: file_data[FILE_TYPE],
        COMPETITION: file_data[COMPETITION],
        COMPETITION_YEAR: file_data[COMPETITION_YEAR]
    }

    insert_file_data(params)
    await message.answer(f'{file_data[FILE_TYPE]} добавлен')
