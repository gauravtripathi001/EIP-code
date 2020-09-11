import sys
#Count minimum number of coins needed to reach amount a
def coin_change(a,coins):
    #Table to store the minimum number of coins needed to reach a subproblem with optimal substructure
    table=[10000000]*(a+1)

    #Initialize the number of ways to create value 0
    table[0]=0

    for i in range(1,a+1):
        min_value=1000000
        for c in coins:
            if(i-c>=0):
                min_value=min(min_value,table[i-c])
        table[i]=min_value+1

    if(table[a] is not 10000000):
        return table[a]

    return -1

def main():
    a=10
    coins=[1,5,7]
    print(coin_change(a,coins))

main()
    
