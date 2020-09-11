def maxStolenValue(values):
    #dp table will store maximal values upto index i
    n=len(values)
    dp=[0 for i in range(n)]
    
    if(n==0):
        return 0
    if(n>=1):
        dp[0]=values[0]
    if(n>=2):
        dp[1]=max(values[0],values[1])

        for i in range(2,n):
            dp[i]=max(dp[i-2]+values[i],dp[i])

    return dp[n-1]

def main():
    values = [6, 1, 2, 7]
    print(maxStolenValue(values))

main()
    
