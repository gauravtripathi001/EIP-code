#Counting subsets of size k-DP
def subsets(n,k):
    table=[[0 for i in range(k+1)] for j in range(n+1)]
    for r in range(1,n+1):
        table[r][0]=1
    for c in range(1,k+1):
        table[c][c]=1
    #If you do not understand these indices, you would need to look it up on the video
    for r in range(2,n+1):
        for c in range(1,min(k,r)+1):
            table[r][c]=table[r-1][c-1]+table[r-1][c]

    return table[n][k]

def main():
    print(subsets(4,2))

main()
