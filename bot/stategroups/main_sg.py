from aiogram.dispatcher.filters.state import StatesGroup, State


def generate_state(*kwargs):
    return '_'.join(kwargs) + 'state'


class MainSG(StatesGroup):
    MAIN = 'main'

    ADD = 'add'
    GET = 'get'

    PROTOCOL = 'protocol'
    RULE = 'rule'

    START = 'start'
    COMPETITION = 'competition'
    YEAR = 'year'

    main_start = State(generate_state(MAIN, START))

    ap_start = State(generate_state(ADD, PROTOCOL, START))
    ap_competition = State(generate_state(ADD, PROTOCOL, COMPETITION))
    ap_year = State(generate_state(ADD, PROTOCOL, YEAR))

    ar_start = State(generate_state(ADD, RULE, START))
    ar_competition = State(generate_state(ADD, RULE, COMPETITION))
    ar_year = State(generate_state(ADD, RULE, YEAR))

    gp_competition = State(generate_state(GET, PROTOCOL, COMPETITION))
    gp_year = State(generate_state(GET, PROTOCOL, YEAR))

    gr_competition = State(generate_state(GET, RULE, COMPETITION))
    gr_year = State(generate_state(GET, RULE, YEAR))
