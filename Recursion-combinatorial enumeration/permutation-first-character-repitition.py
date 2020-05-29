def firstPerm(a):
    results=[]
    a.sort()
    helper(a,[],results)
    
    print(set(tuple(row) for row in results))
def helper(a,buffer,results):
    if(len(a)==0):
        results.append(buffer)
        return
    else:
        for i in range(0,len(a)):
            buffer.append(a[i])
            helper(a[0:i]+a[i+1:],buffer.copy(),results)
            buffer.pop()
def main():
    a=[1,2,3,1]
    firstPerm(a)
    
main()
