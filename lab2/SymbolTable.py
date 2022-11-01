from HashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.__size = size
        self.__table = HashTable(size)

    def add(self, identifier, value):
        return self.__table.add(identifier, value)

    def delete(self, identifier):
        return self.__table.delete(identifier)

    def getValueForIdentifier(self, identifier):
        return self.__table[identifier]

    def __str__(self):
        return self.__table.__str__()
