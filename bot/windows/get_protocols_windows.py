from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const

from bot.stategroups import MainSG
from bot.buttons import StopButton


gp_competition_window = Window(
    Const("Введи название соревнования"),
    StopButton.button,
    state=MainSG.gp_competition
)

gp_year_window = Window(
    Const("Введи год сореснования"),
    StopButton.button,
    state=MainSG.gp_year
)
