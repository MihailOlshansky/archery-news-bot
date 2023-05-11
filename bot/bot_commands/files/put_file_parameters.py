from aiogram.types import Message
from aiogram_dialog import DialogManager

from bot.bot_commands.common import get_from_dm, get_state
from bot.common import user_req_data, get_file_type_by_state
from database.tables import FILE_ID, FILE_FORMAT, COMPETITION, FILE_TYPE, COMPETITION_YEAR


def put_file_info(message: Message, manager: DialogManager):
    file_id: str = message.document.file_id
    file_format = message.document.file_name.split('.')[-1]

    (user, chat) = get_from_dm(manager)

    user_req_data[chat][user][FILE_ID] = file_id
    user_req_data[chat][user][FILE_FORMAT] = file_format
    user_req_data[chat][user][FILE_TYPE] = get_file_type_by_state(get_state(manager))


def put_competition(message: Message, manager: DialogManager):
    competition = message.html_text
    (user, chat) = get_from_dm(manager)
    user_req_data[chat][user][COMPETITION] = competition


def put_year(message: Message, manager: DialogManager):
    year = message.html_text
    (user, chat) = get_from_dm(manager)
    user_req_data[chat][user][COMPETITION_YEAR] = year
