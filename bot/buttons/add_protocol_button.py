from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button

from bot.bot_commands import add_protocol_clicked


class AddProtocolButton:
    button = Button(
        Const('Добавить протокол'),
        'add_protocol',
        on_click=add_protocol_clicked
    )
