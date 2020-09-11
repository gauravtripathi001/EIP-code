def football_scores(target,scores):
    dp=[0 for i in range(target+1)]
    dp[0]=1
    for i in range(1,target+1):
        for s in scores:
            dp[i]+=dp[i-s] if i>=s else 0
    return dp[target]

def main():
    target=7
    scores=[2,3,6]
    print(football_scores(target,scores))

main()
