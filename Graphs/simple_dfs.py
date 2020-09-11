def dfs(graph):
    n=len(graph)
    visited=[False]*n
    for i in range(n):
        if(visited[i]==False):
            dfs(i,visited)

def dfs(s,visited):
    visited[s]=True
    for i in graph[s]:
        if(visited[i]==False):
            dfs(i,visited)
