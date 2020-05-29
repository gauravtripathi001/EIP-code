def casePerm(s):
    results=[]
    casePermHelper(0,s,results)
    print(results)

def casePermHelper(i,s,results):
    if(i==len(s)):
        results.append(s)
        return
    else:
            if(s[i].isalpha()):
                casePermHelper(i+1,s[:i]+s[i].upper()+s[i+1:],results)
                casePermHelper(i+1,s[:i]+s[i].lower()+s[i+1:],results)
            else:
                casePermHelper(i+1,s,results)

def main():
    s="a34b5"
    casePerm(s)

main()
    
    
    
