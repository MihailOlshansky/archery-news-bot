from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const

from bot.stategroups import MainSG
from bot.buttons import StopButton

ap_start_window = Window(
    Const("Прикрепи протокол"),
    StopButton.button,
    state=MainSG.ap_start
)

ap_competition_window = Window(
    Const("Введи название соревнования"),
    StopButton.button,
    state=MainSG.ap_competition
)

ap_year_window = Window(
    Const("Введи год сореснования"),
    StopButton.button,
    state=MainSG.ap_year
)
