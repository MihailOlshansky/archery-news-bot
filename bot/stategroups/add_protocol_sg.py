from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.stategroups.common import generate_state, StatesConstants


class AddProtocolSG(StatesGroup):
    start = State(generate_state(StatesConstants.ADD, StatesConstants.PROTOCOL, StatesConstants.START))
    competition = State(generate_state(StatesConstants.ADD, StatesConstants.PROTOCOL, StatesConstants.COMPETITION))
    year = State(generate_state(StatesConstants.ADD, StatesConstants.PROTOCOL, StatesConstants.YEAR))
