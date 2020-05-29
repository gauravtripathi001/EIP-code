import copy
n=9
def helper(p,r,c,res):
    if(r==n):
        res.append(copy.deepcopy(p))
        #res=res+copy.deepcopy(p)
        #print(res)
        return
    #print(p,r,c)
    if(p[r][c]=='.'):
        for val in range(1,n+1):
            if(valid(p,r,c,val)):
                p[r]=p[r][:c]+str(val)+p[r][c+1:]
                #print(p)
                if(c==n-1):
                    helper(p,r+1,0,res)
                else:
                    helper(p,r,c+1,res)
                p[r]=p[r][:c]+"."+p[r][c+1:]
    else:
        if c==n-1:
            helper(p,r+1,0,res)
        else:
            helper(p,r,c+1,res)

def valid(p,r,c,val):
    for row in range(n):
        if(p[row][c]==str(val)):
            return False
    for col in range(n):
        if(p[r][col]==str(val)):
            return False
    r=(r//3)*3
    c=(c//3)*3
    for row in range(r,r+3):
        for col in range(c,c+3):
            if(p[row][col]==str(val)):
                return False
    return True

def main():
    A=[ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ]
    res=[]
    helper(A,0,0,res)
    A=res[0]
    print(A)
    
main()


