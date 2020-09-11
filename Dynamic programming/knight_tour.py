# Complete the function below.

def numPhoneNumbers(startdigit, phonenumberlength):
    if(startdigit==5 and phonenumberlength==1):
        return 1
    elif(startdigit==5):
        return 0
        
    dict={1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4],0:[4,6]}
    
    q=[];q.append(startdigit);curr_length=1;count=1
    
    while(len(q)>0 and curr_length<phonenumberlength):
        count=0;n=len(q)
        print(q)
        for i in range(n):
            node=q.pop(0)
            q=q+dict[node]
            count+=len(dict[node])
        curr_length+=1
        
    return count

def main():
    startdigit=6;phonenumberlength=20
    print(numPhoneNumbers(startdigit, phonenumberlength))
    
main()
