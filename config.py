from loguru import logger
from dotenv import dotenv_values as _dotenv


logger.add("./logs/debug.log", rotation="1 DAY")


def _get_env(key: str) -> str:
    value = _dotenv()[key]
    if not value:
        raise ValueError(f"{key} env var not set")
    return value


TOKEN = _get_env("TOKEN")
CHAT_ID = int(_get_env("CHATID"))
DB_URL = _get_env("DBURL")
