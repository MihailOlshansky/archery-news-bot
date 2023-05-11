from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const

from bot.stategroups import AddRuleSG
from bot.buttons import StopButton

ar_start_window = Window(
    Const("Прикрепи положение"),
    StopButton.button,
    state=AddRuleSG.start
)

ar_competition_window = Window(
    Const("Введи название соревнования"),
    StopButton.button,
    state=AddRuleSG.competition
)

ar_year_window = Window(
    Const("Введи год сореснования"),
    StopButton.button,
    state=AddRuleSG.year
)
