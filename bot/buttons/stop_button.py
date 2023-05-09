from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot.bot_commands import stop_clicked


class StopButton:
    button = Button(Const('В начало'), 'stop', on_click=stop_clicked)
