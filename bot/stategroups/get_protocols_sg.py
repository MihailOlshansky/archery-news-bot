from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.stategroups.common import generate_state, StatesConstants


class GetProtocolsSG(StatesGroup):
    competition = State(generate_state(StatesConstants.GET, StatesConstants.PROTOCOL, StatesConstants.COMPETITION))
    year = State(generate_state(StatesConstants.GET, StatesConstants.PROTOCOL, StatesConstants.YEAR))
