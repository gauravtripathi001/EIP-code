import queue
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insertNode(self,data):
        #check if root node has element
        if self.data:
            if(data<=self.data):
                if(self.left is None):
                    self.left=Node(data)
                else:
                    self.left.insertNode(data)
            elif(data>self.data):
                if(self.right is None):
                    self.right=Node(data)
                else:
                    self.right.insertNode(data)
        else:
            self.data=data
    
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
            print (queue[0].data) 
            node = queue.pop(0) 
    
            #Enqueue left child 
            if node.left is not None: 
                queue.append(node.left) 
    
            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right) 

def main():
    root=Node(6)
    root.insertNode(5)
    root.insertNode(4)
    root.insertNode(7)
    root.insertNode(8)
    root.bfs()

main()
            
    
    