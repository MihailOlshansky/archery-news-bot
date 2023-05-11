from aiogram_dialog import Dialog

from bot.windows import gp_competition_window, gp_year_window

get_protocols_dialog = Dialog(
    gp_competition_window,
    gp_year_window
)
