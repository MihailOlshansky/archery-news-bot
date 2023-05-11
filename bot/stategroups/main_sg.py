from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.stategroups.common import generate_state, StatesConstants


class MainSG(StatesGroup):
    start = State(generate_state(StatesConstants.MAIN, StatesConstants.START))
