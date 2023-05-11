from database.tables.file import COMPETITION_YEAR, COMPETITION, FILE_ID, FILE_FORMAT, FILE_TYPE
from database.database_commands.common import execute_request
from database.tables.file.names import ARCHERY_FILE_TABLE


def get_files_by_parameters(params: dict[str, str]):
    get_protocols_sql =\
        f"SELECT {FILE_ID}, {COMPETITION}, {COMPETITION_YEAR}, {FILE_FORMAT}, {FILE_TYPE} " \
        f"FROM {ARCHERY_FILE_TABLE} " \
        f"WHERE LOWER({COMPETITION}) LIKE '%{params[COMPETITION].lower()}%' "

    conditions = list()
    for dates in params[COMPETITION_YEAR].split(', '):
        dates_range = dates.split('-')
        date_start = dates_range[0]
        date_end = int(dates_range[-1]) + 1
        conditions.append(f"{COMPETITION_YEAR} BETWEEN {date_start} AND {date_end}")

    if len(conditions) != 0:
        get_protocols_sql += "AND (" + " OR ".join(conditions) + ")"

    return execute_request(get_protocols_sql, "Get protocols exception", mode='fetchall')
