def firstPerm(a):
    results=[]
    firstPermHelper(a,0,results)
    print(results)

def firstPermHelper(a,i,results):
    #base case
    if(i==len(a)):
        results.append(a.copy())
        return
    else:
        #firstPermHelper(a,i+1,results)
        for j in range(i,len(a)):
            a[i],a[j]=a[j],a[i]
            ####Important step
            firstPermHelper(a,i+1,results)
            a[j],a[i]=a[i],a[j]
def main():
    a=[1,2,3]
    firstPerm(a)

main()
