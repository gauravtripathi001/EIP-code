import sys
#Count number of ways to reach amount a using coin denominations
def coin_change(a,coins):
    #Table to store the number of coins with amount
        
    table = [0 for k in range(a+1)]
    m=len(coins)
      
    # Base case (If given value is 0) 
    table[0] = 1

    # Pick all coins one by one and update the table[] values 
    # after the index greater than or equal to the value of the 
    # picked coin 
    for i in range(0,m):
        for j in range(coins[i],a+1): 
            table[j] += table[j-coins[i]] 

    return table[a]

def main():
    a=5
    coins=[1,2,5]
    print(coin_change(a,coins))

main()
    
