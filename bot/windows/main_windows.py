from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.text import Const

from bot.common import is_admin_command
from bot.stategroups import MainSG
from bot.buttons import GetProtocolsButton, GetRulesButton, AddRuleButton, AddProtocolButton


main_window = Window(
    Const("Привет!\nЗдесь ты сможешь найти протоколы и положения с различных соревнований"),
    Row(
        GetProtocolsButton.button,
        GetRulesButton.button
    ),
    Row(
        AddProtocolButton.button,
        AddRuleButton.button,
        when=is_admin_command
    ),
    state=MainSG.main_start
)
