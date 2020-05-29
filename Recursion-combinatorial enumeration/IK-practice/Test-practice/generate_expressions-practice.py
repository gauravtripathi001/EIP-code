import re
def generate_all_expressions(s, target):
    k=target
    results=[]
    helper(s[0],1,s,k,results)
    return results

def helper(exp,i,s,k,results):
    
    if(i==len(s)):
        e=re.sub(r'\b0+(?!\b)', '', "".join(exp))
        if(eval(e)==k):
            r="".join(exp)
            results.append(r)
            return
    else:
        helper(exp+s[i],i+1,s,k,results)
        helper(exp+"+"+s[i],i+1,s,k,results)
        helper(exp+"*"+s[i],i+1,s,k,results)
def main():
    s="050505"
    target=5
    results=[]
    results=generate_all_expressions(s, target)
    print(results)
    print(len(results))

main()
