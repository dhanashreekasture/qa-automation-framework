import logging


class Logger:

    logging.basicConfig(
        filename="reports/test.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    @staticmethod
    def info(msg):
        logging.info(msg)

    @staticmethod
    def error(msg):
        logging.error(msg)