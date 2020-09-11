#Adjacency list representation for integer vertices for directed graphs.
class Graph:
    def __init__(self,n):
        self.n=n
        self.adjList=[]
        for i in range(n):
            self.adjList.append([])

    def add_edge(self,start,end):
        self.adjList[start].append(end)

def main():
    g=Graph(3)
    g.add_edge(1,2)
    print(g.adjList)

main()
    
    
    
