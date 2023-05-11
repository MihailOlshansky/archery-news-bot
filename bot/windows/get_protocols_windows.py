from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const

from bot.stategroups import GetProtocolsSG
from bot.buttons import StopButton


gp_competition_window = Window(
    Const("Введи название соревнования"),
    StopButton.button,
    state=GetProtocolsSG.competition
)

gp_year_window = Window(
    Const("Введи год сореснования"),
    StopButton.button,
    state=GetProtocolsSG.year
)
