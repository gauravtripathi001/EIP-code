import re
def generate_all_expressions(s, target):
    k=target
    results=[]
    s=list(s)
    helper([s[0]],0,s,k,results)
    return results

def helper(exp,i,s,k,results):
    e=re.sub(r'\b0+(?!\b)', '', "".join(exp))
    
    if(i==len(s)-1 and eval(e)==k):
        r="".join(exp)
        results.append(r)
        return
    else:
        if(i+1<len(s)):
            helper(exp+[s[i+1]],i+1,s,k,results)
            helper(exp+["+"]+[s[i+1]],i+1,s,k,results)
            helper(exp+["*"]+[s[i+1]],i+1,s,k,results)
def main():
    s="050505"
    target=5
    results=[]
    results=generate_all_expressions(s, target)
    print(results)
    print(len(results))

main()
