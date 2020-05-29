import queue

class tree_node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

    def search(self,key):
        if self is None:
            return None
        #Let us start from the root. Take a pointer to the root
        curr=self
        while curr is not None:
            if(key==curr.key):
                return curr
            elif(key<curr.key):
                curr=curr.left
            else:
                curr=curr.right
        return None

    def insert(self,key):
        newNode=tree_node(key)
        if(self is None):
            return newNode
        #Let us start from the root. Take a pointer to the root
        prev=None
        curr=self
        while curr is not None:
            if(key==curr.key):
                return
            elif(key<curr.key):
                prev=curr
                curr=curr.left
            else:
                prev=curr
                curr=curr.right
        if(key<prev.key):
            prev.left=newNode
        else:
            prev.right=newNode
        return self
    
    def find_min(self):
        if(self is None):
            return None
        curr=self
        while curr.left is not None:
            curr=curr.left
        return curr.key
        
    
    def bfs(self):
        # Base Case 
        if self is None: 
            return
        
        # Create an empty queue for level order traversal 
        queue = [] 
    
        # Enqueue Root and initialize height 
        queue.append(self) 
    
        while(len(queue) > 0): 
            # Print front of queue and remove it from queue 
            print (queue[0].key) 
            node = queue.pop(0) 
    
            #Enqueue left child 
            if node.left is not None: 
                queue.append(node.left) 
    
            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right)

def main():
    root=tree_node(6)
    #root.bfs()
    root.insert(5)
    #root.bfs()
    root.insert(4)
    root.insert(7)
    root.insert(8)
    #root.bfs()
    #print((root.find_min()))

main()
        
        
