from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.stategroups import MainSG


async def add_protocol_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    await manager.dialog().switch_to(MainSG.ap_start)


async def add_rule_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    await manager.dialog().switch_to(MainSG.ar_start)
