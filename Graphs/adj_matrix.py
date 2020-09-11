#Adjacency matrix-Not 100% sure if correct or not
class Graph:
    def __init__(self,n):
        self.n=n
        self.matrix=[ [ 0 for i in range(n) ] for j in range(n) ] 

    def addEdge(self,start,end):
        self.matrix[start][end]=1

def main():
    g=Graph(3)
    g.addEdge(1,2)
    print(g.matrix)

main()
        
