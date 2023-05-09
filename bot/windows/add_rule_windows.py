from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const

from bot.stategroups import MainSG
from bot.buttons import StopButton

ar_start_window = Window(
    Const("Прикрепи положение"),
    StopButton.button,
    state=MainSG.ar_start
)

ar_competition_window = Window(
    Const("Введи название соревнования"),
    StopButton.button,
    state=MainSG.ar_competition
)

ar_year_window = Window(
    Const("Введи год сореснования"),
    StopButton.button,
    state=MainSG.ar_year
)
