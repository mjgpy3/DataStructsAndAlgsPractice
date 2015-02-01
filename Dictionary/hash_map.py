from dictionary import Dictionary

class HashMap(Dictionary):
    def __init__(self, load_factor = 0.75):
        self.__load_factor = load_factor
        self.__capacity = 16
        self.__size = 0
        self.__values = [None]*self.__capacity

    def insert(self, key, value):
        self.__size += 1
        self.__values[key.hash()] = (key, value)
        return self

    def get(self, key):
        v = self.__values[key.hash()]

        if v: return v[1]

        raise KeyError(str(key) + ' key not found')

    def __contains__(self, key):
        return self.__values[key.hash()]

    def __len__(self):
        return self.__size

    def capacity(self):
        return self.__capacity

    def doubling_size(self):
        return self.__capacity * self.__load_factor
