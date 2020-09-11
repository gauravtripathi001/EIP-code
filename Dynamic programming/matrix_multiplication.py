#Brute force
# def  minMultiplicationCost(input):
#     num_matrices=len(input)-1
#     matrices=[(input[i],input[i+1]) for i in range(num_matrices)]

#     return helper(matrices)

# def helper(m):
#     #Base case
#     if(len(m)==1):
#         return m[0][0]*m[0][1]
#     #Two matrices
#     if(len(m)==2):
#         return m[0][0]*m[0][1]*m[-1][1]

#     #General case
#     return min((m[0][0]*m[0][1]*m[-1][1]+helper(m[1:]))
#               ,(helper(m[:-1])+m[0][0]*m[-1][0]*m[-1][1]))

def minMultiplicationCost_brute_force(input):
    i=1;j=len(input)-1
    return helper(i,j,input)

def helper(i,j,input):
    if(i==j):
        return 0
    val=sys.maxsize
    for k in range(i,j):
        val=min(val,(helper(i,k,input)+helper(k+1,j,input)+input[i-1]*input[k]*input[j]))
    return val

import sys
def minMultiplicationCost_dp(input):
    n=len(input)
    dp=[[0 for x in range(n)] for y in range(n)]
    k_table=[[0 for x in range(n)] for y in range(n)]
    for l in range(1,n):
        for i in range(1,n-l):
            val=sys.maxsize
            for k in range(i,i+l):
                #val=min(val,(dp[i][k]+dp[k+1][i+l]+input[i-1]*input[k]*input[i+l]))
                if(val>(dp[i][k]+dp[k+1][i+l]+input[i-1]*input[k]*input[i+l])):
                    val=(dp[i][k]+dp[k+1][i+l]+input[i-1]*input[k]*input[i+l])
                    k_table[i][i+l]=k
            dp[i][i+l]=val
    printParenthesis(k_table, 1, len(input)-1)
    return dp[1][n-1]

def printParenthesis(k_table, i, j ):
    print(i,j,"\n")
    # Displaying the parenthesis. 
    if j == i: 
  
        # The first matrix is printed as  
        # 'A', next as 'B', and so on 
        print(chr(65 + i), end = "") 
        return
    else: 
        print("(", end = "") 
  
        # Passing (m, k, i) instead of (s, i, k) 
        printParenthesis(k_table, i, k_table[i][j]) 
  
        # (m, j, k+1) instead of (s, k+1, j) 
        printParenthesis(k_table, k_table[i][j]+1,j) 
        print (")", end = "" )

def main():
    mtxSizes=[10, 20, 30, 40, 30]
    print("Brute force",minMultiplicationCost_brute_force(mtxSizes))
    print("DP approach",minMultiplicationCost_dp(mtxSizes))

main()
    
