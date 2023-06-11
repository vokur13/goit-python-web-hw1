from .record import Field
from collections import UserList


class Email(Field, UserList):

    def __init__(self):
        super().__init__()
        self.value = input('Email: ')

    def value_of(self):
        if self.value is not None:
            self.append(self.value)
        return self
