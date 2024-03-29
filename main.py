import sys
from typing import NoReturn

from config import logger
from handler import BotStopped
from handler import run as run_handler


def main() -> NoReturn:
    logger.debug("START")
    while True:
        try:
            run_handler()
        except BotStopped:
            logger.error("BotStopped")
        except KeyboardInterrupt:
            logger.debug("KeyboardInterrupt")
            sys.exit(0)
        except Exception as e:
            logger.critical(
                f"Bot crashed for unknown reason: {e.__class__=} {e.args=}"
            )


if __name__ == "__main__":
    main()
