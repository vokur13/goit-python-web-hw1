from fabrique import Operation, TypeOperation, Factory, command
from address_book import book


class Exit(Operation):
    def __init__(self, payload):
        super().__init__()
        self.payload = payload

    def operation(self):
        print('Au revoir!')
        return book.save()

    def info(self):
        return TypeOperation.EXIT.value


class ExitFactory(Factory):
    def __init__(self, payload):
        self.payload = payload

    def create_operation(self) -> Operation:
        return Exit(self.payload)


def sortie():
    payload = ()
    command(ExitFactory(payload))
