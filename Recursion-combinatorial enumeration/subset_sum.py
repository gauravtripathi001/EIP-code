def combHelper(slate,bag,results,k):
    if(sum(slate)>k):
            return
        
    if(len(bag)==0):
        if(sum(slate)!=k):
            return
        results.append(slate)
        return
    else:
        #exclude
        combHelper(slate,bag[1:],results,k)
        #include
        combHelper(slate+[bag[0]],bag[1:],results,k)
def main():
    a=[1,2,3]
    results=[]
    k=3
    combHelper([],a,results,k)
    print(results)

main()
