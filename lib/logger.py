# coding: utf-8

import logging.config
from conf.settings import LOGGING_DIC

logging.config.dictConfig(LOGGING_DIC)

class Logger:
    def __init__(self, mode='2'):
        if mode == '1':
            self.mode = logging.getLogger('output_info_shell')
        elif mode == '2':
            self.mode = logging.getLogger('output_shell_and_file')
        else:
            self.mode = logging.getLogger('debug')

    def debug(self, msg):
        self.mode.debug(msg)

    def info(self, msg):
        self.mode.info(msg)

    def warning(self, msg):
        self.mode.warning(msg)

    def error(self, msg):
        self.mode.error(msg)

    def critical(self, msg):
        self.mode.critical(msg)


if __name__ == '__main__':
    logger_obj = Logger('1')
    logger_obj.info('Hello World!')

