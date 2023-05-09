from database.database_commands.common import execute_request
from database.tables.admin import *
from database.tables.file import *
from database.tables.storage import *


def init_database(mode: str = 'in_memory'):
    init_file_table()
    init_admin_table()

    if mode == 'database':
        init_state_storage_table()
        init_data_storage_table()


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
    execute_request(cine_file_table_query, 'Initializing file table exception')


def init_admin_table():
    cine_admin_table_query = \
        f'CREATE TABLE IF NOT EXISTS {ARCHERY_ADMIN_TABLE}' \
        f'({USER_ID} varchar(255), ' \
        f'{USER_NAME} varchar(255), ' \
        f'PRIMARY KEY ({USER_ID}));'
    execute_request(cine_admin_table_query, 'Initializing admin table exception')


def init_state_storage_table():
    cine_state_storage_table_query = \
        f'CREATE TABLE IF NOT EXISTS {ARCHERY_STATE_STORAGE}' \
        f'({KEY} varchar(255), ' \
        f'{STATE} varchar(255), ' \
        f'PRIMARY KEY ({KEY}));'
    execute_request(cine_state_storage_table_query, 'Initializing state storage table exception')


def init_data_storage_table():
    cine_data_storage_table_query = \
        f'CREATE TABLE IF NOT EXISTS {ARCHERY_DATA_STORAGE}' \
        f'({KEY} varchar(255), ' \
        f'{DATA} text, ' \
        f'PRIMARY KEY ({KEY}));'
    execute_request(cine_data_storage_table_query, 'Initializing data storage table exception')
