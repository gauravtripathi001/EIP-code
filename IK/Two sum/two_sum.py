def two_sum_dict(a,sum):
    dict={}
    for i in range(len(a)):
        if ((sum-a[i]) in dict):
            return True
        dict[a[i]]=1
    return False

def two_sum_two_pointer(a,sum):
    a.sort()
    l,r=0,len(a)-1
    while(l<r):
        if(a[l]+a[r]==sum):
            return True
        elif(a[l]+a[r]<sum):
            l+=1
        else:
            r-=1
    return False

def main():
    a=[1,2,3,4,5]
    print(two_sum_two_pointer(a,3))
main()
    
    
        
            
    
