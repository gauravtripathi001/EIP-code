# Complete the function below.

# For your reference:
#
# class Node:
#     def __init__(self):
#         self.val = 0
#         self.neighbours = []

def build_other_graph(node):
    visited=set()
    #The dfs will add all the elements to the visited set as the graph is strongly connected
    dfs(node,visited)

    new_visited={}
    #We iterate over each node
    for i in visited:
        if i.val not in new_visited:
            new_node=Node()
            new_node.val=i.val
            new_visited[i.val]=new_node
    #For each neighbor in the node, we reverse the edges
        for neighbor in i.neighbours:
            if neighbor.val not in new_visited:
                new_neighbor=Node()
                new_neighbor.val=neighbor.val
                new_visited[neighbor.val]=new_neighbor
            new_visited[neighbor.val].neighbours.append(new_visited[i.val])
            
    return new_unvisited[node.val]
        
    

def dfs(node,visited):
    visited.add(node)
    for neighbor in node.neighbors:
        if(neighbor not in visited):
            dfs(neighbor,visited)
