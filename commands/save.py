from fabrique import Operation, TypeOperation, Factory, command
from address_book import AddressBook

book = AddressBook()


class Save(Operation):
    def __init__(self, payload):
        super().__init__()
        self.payload = payload

    def operation(self):
        print('Saving...')
        return book.save()

    def info(self):
        return TypeOperation.SAVE.value


class SaveFactory(Factory):
    def __init__(self, payload):
        self.payload = payload

    def create_operation(self) -> Operation:
        return Save(self.payload)


def save():
    payload = ()
    command(SaveFactory(payload))
