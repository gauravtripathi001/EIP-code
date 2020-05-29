def palindrome_decomposition_practice(s):
    results=[]
    helper(s,[],results)
    return results

def helper(s,result,results):
    if(len(s)==0):
        v=results.copy()
        results.append("|".join(v))
        return
    else:
        for i in range(len(s)):
            if(isPalindrome(s[:i+1])):
               result.append(s[:i+1])
               helper(s[i+1:],result,results)
               result.pop()
def isPalindrome(s):
    l=0
    r=len(s)-1
    while(l<=r):
        if(s[l]!=s[r]):
           return False
        l+=1
        r-=1
    return True

def main():
    s="abracadabra"
    print(palindrome_decomposition_practice(s))

main()
