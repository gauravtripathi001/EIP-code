def selection_sort(a):
    n=len(a)
    if(n==1):
        return a
    #Find minimum from index i to n-1 where i->0-n-1
    for i in range(n):
        min_i=i
        #Update the minimum index for each i
        for j in range(i+1,n):
            if(a[j]<a[min_i]):
                min_i=j
        #Swap the minimum index element with ith element
        a[min_i],a[i]=a[i],a[min_i]
    return a

def main():
    a=[34,22,46,65,1,9,55]
    print(selection_sort(a))

main()
