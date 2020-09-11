def count_ways_to_top(n):
    dp={}
    dp[1]=1;dp[2]=2
    for i in range(3,n+1):
        dp[i%3]=dp[(i-1)%3]+dp[(i-2)%3]
    return dp[n%3]

def main():
    n=4
    print("No of ways to reach at stair",n,count_ways_to_top(n))
    
main()
