# coding: utf-8
# config

import configparser
config = configparser.ConfigParser()

class Config:
    def __init__(self, route):
        self.route = route

    def read(self, section, option) -> str:
        config.read(self.route, encoding='utf-8')
        config_res = config.get(section, option)
        return config_res

    def set(self, section, option, value):
        config.read(self.route, encoding='utf-8')
        config.set(section, option, value)
        config.write(open(self.route, mode='w'))
