#Python
import logging 
from logging.config import dictConfig

#Aiogram
from aiogram import Bot, Dispatcher
#Third - Party
from dotenv import dotenv_values


config: dict  = dotenv_values()
BOT_TOKEN: str = config.get("BOT_TOKEN")
API_URL: str = config.get("API_URL")
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()
VOLUME = "./volume/"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "detailed",
        },
    },
    "formatters": {
        "detailed": {
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
} 
dictConfig(LOGGING)
logger = logging.getLogger(__name__)
