def generate_state(*kwargs):
    return '_'.join(kwargs) + 'state'


class StatesConstants:
    MAIN = 'main'

    ADD = 'add'
    GET = 'get'

    PROTOCOL = 'protocol'
    RULE = 'rule'

    START = 'start'
    COMPETITION = 'competition'
    YEAR = 'year'
