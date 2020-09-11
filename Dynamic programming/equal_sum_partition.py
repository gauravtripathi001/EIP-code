#
#  Complete the equalSubSetSumPartition function below.
#
#  @param s: input array as parameter.
#

def equalSubSetSumPartition(s):
    # Write your code here
    n=len(s)
    scale_value=(-min(s) if min(s)<0 else min(s)) +1
    s=[i+scale_value for i in s]
    print(s)
    sum_s=sum(s)
    if(sum_s%2 is not 0):
        return []
    target=sum_s//2
    
    dp=[[False for i in range(target+1)] for j in range(n+1)]
    
    for i in range(0,n+1):
        dp[i][0]=True

    for j in range(1,target+1):
        dp[0][j]=False

    #print("Target is",target)
    for i in range(1,n+1):
        for j in range(1,target+1):
            dp[i][j]=dp[i-1][j] or (dp[i-1][j-s[i-1]] if (j-s[i-1]<=target and j-s[i-1]>=0) else False)

    if(dp[n][target] is False):
        return []

    #print(dp)

    #Look up the path in DP array
    target_row=n
    for i in range(1,n+1):
        if(dp[i][target]==True):
            target_row=i
            break
    #print(target_row)
    path=[target_row-1]
    while(target_row>0 and target >= 0):
        #print(target_row,target)
        if(dp[target_row-1][target]==True):
            target_row-=1
        else:
            path.append(target_row-1)
            target=target-s[target_row-1]
            
    #No path so no subset can be created
    if(len(path)==0):
        return []
    
    bool_path=[False for i in range(n)]
    for i in path:
        bool_path[i]=True

    #print(bool_path)
    return bool_path

def main():
    s = [1,0,-1]
    print(equalSubSetSumPartition(s))

main()
    
