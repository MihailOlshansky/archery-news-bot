from typing import Dict

from aiogram import types, Bot
from aiogram.dispatcher.filters.state import State
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.when import Whenable

from bot.stategroups import AddProtocolSG, AddRuleSG, GetProtocolsSG, GetRulesSG, MainSG
from bot.stategroups.common import StatesConstants
from config import TG_TOKEN
from database import is_admin

bot = Bot(token=TG_TOKEN)
user_req_data = dict()


def get_file_type_by_state(state: State) -> str:
    state_name = state.state
    if StatesConstants.PROTOCOL in state_name:
        return 'Протокол'
    elif StatesConstants.RULE in state_name:
        return 'Положение'
    else:
        return 'Неизвестный_Тип'


def get_year_state(state: State) -> State:
    state_name = state.state
    if StatesConstants.ADD in state_name:
        if StatesConstants.PROTOCOL in state_name:
            return AddProtocolSG.year
        elif StatesConstants.RULE in state_name:
            return AddRuleSG.year
    elif StatesConstants.GET in state_name:
        if StatesConstants.PROTOCOL in state_name:
            return GetProtocolsSG.year
        elif StatesConstants.RULE in state_name:
            return GetRulesSG.year


def get_competition_state(state: State) -> State:
    state_name = state.state
    if StatesConstants.ADD in state_name:
        if StatesConstants.PROTOCOL in state_name:
            return AddProtocolSG.competition
        elif StatesConstants.RULE in state_name:
            return AddRuleSG.competition
    elif StatesConstants.GET in state_name:
        if StatesConstants.PROTOCOL in state_name:
            return GetProtocolsSG.competition
        elif StatesConstants.RULE in state_name:
            return GetRulesSG.competition


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


def is_admin_command(data: Dict, widget: Whenable, dialog_manager: DialogManager) -> bool:
    user_id = data['event'].from_user.id
    return is_admin(user_id)
