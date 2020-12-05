def insertion_sort(a):
    helper(a,len(a)-1)
    return a

def helper(a,n):
    if(n==1):
        return
    helper(a,n-1);nth=a[n]
    i=n-2
    while(i>=0 and nth<a[i]):
        a[i],a[i+1]=a[i+1],a[i]
        i-=1
    a[i+1]=nth

    return

def main():
    a=[34,12,36,22,11,53]
    print(insertion_sort(a))

main()
