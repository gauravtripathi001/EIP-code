def selection_sort(a):
    n=len(a)
    for i in range(0,n-1):
        iMin=i
        for j in range(i+1,n):
            if(a[j]<a[iMin]):
                iMin=j
        a[iMin],a[i]=a[i],a[iMin]
    return a

def main():
    a=[2,5,1,3,4,7,0,9]
    print(selection_sort(a))

main()
