from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button

from bot.bot_commands import add_rule_clicked


class AddRuleButton:
    button = Button(
        Const('Добавить положение'),
        'add_rule',
        on_click=add_rule_clicked
    )


