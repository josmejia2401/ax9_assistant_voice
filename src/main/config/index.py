#!/usr/bin/python3
from .dto import ConfigDTO
from ..utils.filex import File


class Config(object):
    data = dict()

    @staticmethod
    def loadJson(dir_file=None):
        if dir_file:
            config_json = File.loadFileFromResourcesAsJson('config.json', dir_file)
        else:
            config_json = File.loadFileFromResourcesAsJson('config.json')
        Config.data = ConfigDTO(config_json)
        return Config.data

    @staticmethod
    def getConfig() -> ConfigDTO:
        return Config.data

    @staticmethod
    def setConfig(config) -> ConfigDTO:
        File.saveJson(config, 'config.json')
        return Config.data