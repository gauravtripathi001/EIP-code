def bubble_sort(a):
    n=len(a)
    #######Important to remember
    for i in range(1,n):
    #######Important to remember
        for j in range(0,n-i):
            if(a[j+1]<a[j]):
                a[j],a[j+1]=a[j+1],a[j]
    return a
def selection_sort(a):
    n=len(a)
    for i in range(0,n):
        iMin=i
        for j in range(i+1,n):
            if(a[j]<a[iMin]):
                iMin=j
        a[iMin],a[i]=a[i],a[iMin]
    return a
def insertion_sort(a):
    n=len(a)
    #######Important to remember
    for i in range(1,n):
        hole=i
        value=a[hole]
        #######Important to remember
        while(hole>0 and a[hole-1]>value):
            a[hole]=a[hole-1]
            hole-=1
        a[hole]=value
    return a
def merge_sort(a):
    n=len(a)
    mid=n//2
    if(n<2):
        return
    l,r=a[:mid],a[mid:]
    merge_sort(l)
    merge_sort(r)
    merge(a,l,r)
    return a
    
def merge(a,l,r):
    n,nl,nr=len(a),len(l),len(r)
    i,j,k=0,0,0
    while(k<n and i<nl and j<nr):
        if(l[i]<r[j]):
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1
        k+=1
    while(i<nl):
        a[k]=l[i]
        i+=1
        k+=1
    while(j<nr):
        a[k]=r[j]
        j+=1
        k+=1
    
import random
def quick_sort(a,s,e):
    #######Important to remember
    if(s>=e):
        return
    pIndex=random.randint(s,e)
    pivot=a[pIndex]
    a[pIndex],a[s]=a[s],a[pIndex]
    
    orange=s
    #######Important to remember
    for green in range(s+1,e+1):
        if(a[green]<pivot):
            orange+=1
            a[green],a[orange]=a[orange],a[green]
    a[orange],a[s]=a[s],a[orange]
    ########Important to remember
    quick_sort(a,s,orange-1)
    quick_sort(a,orange+1,e)
    return a
    
#def heap_sort(a):
#def radix_sort(a):
#def bucket_sort(a):
#def counting_sort(a):
def main():
    a=[1,3,2,6,7,4]
    #print("Bubble sort",bubble_sort(a))
    #print("Selection sort",selection_sort(a))
    #print("Insertion sort",insertion_sort(a))
    #print("Merge sort",merge_sort(a))
    print("Quick sort",quick_sort(a,0,len(a)-1))



main()
