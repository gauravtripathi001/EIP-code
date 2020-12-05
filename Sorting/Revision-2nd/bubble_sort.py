def bubble_sort(a):
    n=len(a)
    if(n==1):
        return a

    for i in range(n-1,-1,-1):
        for j in range(i):
            print(j)
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    return a

def main():
    a=[2,8,1,4,55,68,32,59,31]
    print(bubble_sort(a))

main()
