from dictionary import Dictionary

class AssocList(Dictionary):
    def __init__(self):
        self.list = None

    def insert(self, key, value):
        self.list = Node((key, value), self.list)

    def delete(self, key):
        self.list.delete_where(lambda t: t[0] == key)

    def get(self, key):
        v = self.__item_at(key)

        if v: return v[1]

        raise KeyError(key + ' not found')

    def __contains__(self, key):
        return bool(self.__item_at(key))

    def __item_at(self, key):
        return self.list and self.list.find_where(lambda t: t[0] == key)

class Node(object):
    def __init__(self, datum, next = None):
        self.datum = datum
        self.next = next
        self.true_node = True

    def delete_where(self, p):
        if p(self.datum):
            self.true_node = False
        if self.next:
            self.next.delete_where(p)

    def find_where(self, p):
        if self.true_node and p(self.datum):
            return self.datum

        return self.next and self.next.find_where(p)
