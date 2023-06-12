from fabrique import Operation, TypeOperation, Factory, command
from address_book import AddressBook

book = AddressBook()


class Search(Operation):
    def __init__(self, payload):
        super().__init__()
        self.payload = payload

    def operation(self):
        return book.search(self.payload)

    def info(self):
        return TypeOperation.SEARCH.value


class SearchFactory(Factory):
    def __init__(self, payload):
        self.payload = payload

    def create_operation(self) -> Operation:
        return Search(self.payload)


def search():
    payload = (input('Enter contact name: '))
    command(SearchFactory(payload))
