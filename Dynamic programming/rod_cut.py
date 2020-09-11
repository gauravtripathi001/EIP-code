def max_product_from_cut_pieces(n):
    # Base cases 
    dp=[i-1 for i in range(n+1)]
    dp[0]=0
    # Make a cut at different places 
    # and take the maximum of all 
    
    for i in range(3, n+1):
        for cut in range(2,i//2+1):
            dp[i]=max(dp[i],dp[i-cut]*cut,(i-cut)*cut)
        print("i=",i,"dp table is",dp)
        
   
    #Return the maximum of all values 
    return dp[n]

def main():
    n=6
    res=max_product_from_cut_pieces(n)
    print(res)

main()
