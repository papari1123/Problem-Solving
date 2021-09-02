"""
reference :
https://www.geeksforgeeks.org/binary-tree-set-1-introduction/

1. Tree node
"""

# A Python class that represents an individual node
# in a Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

"""
2. preorder, inorder, postorder search
 pre-order : root->left->right
  in-order : left->root->right
post-order : left->right->root
"""    

def preorder_search(node):
    if(node!=None):
        print(node.val)
        preorder_search(node.left)
        preorder_search(node.right)

def inorder_search(node):
    if(node != None):
        inorder_search(node.left)
        print(node.val)
        inorder_search(node.right)

def postorder_search(node):
    if(node != None):
        postorder_search(node.right)
        postorder_search(node.left)
        print(node.val)

root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
print('pre-order')
preorder_search(root)
print('in-order')
inorder_search(root)
print('post-order')
postorder_search(root)

"""
3. 
"""