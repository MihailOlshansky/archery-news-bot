import re

from database.database import get_connection


FETCH_ALL = "fetchall"
COMMIT = "commit"


def to_tuple_string(data: iter, remove_quotes: bool = False):
    result = str(tuple(data))
    return re.sub("[\'\"]", "", result) if remove_quotes else result


def execute_request(req: str, error_message: str, mode: str = COMMIT):
    connection = get_connection()
    if connection is None:
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute(req)
            if mode == COMMIT:
                connection.commit()
            elif mode == FETCH_ALL:
                rows = cursor.fetchall()
                return rows
    except Exception as e:
        print(error_message)
        print(e)
        print('#' * 30)
    finally:
        connection.close()
