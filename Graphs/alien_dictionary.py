from collections import deque

class Node:
    def __init__(self,val):
        self.val=val
        self.indegree=0
        self.neighbors=[]

def alien_dictionary(x):
    graph={}
    for i in range(len(x)-1):
        build_directed_graph(graph,x[i],x[i+1])

    q=deque()
    #Preprocess nodes with zero indegree
    for k,v in graph.items():
        #######
        print(k)
        for i in v.neighbors:
            print(i.val)
        print()
        #######
        if(v.indegree==0):
            q.append(v)

    #Topological sort
    result=[]
    while(len(q)>0):
        node=q.popleft()
        result.append(node.val)
        for child in node.neighbors:
            child.indegree-=1
            if(child.indegree==0):
                q.append(child)

    return result
    

    
    

def build_directed_graph(graph,x,y):
    for i in range(min(len(x),len(y))):
        if(x[i]==y[i]):
            continue
        else:
            node=Node(x[i])
            if(x[i] not in graph):
                graph[x[i]]=node

            neighbor=Node(y[i])
            if(y[i] not in graph):
                graph[y[i]]=neighbor
                graph[y[i]].indegree=1
            else:
                graph[y[i]].indegree+=1

            graph[x[i]].neighbors.append(graph[y[i]])
            return
    return

def main():
    x=["baa", "abcd", "abca", "cab", "cad"]
    print(alien_dictionary(x))
main()
