#Bottom up implementation of fibonacci

memo={0:0,1:1}
def fibo(n):
    for i in range(2,n+1):
        memo[i]=memo[i-1]+memo[i-2]
    return memo[n]

def main():
    n=10
    for i in range(n+1):
        print(i,fibo(i))

main()
