# Complete the function below.

def string_transformation(words, start, stop):
    #Creating a graph out of words,start, and stop
    def find_adjacent(vertex,words):
        n=len(vertex)
        res=set()
        for word in words:
            difference=0
            for i in range(n):
                if(word[i] is not vertex[i]):
                    difference+=1
            if(difference==1):
                res.add(word)
        return res
                
    words=set(words)
    words.add(stop)
    
    def returnShortestPath(words, start, stop):

        queue = [(start,[start])]
        visited = set()
    
        while queue:
            vertex, path = queue.pop(0)
            visited.add(vertex)
            neighbors=find_adjacent(vertex,words)
            words=words-neighbors
            for node in neighbors:
                if node == stop:
                    return path + [stop]
                else:
                    if node not in visited:
                        visited.add(node)
                        queue.append((node, path + [node]))
        return -1
    
    return returnShortestPath(words,start,stop)

def main():
    words=[]
    start="zzzzz"
    stop="zzzzz"
    print(string_transformation(words, start, stop))

main()
