class Solution:
    def calcEquation(self, equations,values,queries):
        def build_graph(equations,values):
            #a graph with vertices, adjMap(neighbor,weight)
            graph={}
            
            for i,equation in enumerate(equations):
                u,v=equation
                if(u not in graph):
                    graph[u]={v:values[i]}
                else:
                    graph[u][v]=values[i]
                if(v not in graph):
                    graph[v]={u:1/values[i]}
                else:
                    graph[v][u]=1/values[i]
            
            return graph
        
        def get_weight(graph,s,t,visited):
            #if s or t not in graph
            if(s not in graph or t not in graph):
                return -1
            
            #if s and t have an edge
            if(t in graph[s]):
                return graph[s][t]
            #Check if neighbor contains a path to t
            visited.add(s)
            for neighbor,weight in graph[s].items():
                if(neighbor not in visited):
                    v=get_weight(graph,neighbor,t,visited)
                    if(not(v==-1)):
                        return weight*v
            #visited.remove(s)
            
            return -1
        
        graph=build_graph(equations,values)
        res=[]
        visited=set()
        for query in queries:
            res.append(get_weight(graph,query[0],query[1],visited))
        return res
        
def main():
    equations=[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values=[3.0,4.0,5.0,6.0]
    #queries=[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    queries=[["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    s=Solution()
    print(s.calcEquation(equations,values,queries))

main()
