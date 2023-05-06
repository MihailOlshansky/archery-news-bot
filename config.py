import os
import dotenv

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(env_path)

# получение переменных из .env файла
# токен бота
TG_TOKEN: str = os.getenv("TG_TOKEN")

# параметры БД (MySql)
DB_PORT: int = int(os.getenv("DB_PORT"))
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

