from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.stategroups import MainSG


async def stop_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    await manager.mark_closed()
    await manager.reset_stack()
    await manager.start(MainSG.start)

