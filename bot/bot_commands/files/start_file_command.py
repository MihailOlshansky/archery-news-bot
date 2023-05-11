from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from bot.bot_commands.common import get_from_dm, STATE
from bot.common import user_req_data
from bot.stategroups import AddRuleSG, AddProtocolSG, GetRulesSG, GetProtocolsSG, generate_state, StatesConstants


async def add_protocol_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    user, chat = get_from_dm(manager, need_to_create=True)
    user_req_data[chat][user][STATE] = AddProtocolSG.start

    await manager.mark_closed()
    await manager.start(AddProtocolSG.start, mode=StartMode.RESET_STACK)


async def add_rule_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    user, chat = get_from_dm(manager, need_to_create=True)
    user_req_data[chat][user][STATE] = AddRuleSG.start

    await manager.mark_closed()
    await manager.start(AddRuleSG.start, mode=StartMode.RESET_STACK)


async def get_protocols_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    user, chat = get_from_dm(manager, need_to_create=True)
    user_req_data[chat][user][STATE] = GetProtocolsSG.competition

    await manager.mark_closed()
    await manager.start(GetProtocolsSG.competition, mode=StartMode.RESET_STACK)


async def get_rules_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    user, chat = get_from_dm(manager, need_to_create=True)
    user_req_data[chat][user][STATE] = GetRulesSG.competition

    await manager.mark_closed()
    await manager.start(GetRulesSG.competition, mode=StartMode.RESET_STACK)
