from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.stategroups.common import generate_state, StatesConstants


class AddRuleSG(StatesGroup):
    start = State(generate_state(StatesConstants.ADD, StatesConstants.RULE, StatesConstants.START))
    competition = State(generate_state(StatesConstants.ADD, StatesConstants.RULE, StatesConstants.COMPETITION))
    year = State(generate_state(StatesConstants.ADD, StatesConstants.RULE, StatesConstants.YEAR))
