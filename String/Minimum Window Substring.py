class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=len(t);min_value=len(s);result=""
        for i in range(0,len(s)):
            k=0
            for j in range(i,len(s)):
                if(s[j]==t[k]):
                    k+=1
                if(k==l-1):
                    min_value=min(min_value,j-i)
                    if(min_value==j-i):
                        print(j,i)
                        result=s[i:j]
                    break
        return result

def main():
    sol=Solution()
    S = "ADOBECODEBANC"; T = "ABC"
    print(sol.minWindow(S,T))

main()
