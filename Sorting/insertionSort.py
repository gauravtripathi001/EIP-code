def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        hole=i
        value=a[i]
        while(hole>0 and a[hole-1]<value):
            a[hole]=a[hole-1]
            hole=hole-1
        a[hole]=value
    return a

def main():
    a=[9,3,1,5,2,8,0]
    print(insertion_sort(a))

main()
