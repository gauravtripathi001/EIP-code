def balanced_parentheses(k):
    results=[]
    helper(0,0,"",results,k)
    print(results)

def helper(l,r,curr,results,k):
    #Backtracking
    if(l<r or l>k or r>k):
        return
    #Base case
    if(l==k and r==k):
        results.append(curr)
        return
    #Recursion
    helper(l+1,r,curr+"(",results,k)
    helper(l,r+1,curr+")",results,k)

def main():
    k=4
    balanced_parentheses(k)

main()
