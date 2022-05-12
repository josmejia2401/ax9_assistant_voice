#!/usr/bin/python3
from .engine.stt import STTEngine
from .engine.tts import TTSEngine
from .commads.index import IndexCommand
from .config.index import Config
import json

class Main:
    def __init__(self):
        super().__init__()
        Config.loadJson()
        print( json.dumps(Config.data.toJson))
        self.commands = IndexCommand()
        self.sttEngine = STTEngine()
        self.ttsEngine = TTSEngine()

    def init(self):
        try:
            while True:
                query = self.sttEngine.command()
                command = self.commands.command(query)
                self.ttsEngine.speak(command)
        except Exception as e:
            print(e)
        finally:
            self.ttsEngine.stop()
            self.sttEngine.stop()


if __name__ == '__main__':
    main = Main()
    main.init()
