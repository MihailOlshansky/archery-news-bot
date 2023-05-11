from aiogram_dialog import Dialog

from bot.windows import gr_competition_window, gr_year_window

get_rules_dialog = Dialog(
    gr_competition_window,
    gr_year_window
)
