import logging
import logging.config

from basetypes.Broker.tdaBroker import TdaBroker
from basetypes.Database.sqliteDatabase import SqliteDatabase
from basetypes.Mediator.botMediator import Bot
from basetypes.Notifier.telegramnotifier import TelegramNotifier
from basetypes.Strategy.cspByDeltaStrategy import CspByDeltaStrategy

if __name__ == "__main__":
    # Create Logging
    logging.config.fileConfig(
        "logConfig.ini",
        defaults={"logfilename": "autotrader.log"},
        disable_existing_loggers=False,
    )

    # Create our strategies
    cspstrat = CspByDeltaStrategy(
        strategy_name="CSP1", underlying="XSP", portfolioallocationpercent=0.75
    )

    # Create our broker
    tdabroker = TdaBroker()

    # Create our local DB
    sqlitedb = SqliteDatabase("./pers/LoopTrader.db")

    # Create our notifier
    telegram_bot = TelegramNotifier()

    # Create our Bot
    bot = Bot(
        broker=tdabroker,
        strategies=[cspstrat],
        database=sqlitedb,
        notifier=telegram_bot,
    )

    # Run Bot
    bot.process_strategies()


# main()
