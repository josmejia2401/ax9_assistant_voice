#!/usr/bin/python3
import random
from ...regex.index import ReEval
from ...engine.tts import TTSEngine
from ...engine.stt import STTEngine
from .keyword import no_listen
from ...config.index import Config

class SetUpCommand(object):
    def __init__(self):
        super().__init__()

    def command(self, query):
        command = self._changeNameCommand(query)
        return command

    def _changeNameCommand(self, query):
        allowed = ["^.*(cambiar nombre)+.*$", "^.*(cambiar mi nombre)+.*$", "^.*(establecer nombre)+.*$", "^.*(cambiar dueño)+.*$", "^.*(cambiar mi dueño)+.*$", "^.*(establecer dueño)+.*$"]
        for pattern in allowed:
            result = ReEval.eval(pattern, query)
            if result:
                TTSEngine.getInstance().speak("¿Cuál es tú nombre o cómo deseas que te llame?")
                command = None
                cont = 0
                while command is None:
                    command = STTEngine.getInstance().command()
                    if command:
                        break
                    if cont < 5:
                        TTSEngine.getInstance().speak(random.choice(no_listen))
                    else:
                        break
                    cont = cont + 1
                if command:
                    #(.*) representa el nombre - grupo(1)
                    name_allowed = ["(.*) es mi nombre.*", "soy (.*)", "me llamo (.*)", "llamame (.*)", ".* llamar (.*)"]
                    for name in name_allowed:
                        m = ReEval.match(name, command)
                        if m and m.group(1):
                            command = m.group(1)
                            break
                    config = Config.getConfig()
                    config.userInfo.name = command
                    Config.setConfig(config.toJson)
                    return f'Te he cambiado el nombre a: {command}'
                else:
                    return 'Lo intenté, pero no logré entender. Intenta más luego cambiar el nombre.'
        return None
