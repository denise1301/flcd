from HashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.__size = size
        self.__table = HashTable(size)

    def add(self, identifier):
        return self.__table.add(identifier)

    def contains(self, key):
        return self.__table.get(key)

    def delete(self, key):
        return self.__table.delete(key)

    def __str__(self):
        return "Symbol Table:\n" + str(self.__table)
