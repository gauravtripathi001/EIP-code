#Fibonacci using DP

#First create a memo dictionary to memorize results
memo={0:0,1:1}

def fibo(n):
    if(n not in memo):
        memo[n]=fibo(n-1)+fibo(n-2)
    return memo[n]

def main():
    n=10
    for i in range(n+1):
        print("fibo(",i,")",fibo(i))

main()
