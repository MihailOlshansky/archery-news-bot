from aiogram_dialog import Dialog

from bot.windows import ar_start_window, ar_competition_window, ar_year_window

add_rule_dialog = Dialog(
    ar_start_window,
    ar_competition_window,
    ar_year_window
)
