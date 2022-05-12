#!/usr/bin/python3
import random
from ..regex.index import ReEval
from ..engine.tts import TTSEngine
from ..engine.stt import STTEngine
from .keyword import no_listen
from ..config.index import Config

class SetUpCommand(object):
    def __init__(self):
        super().__init__()
        self.reval = ReEval()
        self.ttsEngine = TTSEngine()
        self.sttEngine = STTEngine()

    def command(self, query):
        command = self._changeNameCommand(query)
        return command

    def _changeNameCommand(self, query):
        allowed = ["^.*(cambiar nombre)+.*$", "^.*(cambiar mi nombre)+.*$", "^.*(establecer nombre)+.*$", "^.*(cambiar dueño)+.*$", "^.*(cambiar mi dueño)+.*$", "^.*(establecer dueño)+.*$"]
        for pattern in allowed:
            result = self.reval.eval(pattern, query)
            if result:
                self.ttsEngine.speak("¿Cuál es tú nombre o cómo deseas que te llame?")
                command = None
                cont = 0
                while command is None:
                    command = self.sttEngine.command()
                    if command:
                        break
                    if cont < 5:
                        self.ttsEngine.speak(random.choice(no_listen))
                    else:
                        break
                    cont = cont + 1
                if command:
                    config = Config.getConfig()
                    config.userInfo.name = command
                    Config.setConfig(config.toJson)
                    return f'Te he cambiado el nombre a: {command}'
                else:
                    return 'Lo intenté, pero no logré entender. Intenta más luego cambiar el nombre.'
        return None
