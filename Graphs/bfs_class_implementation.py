from collections import deque 

class Graph:
    def __init__(self,n,edges):
        self.n=n
        self.map={}

        for i in range(1,n+1):
            self.map[i]=[]

        for edge in edges:
            self.map[edge[0]].append(edge[1])

    def bfs(self,s):
        visited=[False for i in range(self.n)]
        queue=deque()

        queue.append(s)
        visited[s-1]=True

        while(queue):
            top=queue.popleft()
            for i in self.map[top]:
                if(!(visited[i-1]):
                   visited[i-1]=True
                   queue.append(i)

    def bfs_with_levels(self,s):
            visited=[False for i in range(self.n)]
            queue=deque()

            queue.append(s)
            visited[s-1]=True
            level=1
            while(queue):
                #Number of vertices in current level
                size=len(queue)
                for j in range(size):
                    top=queue.popleft()
                    for i in self.map[top]:
                        if(!(visited[i-1]):
                           visited[i-1]=True
                           queue.append(i)
                level+=1
