from typing import Dict

from aiogram import types, Bot
from aiogram.dispatcher.filters.state import State
from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.when import Whenable

from bot.stategroups import MainSG
from config import TG_TOKEN
from database import is_admin

bot = Bot(token=TG_TOKEN)


def get_file_type_by_state(state: State):
    group = state.group
    if MainSG.PROTOCOL in group:
        return 'Протокол'
    elif MainSG.RULE in group:
        return 'Положение'
    else:
        return 'Неизвестный_Тип'


async def send_wrong_file_info_format(message: types.Message):
    await message.answer('Неверный формат. Введите информацию о файле в виде:\n' +
                         'Название соревнования\n' +
                         'Год проведения соревнования'
                         )


async def send_wrong_file_request_format(message: types.Message):
    await message.answer('\n'.join([
        'Неверный формат. Введите информацию о файле в виде:',
        'Соревнование: <название соревнования>',
        'Год: <диапазон лет>',
        '========================================',
        'Пример:',
        'Соревнование: Русская зима',
        'Год: 2019-2021, 2023'
    ]))


def is_admin_command(data: Dict, widget: Whenable, dialog_manager: DialogManager):
    user_id = data['event'].from_user.id
    return is_admin(user_id)
