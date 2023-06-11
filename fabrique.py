from abc import abstractmethod, ABC
from enum import Enum


class TypeOperation(str, Enum):
    ADD = 'add'
    SEARCH = 'search'
    EDIT = 'edit'
    REMOVE = 'remove'
    SAVE = 'save'
    LOAD = 'load'
    CONGRATULATE = 'congratulate'
    VIEW = 'view'
    EXIT = 'exit'


class Operation(ABC):

    def __init__(self):
        self.payload = None

    @abstractmethod
    def operation(self):
        ...

    @abstractmethod
    def info(self):
        ...


class Factory(ABC):
    @abstractmethod
    def create_operation(self) -> Operation:
        ...

    def make_operation(self) -> Operation:
        return self.create_operation()


def command(factory: Factory):
    operator = factory.make_operation()
    result = operator.operation()
    return result, operator.info(), operator.payload
