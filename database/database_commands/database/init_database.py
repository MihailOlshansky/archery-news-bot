from database.database_commands.common import execute_request
from database.tables.admin.fields import USER_ID, USER_NAME
from database.tables.admin.names import ARCHERY_ADMIN_TABLE
from database.tables.file.fields import ID, COMPETITION, COMPETITION_YEAR, FILE_ID, FILE_FORMAT, FILE_TYPE
from database.tables.file.names import ARCHERY_FILE_TABLE


def init_database():
    init_file_table()
    init_admin_table()


def init_file_table():
    cine_file_table_query = \
        f'CREATE TABLE IF NOT EXISTS {ARCHERY_FILE_TABLE}' \
        f'({ID} int AUTO_INCREMENT, ' \
        f'{COMPETITION} varchar(255) ,' \
        f'{COMPETITION_YEAR} int, ' \
        f'{FILE_ID} varchar(255), ' \
        f'{FILE_FORMAT} varchar(7), ' \
        f'{FILE_TYPE} varchar(31), ' \
        f'PRIMARY KEY ({ID}));'
    execute_request(cine_file_table_query, 'Initialization exception')


def init_admin_table():
    cine_admin_table_query = \
        f'CREATE TABLE IF NOT EXISTS {ARCHERY_ADMIN_TABLE}' \
        f'({USER_ID} varchar(255), ' \
        f'{USER_NAME} varchar(255), ' \
        f'PRIMARY KEY ({USER_ID}));'
    execute_request(cine_admin_table_query, 'Initialization exception')
