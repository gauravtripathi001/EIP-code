def american_football(scores,target):
    dp=[0 for i in range(target+1)]
    dp[0]=1

    
    for i in range(1,target+1):
        for score in scores:
            if(i-score>=0):
                dp[i]+=dp[i-score]

    return dp[target]

def main():
    scores=[2,3,6]
    target=7
    print(american_football(scores,target))

main()
        
                
