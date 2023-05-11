from aiogram_dialog import Dialog

from bot.windows import ap_start_window, ap_competition_window, ap_year_window

add_protocol_dialog = Dialog(
    ap_start_window,
    ap_competition_window,
    ap_year_window
)
