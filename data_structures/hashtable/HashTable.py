class HashTable:
    def __init__(self):
        self.table = [[] for x in range(13)]

    def hash(self, key):
        chrcodes = sum([ord(x) for x in key])
        return chrcodes % 13 

    def insert(self, key, data):
        # try to get existing key
        print(self.hash(key))
        for item in self.table[self.hash(key)]:
            if item[0] == key:
                item[1] == data
                return
        self.table[self.hash(key)].append((key, data))

    def remove(self, key):
        data = self.get(key)
        if data:
            self.table[self.hash(key)].remove((key, data))

    def get(self, key):
        for item in self.table[self.hash(key)]:
            if item[0] == key:
                return item[1]
        return None