#!/usr/local/bin/env python3
class QueueWithStacks:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


q = QueueWithStacks()

for i in range(5):
    print('enqueue item: ', i)
    q.enqueue(i)

print('-' * 16)

for i in range(5):
    print('dequeue item: ', q.dequeue())
