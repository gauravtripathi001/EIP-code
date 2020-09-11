#Find the maximum sum path in a 2D-grid
def max_path(grid):
    #Initialize a table with row size and col size
    rows=len(grid);cols=len(grid[0])
    table=[[0 for i in range(cols)] for j in range(rows)]
    path=[]
    pointer={}

    #Fill the source column
    table[0][0]=grid[0][0]
    pointer[(0,0)]=-1
    
    #Populate the 0th row and 0th col because there are only one way paths leading to them
    for j in range(1,cols):
        table[0][j]=table[0][j-1]+grid[0][j]
        pointer[(0,j)]=(0,j-1)

    for i in range(1,rows):
        table[i][0]=table[i-1][0]+grid[i][0]
        pointer[(i,0)]=(i-1,0)
    #Populate the rest of the table by iterating over grid
    for i in range(1,rows):
        
        for j in range(1,cols):
            table[i][j]=max(table[i-1][j],table[i][j-1])+grid[i][j]
            pointer[(i,j)]=(i-1,j) if(table[i-1][j]>table[i][j-1]) else (i,j-1)
    return table[rows-1][cols-1],pointer

def create_path(pointers,end):
    parent=pointers[end]
    res=[end]
    while(parent is not -1):
        res.append(parent)
        parent=pointers[parent]
    return res
        
    

def main():
    grid=[[1,3,1],[1,5,1],[4,2,1]]
    max_sum,pointers=max_path(grid)
    rows=len(grid);cols=len(grid[0])
        
    print("Max sum is ",max_sum, "Path is ",create_path(pointers,(rows-1,cols-1)))

main()
