def merge_sort(a):
    n=len(a)
    if(n<2):
        return
    mid=n//2
    l=[]
    r=[]
    for i in range(0,mid):
        l.append(a[i])
    for i in range(mid,n):
        r.append(a[i])
    merge_sort(l)
    merge_sort(r)
    merge(a,l,r)
    return a

def merge(a,l,r):
    n=len(a)
    nL=len(l)
    nR=len(r)

    i=j=k=0
    while(k<n and i<nL and j<nR):
        if(l[i]<r[j]):
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1
        k+=1

    while(i<nL):
        a[k]=l[i]
        k+=1
        i+=1
    while(j<nR):
        a[k]=r[j]
        k+=1
        j+=1
    return a

def main():
    a=[9,3,1,5,2,8,0]
    print(merge_sort(a))

main()
