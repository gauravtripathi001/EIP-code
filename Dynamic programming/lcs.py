#In this approach, we create the dp table with the actual strings
#The drawback here is that a lot of extra space is wasted in storing the actual strings
def lcs(a, b):
    # Write your code here
    la=len(a);lb=len(b)
    dp=[["" for j in range(la+1)] for i in range(lb+1)]
    
    for i in range(1,lb+1):
        for j in range(1,la+1):
            if(a[j-1]==b[i-1]):
                dp[i][j]=dp[i-1][j-1]+a[j-1]
            else:
                dp[i][j]=(dp[i][j-1] if len(dp[i][j-1])>len(dp[i-1][j]) else dp[i-1][j])
    return dp[lb][la]

#This approach creates the dp table with the longest subsequences of substrings
#Then the actual subsequence is created by tracing back through the dp table
def lcs_space_optimized(a,b):
    la=len(a);lb=len(b)
    dp=[[0 for j in range(la+1)] for i in range(lb+1)]

    for i in range(1,lb+1):
        for j in range(1,la+1):
            if(a[j-1]==b[i-1]):
                dp[i][j]=1 + dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    #Trace path
    s=""
    i=lb;j=la
    while(i>0 and j>0):
        if(a[j-1]==b[i-1]):
            s+=a[j-1]
            j-=1;i-=1
        else:
            if(dp[i-1][j]>dp[i][j-1]):
                i-=1
            else:
                j-=1

    return s[::-1]
                
                

def main():
    a="abcdef"
    b="aecbdf"
    print(lcs_space_optimized(a,b))

main()
