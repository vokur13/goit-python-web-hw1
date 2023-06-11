from .record import Field
from collections import UserList


class Phone(Field, UserList):

    def __init__(self):
        super().__init__()
        self.value = input('Phone: ')

    def value_of(self):
        if self.value is not None:
            self.append(self.value)
        return self
