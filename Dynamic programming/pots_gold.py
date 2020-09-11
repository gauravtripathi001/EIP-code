# Your task is to complete this function
# Function should return an integer
def maxCoins(arr, n):
    # Code here
    n=len(arr)
    dp=[[0 for i in range(n)] for j in range(n)]
    
    for num_bags in range(1,n+1):
        for lft in range(0,n-num_bags+1):
            rgt=lft+num_bags-1
            if(num_bags==1):
                dp[lft][rgt]=arr[lft]
            elif(num_bags==2):
                dp[lft][rgt]=max(arr[lft],arr[rgt])
            else:
                dp[lft][rgt]=max((arr[lft]+min(dp[lft+2][rgt],dp[lft+1][rgt-1])),(arr[rgt]+min(dp[lft+1][rgt-1],dp[lft][rgt-2])))
    
    return dp[0][n-1]
