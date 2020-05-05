def bubble_sort(a):
    n=len(a)
    for i in range(1,n):
        flag=0
        for j in range(0,n-i):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                flag=1
        if(flag==0):
            break
    return a

def main():
    a=[9,3,1,5,2,8,0]
    print(bubble_sort(a))

main()
