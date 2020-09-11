#User function Template for python3

'''
*  g[]: adj list of the graph
*  N : number of vertices
'''
def bfs_level(g,N):
    # code here
    visited=[0]*N
    q=[]
    
    q.append(0)
    visited[0]=1
    level=1
    while(not len(q)==0):
        size=len(q)
        for e in range(size):
            top=q.pop(0)
            res.append(top)
            neighbors=g[top]
            for i in neighbors:
                if(visited[i]==0):
                    visited[i]=1
                    q.append(i)
        level+=1
    
