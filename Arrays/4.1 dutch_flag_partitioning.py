#Dutch flag partitioning

#Approach 1
#Create three lists-->Lesser,Equal,Greater
#Merge these lists
#Time complexity O(n)
#Space complexity O(n)
def d_f_p_1(a,pIndex):
    pivot=a[pIndex]
    l,e,g=[],[],[]
    for i in range(0,len(a)):
        if(a[i]<pivot):
            l.append(a[i])
        elif(a[i]>pivot):
            g.append(a[i])
        else:
            e.append(a[i])
    return l+e+g

#Approach 2
#Go over the list in forward direction
#Swap the list with the pivot element
#Go over the list in reversed direction
#Swap the list with the pivot element
#O(n^2)
#O(1)
#
def d_f_p_2(a,pIndex):
    pivot=a[pIndex]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[j]<pivot):
                a[i],a[j]=a[j],a[i]
                break
    
    for i in reversed(range(len(a))):
        for j in reversed(range(i)):
            if(a[j]>pivot):
                a[i],a[j]=a[j],a[i]
                break
    return a
        


#Approach 3
#Greater,unclassified,equal
#Need to think more about this
def main():
    a=[2,0,1,2,0,1]
    pIndex=2
    result=d_f_p_2(a,pIndex)
    print(result)

main()
