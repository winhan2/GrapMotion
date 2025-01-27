# coding: utf-8

from core.command import Cli
from lib.logger import Logger
from core.grap import Grap

DIVIDING_LEN = 100

def main():
    logger_obj = Logger()
    cli_obj = Cli(logger_obj, Grap())
    print('-' * DIVIDING_LEN)
    cli_obj.main()

