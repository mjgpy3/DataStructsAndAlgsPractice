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
        if len(self) == self.doubling_size():
            self.__rehash()
        return self

    def get(self, key):
        v = self.__get(key)

        if v: return v[1]

        raise KeyError(str(key) + ' key not found')

    def __contains__(self, key):
        return bool(self.__get(key))

    def delete(self, key):
        i = self.__locate_index(key)
        v = self.__values[i]
        if v:
            self.__values[i] = (v[0], v[1], False)
        return self

    def capacity(self):
        return self.__capacity

    def doubling_size(self):
        return self.__capacity * self.__load_factor

    def __insert(self, key, value):
        self.__values[self.__locate_index(key)] = (key, value, True)

    def __get(self, key):
        value = self.__values[self.__locate_index(key)]
        return value if value and value[2] else None

    def __locate_index(self, key):
        i = hash(key) % self.capacity()

        while self.__values[i] and self.__values[i][0] != key:
            i = (i + 1) % self.capacity()

        return i

    def __rehash(self):
        self.__size = 0
        self.__capacity *= 2
        old_values = self.__values[:]
        self.__values = [0]*self.__capacity

        for i in old_values:
            if i and i[2]:
                self.insert(i[0], i[1])

    def __len__(self):
        return self.__size
