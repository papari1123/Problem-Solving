"""
5. binary search tree.

https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
"""

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

def lca(root, n1, n2):
     
    # Base Case
    if root is None:
        return None
 
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)
 
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
r1 = Node(20)
r = insert(r1,22)
r = insert(r,8)
r = insert(r,4)
r = insert(r,12)
r = insert(r,10)
r = insert(r,14)
