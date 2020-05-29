def generate_all_subsets(s):
    results=[]
    helper("",s,results)
    return results
def helper(slate,bag,results):
    if(len(bag)==0):
        results.append(slate)
        return
    else:
        helper(slate,bag[1:],results)
        helper(slate+bag[0],bag[1:],results)
def main():
    s="xy"
    print(generate_all_subsets(s))
main()
