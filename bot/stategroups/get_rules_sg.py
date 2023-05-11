from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.stategroups.common import generate_state, StatesConstants


class GetRulesSG(StatesGroup):
    competition = State(generate_state(StatesConstants.GET, StatesConstants.RULE, StatesConstants.COMPETITION))
    year = State(generate_state(StatesConstants.GET, StatesConstants.RULE, StatesConstants.YEAR))
