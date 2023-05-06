from aiogram.types import Message

from database.database_commands.common import execute_request, FETCH_ALL
from database.tables.admin.fields import USER_NAME
from database.tables.admin.names import ARCHERY_ADMIN_TABLE


def is_admin(username: str):
    count_admins_sql = f'SELECT COUNT(*) FROM {ARCHERY_ADMIN_TABLE} WHERE {USER_NAME} = {username}'
    count_admins = execute_request(count_admins_sql, "Admin check error", mode=FETCH_ALL)
    return count_admins != 0

