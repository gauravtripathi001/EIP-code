#Check if a string can be broken into dictonary words
def helper_brute_force(s,dictionary):
    l=len(s)
    if(l==0):
        return True
    for i in range(1,l+1):
        if((s[:i] in dictionary) and (helper_brute_force(s[i:],dictionary))):
           return True
    return False

def helper_top_down(s,dictionary,memo):
    l=len(s)
    if(s in memo):
        return memo[s]
    if(l==0):
        return True
    for i in range(1,l+1):
        if((s[:i] in dictionary) and (helper_top_down(s[i:],dictionary,memo))):
            memo[s]=True
            return True
    memo[s]=False
    return False

def helper_bottom_up(s,dictionary):
    l=len(s)
    
    dp=[False for i in range(l+1)]
    dp[0]=True

    for i in range(1,l+1):
        for j in range(0,i):
            if(dp[j] and (s[j:i] in dictionary)):
                dp[i]=True

    return dp[l]
         
def helper_word_break_count(s,dictionary):
    l=len(s)
    dp=[0 for i in range(l+1)]
    dp[0]=1
    for i in range(1,l+1):
        for j in range(0,i):
            if(s[j:i] in dictionary):
                dp[i]+=dp[j]
    return dp[l]

def helper_word_break_count2(s,dictionary):
    l=len(s)
    dp=[[""] for i in range(l+1)]
    
    for i in range(1,l+1):
        for j in range(0,i):
            if(s[j:i] in dictionary):
                for k in dp[j]:
                    if( k!=""):
                        dp[i]+=[k+" "+s[j:i]]
    print(dp)     
    return dp[l]
        
def main():
    #Brute force testing
    dictionary={"c","o","de","x"}
    s="code"
    result=helper_brute_force(s,dictionary)
    print(result)

    dictionary2={"kickstart","kick","start","is","awe","some","awesome"}
    s2="kickstartisawesome"
    result2=helper_brute_force(s2,dictionary2)
    print(result2)

    #Top down testing
    memo={}
    dictionary3={"kickstart","kick","start","s","awe","some","awesome"}
    s3="kickstartisawesome"
    result3=helper_top_down(s3,dictionary3,memo)
    print(result3)

    #Bottom up testing
    dictionary4={"kickstart","kick","start","is","awe","some","awesome"}
    s4="kickstartisawesome"
    result4=helper_bottom_up(s4,dictionary4)
    print(result4)

    #Word break count
    dictionary5={"kickstart","kick","start","is","awe","some","awesome"}
    s5="kickstartisawesome"
    result5=helper_word_break_count(s5,dictionary5)
    print(result5,"\n")

    #Word break count
    dictionary6={"kickstart","kick","start","is","awe","some","awesome"}
    s6="kickstartisawesome"
    result6=helper_word_break_count2(s6,dictionary6)
    print(result6)
    
main()
