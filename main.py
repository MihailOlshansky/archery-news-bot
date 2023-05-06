from aiogram.utils import executor

from bot.bot import dp
from database.database_commands import init_database


def main():
    init_database()
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
