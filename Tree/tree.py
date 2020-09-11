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
    def levelOrder(self):
        if(self is None):
            return None
        q=[]
        res=[]
        q.append(self)
        while(len(q)>0):
            n=len(q)
            temp=[]
            #All the n nodes are at the same level
            for i in range(n):
                node=q.pop(0)
                temp.append(node.data)
                if(node.left is not None):
                    q.append(node.left)
                if(node.right is not None):
                    q.append(node.right)
            #Append all the nodes at a particular level to the result list
            res.append(temp)
        return res
    def zigzagLevelOrder(self):
        if(self is None):
            return None
        q=[]
        res=[]
        q.append(self)
        #Use this flag to alternate the list level by level
        flag=0
        while(not len(q)==0):
            n=len(q)
            temp=[]
            #All the n nodes are at the same level
            for i in range(n):
                node=q.pop(0)
                temp.append(node.data)
                if(node.left is not None):
                    q.append(node.left)
                if(node.right is not None):
                    q.append(node.right)
            #Append all the nodes at a particular level to the result list
            if(flag==0):
                res.append(temp)
                flag=1
            else:
                res.append(temp[::-1])
                flag=0
        return res
    def isCompleteTree(self):
        nodes = [(self, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))

        return  nodes[-1][1] == len(nodes)

def main():
    root=Node(6)
    root.insertNode(5)
    root.insertNode(4)
    root.insertNode(7)
    root.insertNode(8)
    #root.bfs()
    print(root.levelOrder())
    #print(root.zigzagLevelOrder())
    print(root.isCompleteTree())


main()
            
    
    
