from database.database_commands.common import to_tuple_string, execute_request
from database.tables.file.names import ARCHERY_FILE_TABLE


def insert_file_data(data: dict):
    insert_data_sql = \
        f"INSERT INTO {ARCHERY_FILE_TABLE} {to_tuple_string(data.keys(), True)} " \
        f"VALUES {to_tuple_string(data.values())};"

    execute_request(insert_data_sql, 'Data insertion exception')
