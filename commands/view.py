from fabrique import Operation, TypeOperation, Factory, command
from address_book import book
from adapter import pretty_view


class View(Operation):
    def __init__(self, payload):
        super().__init__()
        self.payload = payload

    def operation(self):
        return pretty_view(book.value_of())

    def info(self):
        return TypeOperation.VIEW.value


class ViewFactory(Factory):
    def __init__(self, payload):
        self.payload = payload

    def create_operation(self) -> Operation:
        return View(self.payload)


def view():
    payload = ()
    command(ViewFactory(payload))


