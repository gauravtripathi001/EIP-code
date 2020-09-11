def fibonacci_brute_force(n):
    if(n==0 or n==1):
        return n
    return fibonacci_brute_force(n-1)+fibonacci_brute_force(n-2)

def fibonacci_top_down(n):
    memo={}
    memo[0]=0
    memo[1]=1
    if(n not in memo):
        memo[n]=fibonacci_top_down((n-1))+fibonacci_top_down((n-2))
    return memo[n]

def fibonacci_bottom_up(n):
    dp={}
    dp[0]=0;dp[1]=1

    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    
    return dp[n]
def fibonacci_bottom_up_space_optimized(n):
    dp={}
    dp[0]=0;dp[1]=1

    for i in range(2,n+1):
        dp[i%3]=dp[(i-1)%3]+dp[(i-2)%3]
    
    return dp[n%3]

def main():
    n=10
    for i in range(0,n+1):
        print("fibonacci_brute_force",i,fibonacci_brute_force(i))
        #print("fibonacci_top_down",i,fibonacci_top_down(i))
        #print("fibonacci_bottom_up",i,fibonacci_bottom_up(i))
        print("fibonacci_bottom_up_space_optimized",i,fibonacci_bottom_up_space_optimized(i))


main()
