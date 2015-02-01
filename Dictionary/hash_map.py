from dictionary import Dictionary

class HashMap(Dictionary):
    def __init__(self, load_factor = 0.75):
        self.__load_factor = load_factor
        self.__capacity = 16

    def capacity(self):
        return self.__capacity

    def doubling_size(self):
        return self.__capacity * self.__load_factor
