from dictionary import Dictionary

class HashMap(Dictionary):
    def __init__(self, load_factor = 0.75):
        self.__load_factor = load_factor
        self.__capacity = 16
        self.__size = 0
        self.__values = [0]*self.__capacity

    def insert(self, key, value):
        self.__size += 1
        self.__insert(key, value)
        return self

    def __insert(self, key, value):
        self.__values[self.__locate_index(key)] = (key, value)

    def get(self, key):
        v = self.__get(key)

        if v: return v[1]

        raise KeyError(str(key) + ' key not found')

    def __get(self, key):
        return self.__values[self.__locate_index(key)]

    def __locate_index(self, key):
        i = hash(key) % self.capacity()

        while self.__values[i] and self.__values[i][0] != key:
            i = (i + 1) % self.capacity()

        return i

    def __contains__(self, key):
        return bool(self.__get(key))

    def __len__(self):
        return self.__size

    def capacity(self):
        return self.__capacity

    def doubling_size(self):
        return self.__capacity * self.__load_factor
