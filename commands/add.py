from fabrique import Operation, TypeOperation, Factory, command
from address_book import book
from fields import *


class Add(Operation):
    def __init__(self, payload):
        super().__init__()
        self.payload = payload

    def operation(self):
        return book.add(self.payload)

    def info(self):
        return TypeOperation.ADD.value


class AddFactory(Factory):
    def __init__(self, payload):
        self.payload = payload

    def create_operation(self) -> Operation:
        return Add(self.payload)


def add():
    payload = (Record(Name(), Phone(), Email()))
    command(AddFactory(payload))
