from abc import abstractmethod, ABC
from collections import UserList
from pathlib import Path
import pickle


class AbsBook(ABC):
    @abstractmethod
    def add(self, value):
        ...

    @abstractmethod
    def search(self, key):
        ...

    @abstractmethod
    def save(self):
        ...

    @abstractmethod
    def load(self):
        ...

    @abstractmethod
    def value_of(self):
        ...


class AddressBook(AbsBook, UserList):
    def __init__(self):
        super().__init__()
        self.path = 'book.bin'

    def add(self, value):
        self.append(value)
        print('New entry added to the book')

    def search(self, key):
        print([i for i in self if i['name'] == key])

    def save(self):
        path = Path(self.path)
        contents = pickle.dumps(self.data)
        path.write_bytes(contents)

    def load(self):
        path = Path(self.path)
        if path.exists():
            contents = path.read_bytes()
            self.data = pickle.loads(contents)
            print('Address Book records are available to operate with.')
        else:
            print('No data to recover')

    def value_of(self):
        return self


book = AddressBook()
