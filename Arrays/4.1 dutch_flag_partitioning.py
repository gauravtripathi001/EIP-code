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
def d_f_p_2(a,pIndex):
    pivot=a[pIndex]
    for i in range(len(a)):
        for j in range(i+1,len(a)-1):
            if(a[j]<pivot):
                a[j],a[pIndex]=a[pIndex],a[j]
                pIndex+=1
                break
    #for i in range(reversed(len(a))):
    #    for 
        


#Approach 3
#Greater,unclassified,equal
#Need to think more about this
def main():
    a=[2,0,1,2,0,1]
    pIndex=2
    result=d_f_p_2(a,pIndex)
    print(result)

main()
