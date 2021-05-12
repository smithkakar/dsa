class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
b.prev_node = a
c.prev_node = b
print('first node value (not head sentinel): ', b.value)
print('next node value: ', b.next_node.value)
print('previous node value: ', b.prev_node.value)