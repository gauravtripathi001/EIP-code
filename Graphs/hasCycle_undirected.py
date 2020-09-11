class Graph:
    def __init__(self,n,edges):
        self.n=n
        self.map={}

        #Add empty list to each vertex to store neighbors
        for i in range(self.n):
            map[i]=[]

        for edge in edges:
            map[edge[0]].append(edge[1])

    def hasCycle(self):
        #0: unvisited
        #1: being visited
        #2: already visited
        status=[0]*self.n
        for i in range(self.n):
            if(status[i]==0):
                if(dfs(i,-1,status)):
                    return True
        return False

    def dfs(s,parent,status):
        status[s]=1
        for i in self.map[s]:
            if(status[i]==0 and dfs(i,s,status)):
                return True
            #The vertex is visited by its descendant
            elif(status[i]==1 and (i is not parent)):
                return True
        status[s]=2
        return False

        
            
            
