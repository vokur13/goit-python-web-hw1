from abc import abstractmethod, ABC
from commands import *


class Starter(ABC):

    def __init__(self):
        self.COMMANDS = {
            'add': add,
            'search': search,
            # 'edit': edit,
            # 'remove':remove,
            'save': save,
            'load': load,
            # 'congratulate':congratulate,
            'view': view,
            'exit': sortie
        }

    @abstractmethod
    def starter(self):
        ...

    @abstractmethod
    def command_handler(self, action_type):
        ...

    @abstractmethod
    def command_yield(self):
        ...


class Commander(Starter):

    def starter(self):
        while True:
            com = input('Enter command: ').casefold().strip()
            if com in ['add', 'view', 'save', 'load', 'search']:
                yield com
            elif com in ['exit']:
                yield com
                break
            else:
                break

    def command_handler(self, action_type):
        return self.COMMANDS[action_type]

    def command_yield(self):
        for command in self.starter():
            self.command_handler(command)()
