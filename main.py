#Third-Party
import asyncio

#Local
from src.settings.base import bot, dp , logger
from src.bot.routers import ROUTERS
from src.bot.utils.rate_exchange import get_exchange_rate

async def main():
    dp.include_routers(*ROUTERS)
    logger.info(msg="Bot started!")
    # await asyncio.gather(
    #     get_exchange_rate(currency="KZT"),
    #     get_exchange_rate(currency="RUB"),
    #     get_exchange_rate(currency = "USD")
    # )
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main=main())
