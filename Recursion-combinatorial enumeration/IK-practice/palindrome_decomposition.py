def generate_palindromic_decompositions(s):
    results=[]
    helper(results,[],0,len(s),s)
    return results

#Easy but good to keep in mind
def isPalindrome(s):
    l=0
    #Important
    r=len(s)-1
    #Important
    while(l<r):
        if(s[l]!=s[r]):
            return False
        l+=1
        r-=1
    return True

def helper(results,result,l,r,s):    
    if(l==r):
        #Remember to use copy when using array here
        x=result.copy()
        #Important to remember the format of join and converting list to a string
        results.append(("|".join(x)))
        return
    else:
        #Iterating over end points of substring
        for i in range(l,r):
            #####Important to remember the indices
            #If substring is a palindrome
            if(isPalindrome(s[l:i+1])):
                #Add the palindrom to result
                result.append(s[l:i+1])
                #####Important to remember the indices
                #Recurse in the remaining substring and add to result if applicable
                helper(results,result,i+1,r,s)
                #Remove the added entry
                result.pop()
def main():
    s="abracadabra"
    print(generate_palindromic_decompositions(s))

main()
            
