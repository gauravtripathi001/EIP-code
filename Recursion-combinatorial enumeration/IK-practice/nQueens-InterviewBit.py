def n_queens(n):
    res=[]
    helper([],0,n,res)
    output=[]
    for board in res:
        fb=["."*n]*n
        for row in range(n):
            col=board[row]
            fb[row]=fb[row][:col] + "Q" + fb[row][col + 1:]
        output.append(fb)
    return output
    

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
    results=n_queens(n)
    print(results)
          
main()
            
