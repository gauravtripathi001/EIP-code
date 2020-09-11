# Complete the function below.


def levenshteinDistance(strWord1, strWord2):
    a=len(strWord1);b=len(strWord2)

    dp=[[0 for j in range(a+1)] for i in range(b+1)]

    for i in range(0,b+1):
        dp[i][0]=i
    for j in range(0,a+1):
        dp[0][j]=j

    for i in range(1,b+1):
        for j in range(1,a+1):
            if(strWord1[j-1]==strWord2[i-1]):
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[b][a]

def main():
    s1="qwe"
    s2="q"
    print(levenshteinDistance(s1,s2))

main()
    

    
