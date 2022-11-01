class HashTable:
    def __init__(self, size):
        self.array = [None] * size

    def hash(self, key):
        # sum of the key's characters ASCII codes % the length of the table
        return sum(ord(c) for c in str(key)) % len(self.array)

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for pos in self.array[index]:
                if pos[0] == key:
                    # key already exists, update the value
                    pos[1] = value
                    break
            else:
                # key doesn't exist but index does (there previously was a value there)
                self.array[index].append([key, value])
        else:
            # key and index don't exist
            self.array[index] = []
            self.array[index].append([key, value])

    def delete(self, key):
        index = self.hash(key)
        if self.array[index] is not None:
            for pos in self.array[index]:
                if pos[0] == key:
                    del self.array[index]

    def __getitem__(self, key):
        index = self.hash(key)
        if self.array[index] is not None:
            for pos in self.array[index]:
                if pos[0] == key:
                    return pos[1]
        return None

    def __str__(self):
        stringOut = ""
        for pos in self.array:
            if pos is not None:
                stringOut = stringOut + str(pos)[1:-1]
        return stringOut
