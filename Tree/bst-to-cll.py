class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left_ptr = left
        self.right_ptr = right
def inorderSuccessor(root, x):
        # Code here
        if(root==None):
            return root
        if(root==x and (root.right_ptr is None and root.left_ptr is None)):
            return None
            
        curr=x
        if(curr.right_ptr is not None):
            curr=curr.right_ptr
            while(curr.left_ptr is not None):
                curr=curr.left_ptr
            return curr
        
        #Search for x in tree
        
        prev=None
        curr=root
        
        while curr is not None:
            if(x==curr):
                break
            elif(x.val<curr.val):
            #Save ancestor of x whenever a left turn is made to search for x
                prev=curr
                curr=curr.left_ptr
            else:
                curr=curr.right_ptr
        #else return the ancestor
        return prev
    
def BTtoLL(root):
    def inorderSuccessor(root, x):
        # Code here
        if(root==None):
            return root
        if(root==x and (root.right_ptr is None and root.left_ptr is None)):
            return None
            
        curr=x
        if(curr.right_ptr is not None):
            curr=curr.right_ptr
            while(curr.left_ptr is not None):
                curr=curr.left_ptr
            return curr
        
        #Search for x in tree
        
        prev=None
        curr=root
        
        while curr is not None:
            if(x==curr):
                break
            elif(x.val<curr.val):
            #Save ancestor of x whenever a left turn is made to search for x
                prev=curr
                curr=curr.left_ptr
            else:
                curr=curr.right_ptr
        #else return the ancestor
        return prev
    def postorder(root,node):
        if(node==None):
            return None
        postorder(root,node.left_ptr)
        postorder(root,node.right_ptr)
        curr=node
        next=inorderSuccessor(root, node)
        
        if(next is not None):
            curr.right_ptr=next
            next.left_ptr=curr
            print(curr.val,next.val)
        

    
    postorder(root,root)
    #Join the first and last element
    first=root
    last=root
    while(last.right_ptr is not None):
        #print("Last is",last)
        last=last.right_ptr
    last.right_ptr=first
    first.left_ptr=last
    return first

def main():
    root=TreeNode(4)
    root.left_ptr=TreeNode(2)
    root.right_ptr=TreeNode(5)
    #root.left_ptr.left_ptr=TreeNode(1)
    #root.left_ptr.right_ptr=TreeNode(3)
    #print(inorderSuccessor(root,TreeNode(1)).val)
    
    BTtoLL(root)
    
    
main()
