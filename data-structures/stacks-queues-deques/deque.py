#!/usr/local/bin/env python3
'''
Deque Implementation using List
'''


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
d.addFront('hello')
d.addRear('world')
print('deque size: ', d.size())
print(f'removing front i.e. {d.removeFront()} and rear i.e. {d.removeRear()}')
print('deque size: ', d.size())
