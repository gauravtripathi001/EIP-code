def profit(sell_values):
    days=len(sell_values[0])

    A=0
    B=1

    dp=[[0 for i in range(days+1)] for j in range(2)]

    dp[A][1]=sell_values[A][0]
    dp[B][1]=sell_values[B][0]

    for day in range(2,days+1):
        dp[A][day]=max(dp[A][day-1] if day>=1 else 0,dp[B][day-2] if day>=2 else 0)+sell_values[A][day-1]
        dp[B][day]=max(dp[B][day-1] if day>=1 else 0,dp[A][day-2] if day>=2 else 0)+sell_values[B][day-1]

    return max(dp[A][days],dp[B][days])

def profit_optimized(sell_values):
    days=len(sell_values[0])

    A=0
    B=1

    dp=[[0 for i in range(3)] for j in range(2)]

    dp[A][1]=sell_values[A][0]
    dp[B][1]=sell_values[B][0]

    for day in range(2,days+1):
        dp[A][day%3]=max(dp[A][(day-1)%3] if day>=1 else 0,dp[B][(day-2)%3] if day>=2 else 0)+sell_values[A][day-1]
        dp[B][day%3]=max(dp[B][(day-1)%3] if day>=1 else 0,dp[A][(day-2)%3] if day>=2 else 0)+sell_values[B][day-1]

    return max(dp[A][days%3],dp[B][days%3])

def profit_path(sell_values):
    days=len(sell_values[0])

    A=0
    B=1

    dp=[[0 for i in range(days+1)] for j in range(2)]

    dp[A][1]=sell_values[A][0]
    dp[B][1]=sell_values[B][0]

    for day in range(2,days+1):
        dp[A][day]=max(dp[A][day-1] if day>=1 else 0,dp[B][day-2] if day>=2 else 0)+sell_values[A][day-1]
        dp[B][day]=max(dp[B][day-1] if day>=1 else 0,dp[A][day-2] if day>=2 else 0)+sell_values[B][day-1]

    profit=max(dp[A][days],dp[B][days])
    path=[]
    for day in range(days,0,-1):
        if(dp[A][day]==profit):
            path.append("A")
            profit=profit-sell_values[A][day-1]
        elif(dp[B][day]==profit):
            path.append("B")
            profit=profit-sell_values[B][day-1]
        else:
            path.append("Switch")
    return path
            



def main():
    sell_values=[[8,1,3,5],[2,1,8,7]]
    print(profit(sell_values))
    print(profit_optimized(sell_values))
    print(profit_path(sell_values))
main()
