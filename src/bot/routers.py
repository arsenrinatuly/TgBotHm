#Local
from src.bot.handlers.master import master_router
from src.bot.handlers.exchange import exchange_router   
from src.bot.handlers.history_exchanges import history_exchanges_router

ROUTERS = [
    master_router,
    exchange_router,
    history_exchanges_router
]
