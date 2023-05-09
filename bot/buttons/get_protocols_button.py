from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const


class GetProtocolsButton:
    button = Button(
        Const('Найти протокол'), 'get_protocol')
