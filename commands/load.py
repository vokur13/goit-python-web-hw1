from fabrique import Operation, TypeOperation, Factory, command
from address_book import book


class Load(Operation):
    def __init__(self, payload):
        super().__init__()
        self.payload = payload

    def operation(self):
        return book.load()

    def info(self):
        return TypeOperation.LOAD.value


class LoadFactory(Factory):
    def __init__(self, payload):
        self.payload = payload

    def create_operation(self) -> Operation:
        return Load(self.payload)


def load():
    payload = ()
    command(LoadFactory(payload))
