from collections import OrderedDict


class OrderedSet(OrderedDict):
    def add(self, key):
        self[key] = None
