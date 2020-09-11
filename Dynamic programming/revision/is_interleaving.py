def isInterleave(A, B, C):
    # Code here
    len_a=len(A);len_b=len(B);len_c=len(C)
    if(not len_c==(len_a+len_b)):
        return False
    #Create DP table
    dp=[[False for j in range(len_a+1)] for i in range(len_b+1)]
    
    #Initialize the empty string interleaving
    dp[0][0]=True
    
    #Initialize first row and first column
    for i in range(1,len_b+1):
        dp[i][0]=(dp[i-1][0] and B[i-1]==C[i-1])
    
    for j in range(1,len_a+1):
        dp[0][j]=(dp[0][j-1] and A[j-1]==C[j-1])
        
    #Calculate the intermediate dp table values
    for i in range(1,len_b+1):
        for j in range(1,len_a+1):
            dp[i][j]=(dp[i-1][j] and (B[i-1]==C[i+j-1])) or (dp[i][j-1] and (A[j-1]==C[i+j-1]))
    #return the result of dp
    print(dp)
    return dp[len_b][len_a]

def main():
    #s1 = "aabcc";s2 = "dbbca";s3 = "aadbbcbcac"
    #s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbbaccc"
    s1="db";s2="b";s3="cbb"
    #s1="xyzy";s2="xyx";s3="xyxzxyy"
    #s1="X";s2="YXYXYXYXY";s3="YYYXXXYXYX"
    print(isInterleave(s1,s2,s3))

main()
