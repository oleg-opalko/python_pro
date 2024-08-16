import datetime
import logging


class LoggingMixin:
    def __init__(self):
        self.logger = logging.getLogger(f'{type(self).__name__}')
        self.logger.setLevel(logging.DEBUG)

        c_handler = logging.StreamHandler()
        time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        log_format = f'[{time}] - %(message)s'

        c_format = logging.Formatter(log_format)

        c_handler.setFormatter(c_format)
        self.logger.addHandler(c_handler)

    def log(self, message: str):
        self.logger.debug(message)
