def intersect(m,n):
    lm=len(m)
    ln=len(n)
    i=0
    j=0
    output=[]

    while(i<lm and j<ln):
        if(m[i]==n[j]):
            #check if the last element on output is the same
            if(len(output)>0):
                if(m[i]!=output[-1]):
                    output.append(m[i])
            if(len(output)==0):
                output.append(m[i])
            i+=1
            j+=1
        elif(m[i]<n[j]):
            i+=1
        else:
            j+=1
    return output

def main():
    m=[1,2,4,5,5,6,7,8]
    n=[1,2,3,5,9]
    print(intersect(m,n))
    
main()
            
        
