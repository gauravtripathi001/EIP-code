#Count number of ways to traverse 2D grid where you can move right and down
def count_2d(r,c):
    table=[[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        table[i][0]=1
    for j in range(c):
        table[0][j]=1
    for i in range(1,r):
        for j in range(1,c):
            table[i][j]=table[i-1][j]+table[i][j-1]
    return table[r-1][c-1]

def main():
    rows=5
    cols=5
    print(count_2d(rows,cols))
main()

    
