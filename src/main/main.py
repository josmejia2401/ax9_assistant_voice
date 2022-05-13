#!/usr/bin/python3
from .engine.stt import STTEngine
from .engine.tts import TTSEngine
from .brain.commads.index import IndexCommand
from .config.index import Config
from .brain.analyzer import Analyzer


class Main:
    def __init__(self):
        super().__init__()
        Config.loadJson()
        self.commands = IndexCommand()

    def init(self):
        try:
            while True:
                query = STTEngine.getInstance().command()
                query, _ = Analyzer.getInstance().extract(query)
                command = self.commands.command(query)
                TTSEngine.getInstance().speak(command)
        except Exception as e:
            print(e)
        finally:
            STTEngine.getInstance().stop()
            TTSEngine.getInstance().stop()


if __name__ == '__main__':
    main = Main()
    main.init()
