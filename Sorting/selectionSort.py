def selection_sort(a):
    l=len(a)
    for i in range(0,l-1):
        iMin=i
        for j in range(i+1,l-1):
            if(a[j]<a[iMin]):
                iMin=j
        temp=a[iMin]
        a[iMin]=a[i]
        a[i]=temp
        

def main():
    a=[]
    selection_sort(a)
    print(a)

main()
