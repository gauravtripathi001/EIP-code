#Adjacency map if vertices are not integers. Directed graph
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_map=dict()
        for vertex in vertices:
            self.adj_map[vertex]=dict()

    def add_edge(self,start,end,weight):
        self.adj_map[start][end]=weight

def main():
    vertices=["A","B","C"]
    g=Graph(vertices)
    g.add_edge("A","B",1)
    print(g.adj_map)

main()
