from .record import Field


class Name(Field):

    def __init__(self):
        self.value = input('Name: ')

    def value_of(self):
        return self.value
