# obtiene el tipo de comando, y basado en ese tipo, se llama al correspondiente
from .datex import DateCommand
from .setup import SetUpCommand


class IndexCommand(object):
    def __init__(self):
        super().__init__()
        self.dateCommand = DateCommand()
        self.setupCommand = SetUpCommand()

    def command(self, query):
        if not query:
            return
        command = self.dateCommand.command(query)
        if not command:
            command = self.setupCommand.command(query)
        return command
