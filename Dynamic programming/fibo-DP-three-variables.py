#Fibonacci with 3 integer variables
def fibo(n):
    #0
    b=0
    #1
    a=1
    if(n==0 or n==1):
        return n
    c=0
    for i in range(2,n+1):
        c=a+b
        temp=a
        a=c
        b=temp
    return c

def main():
    n=10
    for i in range(n+1):
        print(i,fibo(i))

main()
