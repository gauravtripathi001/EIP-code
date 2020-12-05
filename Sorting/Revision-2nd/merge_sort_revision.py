def merge_sort(a):
    helper(a,0,len(a)-1)
    return a

def helper(a,s,e):
    if(s>=e):
        return
    #Divide
    mid=(s+e)//2
    #Sort
    helper(a,s,mid)
    helper(a,mid+1,e)
    #Combine
    aux=[]
    i=s;j=mid+1
    while(i<=mid and j<=e):
        if(a[i]<=a[j]):
            aux.append(a[i]);i+=1
        else:
            aux.append(a[j]);j+=1

    while(i<=mid):
        aux.append(a[i]);i+=1
    while(j<=e):
        aux.append(a[j]);j+=1

    p=0
    for x in range(s,e+1):
        a[x]=aux[p];p+=1

def main():
    a=[34,21,2,37,54,1,33]
    print(merge_sort(a))

main()
    
