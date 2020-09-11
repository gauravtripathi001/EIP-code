def coin_denominations(amount,coins):

    c=len(coins)+1
    a=amount+1

    dp=[[0 for i in range(a)] for j in range(c)]

    for i in range(c):
        dp[i][0]=1

    for j in range(1,a):
        dp[0][j]=0

    for i in range(1,c):
        for j in range(1,a):
            dp[i][j]=dp[i-1][j]+ (dp[i][j-coins[i-1]] if(j-coins[i-1]>=0) else 0)

    return dp[c-1][a-1]

def coin_denominations_optimized(amount,coins):
    c=len(coins)+1
    a=amount+1

    dp=[0 for i in range(a)]

    dp[0]=1

    for i in range(1,c):
        for j in range(1,a):
            dp[j]=dp[j]+ (dp[j-coins[i-1]] if(j-coins[i-1]>=0) else 0)

    return dp[a-1]

def main():
    amount=27
    coins=[1,5,10,25]
    print(coin_denominations_optimized(amount,coins))

main()
    
