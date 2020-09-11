#O(N^3)
def min_set_substring_brute_force(str,set):

    def contains(str,set):
        for i in set:
            if(i not in str):
                return False
        return True

    length=len(str)
    for l in range(1,length+1):
        for i in range(0,length-l+1):
            if(contains(str[i:i+l],set)):
                return str[i:i+l]
    return ""

#Time: O(N^2)
#Space: O(K)
def min_set_substring_optimized(s,t):
    length=len(s);result=(0,length)
    #print(type(t))
    for i in range(0,length):
        temp=t.copy()
        for j in range(i,length):
            if(s[j] in temp):
                temp.remove(s[j])
                if(len(temp)==0):
                    if(j+1-i<result[1]-result[0]):
                        result=(i,j+1)
                    
    return s[result[0]:result[1]]

#Time: O(N)    
def min_set_substring_optimized(s,t):
    length=len(s);resultset=(0,length)
    found={}
    for e in t:
        found[e]=0
    i=j=0;missing=len(t)
    while(i<j):
        if(s[j] in found):
            if(found[s[j]]==0):
                found[s[j]]=1
                missing-=1
                if(missing==0):
                    #Add result to resultset
                    #If the result is less than the existing result
                    
        j+=1
                    
        

def main():
    inp="helloworld"
    set={'w','r','l'}
    print(min_set_substring_optimized(inp,set))
    
main()
