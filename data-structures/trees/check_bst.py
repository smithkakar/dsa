'''
Problem: Given a binary tree, check whether it’s a binary search tree or not.
Sol #1: If a tree is a binary search tree, then traversing the tree inorder 
should lead to sorted order of the values in the tree. 
So, we can perform an inorder traversal and check whether the node values are sorted or not.
'''
import math
prev = -math.inf

class Node:
    """
    Creates a Binary tree node that has data,
    a pointer to it's left and right child
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

tree_vals = []
def inorder(tree):
    if tree != None:
        inorder(tree.left)
        tree_vals.append(tree.data)
        inorder(tree.right)

    return tree_vals

def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)

# Alternate way
def checkBST(root):
    global prev

    if root:
        if not checkBST(root.left):
            return False

        if root.data < prev:
            return False
        
        prev = root.data

        return checkBST(root.right)

    return True

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
tree_vals = inorder(root)
print('tree values: ', tree_vals)
print(sort_check(tree_vals))

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(15)
root2.left.left = Node(1)
root2.left.right = Node(4)
# reset the list
tree_vals = []
tree_vals2 = inorder(root2)
print('tree values: ', tree_vals2)
print(sort_check(tree_vals2))

for ele in [root, root2]:
    if checkBST(ele):
        print(f"{ele} Is BST")
    else:
        print(f"{ele} is Not a BST")
