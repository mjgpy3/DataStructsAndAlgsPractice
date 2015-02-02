import mmh3

class BloomFilter(object):
    def __init__(self, size, n_hashes):
        self.__values = [0]*size
        self.__hashes = [self.__hash(i) for i in xrange(n_hashes)]
        self.__n_hashes = n_hashes

    def insert(self, item):
        for hash in self.__hashes:
            self.__values[self.__index(hash, item)] = 1

    def __contains__(self, item):
        return sum(self.__values[self.__index(hash, item)] for hash in self.__hashes) == self.__n_hashes

    def __index(self, f, item):
        return f(str(type(item)) + str(item)) % len(self.__values)

    def __hash(self, i):
        return lambda x: mmh3.hash(x, i)
