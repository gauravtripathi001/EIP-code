class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s)==1):
            return s
        #Create all substrings sorted by the size of strings in descending order
        
        for length in range(len(s),-1,-1):
            for i in range(0,len(s)-length):
                if(self.is_palindrome(s[i:i+length])):
                    return s[i:i+length]
        return ""
    
    #Find if a string is palindrome
    def is_palindrome(self,str):
        end=len(str)-1
        for start in range(0,len(str)//2):
            if(str[start] is not str[end]):
                return False
            end-=1
        return True

    def longestPalindrome2(self, s: str) -> str:
        n=len(s);result=(0,0)
        #Odd sized palindromes
        for i in range(0,n):
            l=r=i
            while(l>=0 and r<=n-1):
                if(s[l]==s[r]):
                    if((r-l+1)>result[1]-result[0]):
                        result=(l,r+1)
                    l-=1;r+=1
                else:
                    break

        #Even size palindromes
        for i in range(0,n-1):
            l=i;r=i+1

            while(l>=0 and r<=n-1):
                if(s[l]==s[r]):
                    if((r-l+1)>result[1]-result[0]):
                        result=(l,r+1)
                    l-=1;r+=1
                else:
                    break
        return s[result[0]:result[1]]

def main():
    s="babad"
    sol=Solution()
    print(sol.longestPalindrome2(s))

main()
