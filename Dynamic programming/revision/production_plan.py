def production_plan(arr):
    A=0;B=1
    days=len(arr[0])
    dp=[[0 for i in range(days)] for j in range(2)]
    
    dp[A][0]=arr[A][0];dp[B][0]=arr[B][0];dp[A][1]=arr[A][1];dp[B][1]=arr[B][1]
    for day in range(2,days):
    #Max profit on day i when the A is last one
        dp[A][day]=max(dp[A][day-1],dp[B][day-2])+arr[A][day]
    #Max profit on day i when the B is last one
        dp[B][day]=max(dp[B][day-1],dp[A][day-2])+arr[B][day]
        
    #Max profit on day i=max(Max profit on day i when the A is last one
    #+Max profit on day i when the B is last one)
    return dp,max(dp[A][days-1],dp[B][days-1])

def dp_trace_path(arr):
    dp=production_plan(arr)[0]
    A=0;B=1
    days=len(arr[0])
    print(dp)
    
    if(dp[A][days-1]>dp[B][days-1]):
        product=A
        profit=dp[A][days-1]
    else:
        product=B
        profit=dp[B][days-1]

    def other(p):
        if(p==A):
            return B
        else:
            return A
            
        
    d=days-1
    while(d>=0):
        print("On",d,"day the product chosen was",product)
        if(dp[product][d]==dp[other(product)][d-2]+arr[product][d]):
            print("Switch on day",d-1)
            d-=2;product=other(product)
        else:
            d-=1;product=product
        

def main():
    arr=[[8,1,3,5],[2,1,8,7]]
    print(production_plan(arr))
    dp_trace_path(arr)

main()
    
    
