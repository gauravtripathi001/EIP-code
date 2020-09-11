#User function Template for python3

'''
*  g[]: adj list of the graph
*  N : number of vertices
'''
def bfs(g,N):
    # code here
    visited=[0]*N
    q=[]
    res=[]
    q.append(0)
    visited[0]=1
    while(not len(q)==0):
        top=q.pop(0)
        res.append(top)
        neighbors=g[top]
        for i in neighbors:
            if(visited[i]==0):
                visited[i]=1
                q.append(i)
    return res
