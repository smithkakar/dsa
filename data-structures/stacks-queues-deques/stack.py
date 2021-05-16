#!/usr/local/bin/env python3
'''
Stack Implementation using List
'''


class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        # return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()
print("Empty Stack? ", s.isEmpty())

print('pushing one element')
s.push(1)
print('pushing second element')
s.push('two')
print('stack size: ', s.size())
