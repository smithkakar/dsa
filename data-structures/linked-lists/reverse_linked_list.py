#!/usr/local/bin/env python3
'''
Write a function to reverse a Linked List in place O(1) space. 
The function will take in the head of the list as input and return the new head of the list.
'''


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(head):
    current = head
    previous = None
    nextnode = None
    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode

    return previous


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(f'next node to a: {a.nextnode.value}')
print(f'next node to b: {b.nextnode.value}')
print(f'next node to c: {c.nextnode.value}')

print('-'*24)
print('reversing the linkedlist')
reverse(a)
print('-'*24)

print(f'next node to d: {d.nextnode.value}')
print(f'next node to c: {c.nextnode.value}')
print(f'next node to b: {b.nextnode.value}')
