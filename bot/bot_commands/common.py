from aiogram.dispatcher.filters.state import State
from aiogram_dialog import DialogManager

from bot.common import user_req_data


STATE = 'state'


def get_from_dm(manager: DialogManager, need_to_create: bool = False) -> (str, str):
    context = manager.data[STATE]
    (user, chat) = (context.user, context.chat)
    if need_to_create:
        if chat not in user_req_data.keys():
            user_req_data[chat] = dict()
        if user not in user_req_data[chat].keys():
            user_req_data[chat][user] = dict()

    return user, chat


def put_state(manager: DialogManager, state: State = None):
    user, chat = get_from_dm(manager)
    if state is None:
        del user_req_data[chat][user]
    else:
        user_req_data[chat][user][STATE] = state


def get_state(manager: DialogManager) -> State:
    user, chat = get_from_dm(manager)
    return user_req_data[chat][user][STATE]
