def production_plan_profit(sell_values):
    days=len(sell_values[0])
    A=0
    B=1
    dp=[[0 for i in range(days)] for j in range(2)]

    dp[A][0],dp[A][1]=sell_values[A][0],sell_values[A][0]+sell_values[A][1]
    dp[B][0],dp[B][1]=sell_values[B][0],sell_values[B][0]+sell_values[B][1]

    for i in range(2,days):
        dp[A][i]=max(dp[A][i-1],dp[B][i-2])+sell_values[A][i]
        dp[B][i]=max(dp[B][i-1],dp[A][i-2])+sell_values[B][i]

    return max(dp[A][days-1],dp[B][days-1])

def main():
    sell_values=[[8,1,3],[2,1,8]]
    print(production_plan_profit(sell_values))

main()
