from dictionary import Dictionary

class AssocList(Dictionary):
    def __init__(self):
        self.elem = None

    def insert(self, key, value):
        self.elem = key

    def delete(self, key):
        pass

    def get(self, key):
        pass

    def __contains__(self, key):
        return key == self.elem
