from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot.bot_commands.files.start_file_command import get_protocols_clicked


class GetProtocolsButton:
    button = Button(
        Const('Найти протокол'),
        'get_protocol',
        on_click=get_protocols_clicked
    )
