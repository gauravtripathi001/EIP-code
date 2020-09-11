class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
            la=len(s1);lb=len(s2);lc=len(s3)
            if(la+lb is not lc):
                return False
            
            dp=[[False for i in range(la+1)] for j in range(lb+1)]
            

            for j in range(0,lb+1):
                for i in range(0,la+1):
                    dp[j][i]=( (i==0 and j==0) or (i>0 and dp[j][i-1] and s1[i-1]==s3[i+j-1]) or (j>0 and dp[j-1][i] and s2[j-1]==s3[i+j-1]))
            print(dp)
            return dp[lb][la]

def main():
    s=Solution()
    #s1 = "aabcc";s2 = "dbbca";s3 = "aadbbcbcac"
    #s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbbaccc"
    s1="db";s2="b";s3="cbb"
    #s1="X";s2="YXYXYXYXY";s3="YYYXXXYXYX"
    #s1="xyzy";s2="xyx";s3="xyxzxyy"

    print(s.isInterleave(s1,s2,s3))

main()
