def n_queens(n):
    res=[]
    helper([],0,n,res)
    return res

def helper(b,r,n,res):
    if(r==n):
        res.append(b.copy())
        return
    else:
        for c in range(n):
            if(valid(b,r,c,n)):
                b.append(c)
                helper(b,r+1,n,res)
                b.pop()

def valid(b,r,c,n):
    #column collision
    for row in range(r):
        if(b[row]==c):
            return False
    #Diagonal collision
    for row in range(r):
        col=b[row]
        if(abs(r-row)==abs(c-col)):
            return False
    return True

def main():
    n=4
    print(n_queens(n))
          
main()
            
