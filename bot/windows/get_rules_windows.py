from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const

from bot.stategroups import MainSG
from bot.buttons import StopButton


gr_competition_window = Window(
    Const("Введи название соревнования"),
    StopButton.button,
    state=MainSG.gr_competition
)

gr_year_window = Window(
    Const("Введи год сореснования"),
    StopButton.button,
    state=MainSG.gr_year
)
