class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph=self.buildGraph(numCourses,prerequisites)
        visited=[0]*numCourses
        #print(graph)
        for i in range(numCourses):
            if(visited[i]==0):
                if(self.hasCycle(i,graph,visited)):
                    return False
        return True
        
                   
    def buildGraph(self,numCourses,prerequisites):
        graph={}
        for i in range(numCourses):
            graph[i]=[]
        for i in prerequisites:
            graph[i[1]].append(i[0])
        return graph
        
    def hasCycle(self,s,graph,visited):
        visited[s]=1
        for i in graph[s]:
            if(visited[i]==0 and self.hasCycle(i,graph,visited)):
                return True
            if(visited[i]==1):
                return True
        visited[s]=2
        return False

def main():
    numCourses=2
    prerequisites=[[1,0]]
    sol=Solution()
    print(sol.canFinish(numCourses,prerequisites))
main()
