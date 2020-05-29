import random

def quick_select(a,k,s,e):
    if(s>=e): return
    #if pIndex is less than k
        #then quickSelect in right of pIndex
    #else
        #quickSelect in left of pIndex
    pIndex=random.randint(s,e)
    pivot=a[pIndex]
    a[pIndex],a[s]=a[s],a[pIndex]
    small=s
    for big in range(s+1,e+1):
        if(a[big]<pivot):
            small+=1
            a[big],a[small]=a[small],a[big]
    a[s],a[small]=a[small],a[s]

    if(k==small):
        return a[small]
    elif(k<small):
        quick_select(a,k,s,small-1)
    else:
        quick_select(a,k,small+1,e)
    #return -1

def main():
    a=[1,2,3,4,5]
    k=1
    print(quick_select(a,len(a)-k,0,len(a)-1))

main()
            
            
        
