""""
5. binary search tree.

https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
""""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# A utility function to search a given key in BST

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)
 
# This code is contributed by Bhavya Jain
