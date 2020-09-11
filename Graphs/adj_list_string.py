#Adjacency list if vertices are not integers. Directed graph
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_map_list=dict()
        for vertex in self.vertices:
            self.adj_map_list[vertex]=[]

    def add_edge(self,start,end):
        self.adj_map_list[start].append(end)

def main():
    vertices=["A","B","C"]
    g=Graph(vertices)
    g.add_edge("A","B")
    print(g.adj_map_list)

main()
