def quick_sort(a,s,e):
    if(s<e):
        pIndex=partition(a,s,e)
        quick_sort(a,s,pIndex-1)
        quick_sort(a,pIndex+1,e)
    return a

def partition(a,s,e):
    pIndex=s
    pivot=a[e]
    for i in range(s,e+1):
        if(a[i]<pivot):
            a[pIndex],a[i]=a[i],a[pIndex]
            pIndex+=1
    a[pIndex],a[e]=a[e],a[pIndex]
    return pIndex

def main():
    a=[9,3,1,5,2,8,0]
    quick_sort(a,0,len(a)-1)
    print(a)

main()
    
