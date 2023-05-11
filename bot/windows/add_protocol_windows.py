from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const

from bot.stategroups import AddProtocolSG
from bot.buttons import StopButton

ap_start_window = Window(
    Const("Прикрепи протокол"),
    StopButton.button,
    state=AddProtocolSG.start
)

ap_competition_window = Window(
    Const("Введи название соревнования"),
    StopButton.button,
    state=AddProtocolSG.competition
)

ap_year_window = Window(
    Const("Введи год сореснования"),
    StopButton.button,
    state=AddProtocolSG.year
)
