#!/usr/bin/python3
import datetime
from ..regex.index import ReEval
from ..config.index import Config

class DateCommand(object):
    def __init__(self):
        super().__init__()
        self.reval = ReEval()

    def command(self, query):
        command = self._hourCommand(query)
        return command

    def _hourCommand(self, query):
        allowed = ["^.*(que hora es)+.*$", "^.*(hora es)+.*$", "^.*(que hora son)+.*$", "^.*(hora son)+.*$", "^.*(hora actual)+.*$"]
        for pattern in allowed:
            result = self.reval.eval(pattern, query)
            if result:
                strtime = datetime.datetime.now().strftime('%H:%M:%S')
                return f'Señor {Config.getConfig().userInfo.name}, la hora actual es {strtime}'
        return None
