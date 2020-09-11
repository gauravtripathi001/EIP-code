#Minimum cost stair climbing
def min_cost_stair(costarray):
    pointers={}
    n=len(costarray)
    #Adding a 0 to the end of cost array because the nth step will
    #lead to the floor above and the floor above has 0 cost
    costarray.append(0)
    
    table=[0]*(n+2)
    #Initializing table for the starting position
    #Cost to reach floor below or starting position is 0.
    table[0]=0
    pointers[0]=-1
    #Initializing the table with the cost of taking the first step
    table[1]=costarray[0]
    pointers[1]=0
    #Traverse the costarray and populate the table entries
    for i in range(2,n+2):
        table[i]=costarray[i-1]+min(table[i-1],table[i-2])
        pointers[i]=i-1 if(table[i-1]<table[i-2]) else i-2
    return table[n+1],pointers

def create_path(pointers,end):
    res=[end]
    parent=pointers[end]
    while(parent is not -1):
        res.append(parent)
        parent=pointers[parent]
    return res

def main():
    costarray=[1,100,1,1,1,100,1,1,100,1]
    min_cost,path_pointers=min_cost_stair(costarray)
    print("Min cost is",min_cost)
    print("Path is",create_path(path_pointers,len(costarray)))

main()
