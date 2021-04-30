'''
Queue Implementation using List
'''

class Queue:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        # insert at rear end i.e. opposite of the top
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
print('queue size: ', q.size())
print('enqueuing first item')
q.enqueue(1)
print('queue size: ', q.size())
