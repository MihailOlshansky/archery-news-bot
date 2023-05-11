import shutil
import time

from aiogram import types
from aiogram.types import File
from aiogram_dialog import DialogManager

from bot.bot_commands.common import get_from_dm
from bot.common import bot, user_req_data
from database.database_commands import get_files_by_parameters
from database.tables import COMPETITION, COMPETITION_YEAR, FILE_FORMAT, FILE_ID, FILE_TYPE


async def get_files_command(message: types.Message, manager: DialogManager):
    (user, chat) = get_from_dm(manager)
    file_data = user_req_data[chat][user]

    params = {
        COMPETITION: file_data[COMPETITION],
        COMPETITION_YEAR: file_data[COMPETITION_YEAR]
    }

    file_infos = get_files_by_parameters(params)
    if len(file_infos) != 0:
        await send_file_by_info(message, file_infos)


async def send_file_by_info(message: types.Message, file_infos: list[dict[str, str]]):
    directory = f"local\\{message.from_user.id}_{time.time()}"
    media = types.MediaGroup()

    for file_info in file_infos:
        file_id = file_info[FILE_ID]
        filename = f"{file_info[COMPETITION]}_" \
                   f"{file_info[COMPETITION_YEAR]}_" \
                   f"{file_info[FILE_TYPE]}." \
                   f"{file_info[FILE_FORMAT]}"

        filepath = f"{directory}\\{filename}"

        file: File = await bot.get_file(file_id)
        await file.download(destination_file=filepath)
        media.attach_document(types.InputFile(filepath))

    await message.answer_media_group(media)
    shutil.rmtree(directory)
