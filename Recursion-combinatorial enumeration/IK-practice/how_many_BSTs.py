def how_many_BSTs(n):
    if(n==0 or n==1):
        return 1
    else:
        result=0
        for i in range(0,n):
            result+=how_many_BSTs(i)*how_many_BSTs(n-i-1)
        return result
            

def main():
    n=5
    print(how_many_BSTs(n))

main()
