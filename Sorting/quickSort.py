def quickSort(a,s,e):
    if(s<e):
        pIndex=partition(a,s,e)
        quickSort(a,s,pIndex-1)
        quickSort(a,pIndex+1,e)

def partition(a,s,e):
    pIndex=s
    pivot=a[e]
    for i in range(s,e):
        if(a[i]<=pivot):
            a[i],a[pIndex]=a[pIndex],a[i]
            pIndex+=1
    a[pIndex],a[e]=a[e],a[pIndex]        
    return pIndex

def main():
    a=[2,1,4,6,3,8,9]
    quickSort(a,0,len(a)-1)
    print(a)

main()
