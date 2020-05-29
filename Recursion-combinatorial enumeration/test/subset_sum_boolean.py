def check_if_sum_possible(arr, k):
    if(len(arr)==1):
        if(arr[0]==k):
            return True
        else:
            return False
    results=[]
    combHelper([],arr,results,k)
    print(results)
    if(len(results)>0 and results[0]!=[]):
        return True
    elif(len(results[0])==0):
        return False
    else:
        return False
def combHelper(slate,bag,results,k):
    if(len(bag)==0):
        if(sum(slate)==k):
            if(len(slate)>0):
                results.append(slate)
        return
    else:
        #exclude
        combHelper(slate,bag[1:],results,k)
        #include
        combHelper(slate+[bag[0]],bag[1:],results,k)

def main():
    arr=[-10,10]
    k=0
    print(check_if_sum_possible(arr, k))
main()

    
    
