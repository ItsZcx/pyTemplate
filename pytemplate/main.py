import sys

from config import config
from config import logger
from modules.xmodule.module import hello


def main() -> int:
    hello()
    logger.info("Hello from logs. Using stream as well as .log file")
    return 0


if __name__ == "__main__":
    sys.exit(main())
