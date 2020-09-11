from collections imprt deque
class Node:
    def __init__(self):
        self.inDegree=0
        self.neighbors=[]

class Solution:
    def canFinish(self,numCourses,prerequisites):
        #Initialization
        map={}
        for i in range(numCourses):
            map[i]=Node()

        for courses in prerequisites:
            map[courses[0]].inDegree+=1
            map[courses[1]].neighbors.append(map[courses[0]])

        #Find vertices with 0 indegree
        q=deque()
        for k,v in map.items():
            if(v.indegree==0):
                q.append(v)

        #Topological sort
        while(len(q)>0):
            node=q.popleft()
            for child in node.neighbors:
                child.inDegree-=1
                if(child.inDegree==0):
                    q.append(child)

        #Has circular dependency
        for k,node in map.items():
            if(not (node.inDegree==0)):
                return False

        return True
            

        
