def unique_paths_brute_force(grid):
    rows=len(grid);cols=len(grid[0])
    table=[[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        table[i][0]=1
    for j in range(cols):
        table[0][j]=1
    for i in range(1,rows):
        for j in range(1,cols):
            table[i][j]=table[i-1][j]+table[i][j-1]
    return table[rows-1][cols-1]
def unique_paths_space_optimized(grid):
    rows=len(grid);cols=len(grid[0])
    upper_row=[1 for i in range (cols)]
    current_row=[1 for i in range (cols)]

    for i in range(1,rows):
        current_row=[1 for i in range (cols)]
        for j in range(1,cols):
            current_row[j]=upper_row[j]+current_row[j-1]
        upper_row=current_row
    return upper_row[cols-1]
            
#def unique_paths_obstacles(grid):
#Leetcode problem solved
    
def main():
    rows=4;cols=5
    grid=[[0 for j in range(cols)] for i in range(rows)]
    print("unique_paths_brute_force(grid):",unique_paths_brute_force(grid))
    print("unique_paths_space_optimized(grid):",unique_paths_space_optimized(grid))
main()
