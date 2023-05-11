from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot.bot_commands.files.start_file_command import get_rules_clicked


class GetRulesButton:
    button = Button(
        Const('Найти положение'),
        'get_rule',
        on_click=get_rules_clicked
    )
