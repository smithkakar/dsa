'''
Problem: Given a singly linked list, write a function which takes in the first node 
in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list. 
This is also sometimes known as a circularly linked list.
'''

from nose.tools import assert_equal

class TestCycleCheck(object):
    
    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)
        print("ALL TEST CASES PASSED")

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.nextnode = None

def check_cycle(node):
    input_node = node
    while node.nextnode is not None:
        if node.nextnode == input_node:
            return True
        node = node.nextnode
    return False
    
# CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle!

# NON-CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

t = TestCycleCheck()
t.test(check_cycle)