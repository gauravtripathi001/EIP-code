import random
def quick_sort(a):
    helper(a,0,len(a)-1)
    return a

def helper(a,s,e):
    if(s>=e):
        return
    pIndex=random.randint(s,e)
    pivot=a[pIndex]
    a[s],a[pIndex]=a[pIndex],a[s]

    lt=s;gt=s+1
    while(gt<=e):
        if(a[gt]<pivot):
            lt+=1
            a[lt],a[gt]=a[gt],a[lt]
        gt+=1
    a[lt],a[s]=a[s],a[lt]

    helper(a,s,lt-1)
    helper(a,lt+1,e)

def main():
    a=[2,32,1,44,31,23,65]
    print(quick_sort(a))

main()
