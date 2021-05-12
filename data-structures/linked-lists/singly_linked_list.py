'''
- Linked Lists have constant-time insertions and deletions in any position, 
in comparison, arrays require O(n) time to do the same thing.
- Linked lists can continue to expand without having to specify their size ahead of time.
- To access an element in a linked list, we need to take O(k) time to go from 
the head of the list to the kth element. 
In contrast, arrays have constant time operations to access elements in an array.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
print('first node value: ', a.value)
print('next node value: ', a.next_node.value)