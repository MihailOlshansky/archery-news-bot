from aiogram_dialog import Dialog

from bot.windows import *

main_dialog = Dialog(
    main_window,

    # окна добавления протоколов
    ap_start_window,
    ap_competition_window,
    ap_year_window,

    # окна добавления положений
    ar_start_window,
    ar_competition_window,
    ar_year_window,

    # окна получения протоколов
    gp_competition_window,
    gp_year_window,

    # окна получения положений
    gr_competition_window,
    gr_year_window
)
