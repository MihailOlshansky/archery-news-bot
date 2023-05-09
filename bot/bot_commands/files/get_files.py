import re
import shutil
import time

from aiogram import types
from aiogram.types import File
from aiogram_dialog import DialogManager

from bot.common import send_wrong_file_request_format, bot
from database.database_commands import get_files_by_parameters
from database.tables import COMPETITION, COMPETITION_YEAR, FILE_FORMAT, FILE_ID, FILE_TYPE


async def get_files_command(message: types.Message, dialog_manager: DialogManager):
    params: dict[str, str] = await get_parameters_for_get_files(message)
    if params is None:
        return

    file_infos = get_files_by_parameters(params)
    await send_file_by_info(message, file_infos)


async def get_parameters_for_get_files(message: types.Message):
    params: list[str] = re.sub(r"^/get_protocols\s*", '', message.html_text).splitlines()
    params_dict = dict()
    for param in params:
        data = param.split(': ')
        if len(data) != 2:
            await send_wrong_file_request_format(message)
            return
        params_dict[data[0]] = data[1]

    keys = params_dict.keys()
    if 'Год' not in keys or 'Соревнование' not in keys:
        await send_wrong_file_request_format(message)
        return

    return params_dict


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
