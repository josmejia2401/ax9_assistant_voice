#!/usr/bin/python3
import datetime


class StarttingCommand(object):
    pass

    def getCommand(self, query):
        if "hola" in query:
            hour = datetime.datetime.now().hour
            if hour >= 0 and hour < 12:
                return 'Hola, buenos días!'
            elif hour >= 12 and hour < 18:
                return 'Hola, buenas tardes!'
            else:
                return 'Hola, buenas noches!'
        return None
