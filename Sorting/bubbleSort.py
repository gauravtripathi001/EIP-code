def bubble_sort(a):
    l=len(a)
    for i in range(1,l-1):
        for j in range(0,l-i-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp  

def main():
    a=[4,2,3,1,7,9]
    bubble_sort(a)
    print(a)

main()
