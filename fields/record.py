from abc import abstractmethod, ABC
from collections import UserList, UserDict


class AbsRecord(ABC, UserDict):

    @abstractmethod
    def set_record(self, key, value):
        ...

    @abstractmethod
    def get_record(self, key):
        ...

    @abstractmethod
    def value_of(self):
        ...


class Field(ABC):

    @abstractmethod
    def value_of(self):
        ...


class Record(AbsRecord):

    def __init__(self, name: Field, phone: (Field, UserList), email: (Field, UserList)):
        super().__init__()
        self.data = {
            'name': name.value_of(),
            'phone': phone.value_of(),
            'email': email.value_of()
        }

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __getitem__(self, key):
        return self.data[key]

    def set_record(self, key, value):
        self.__setitem__(key, value)

    def get_record(self, key):
        return self.__getitem__(key)

    def value_of(self):
        return self
