#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# The function returns the root of the BST (currently rooted at 'root') 
# after inserting a new Node with value 'Key' into it. 
def insert(root, Key):
    # code here
    new_node=Node(Key)
    if(root is None):
        
        return new_node
    
    
    
    prev=None
    curr=root
    
    while curr is not None:
        if(Key==curr.data):
            return root
        elif(Key<curr.data):
            prev=curr
            curr=curr.left
        else:
            prev=curr
            curr=curr.right
    if(Key<prev.data):
        prev.left=new_node
    else:
        prev.right=new_node
    return root
