def n_choose_k(n,k):
    r=n;c=k
    table=[[0 for j in range(c+1)] for i in range(r+1)]
    if(k==0 or k==n):
        return 1
    
    for i in range(0,r+1):
        table[i][0]=1
    for j in range(0,c+1):
        table[j][j]=1
        
    for i in range(1,r+1):
        for j in range(1,min(i,c+1)):
            table[i][j]=table[i-1][j]+table[i-1][j-1]
            
    #print(table)
    return table[n][k]
        
def main():
    n=6;k=1
    print(n,"choose",k, "is",n_choose_k(n,k))

main()
    
