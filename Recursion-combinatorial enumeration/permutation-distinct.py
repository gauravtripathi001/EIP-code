def permHelper(slate,a):
    if(len(a)==0):
        print(slate)
    else:
        for i in range(0,len(a)):
            permHelper(slate+a[i],a[:i]+a[i+1:])

def main():
    a=["a","b","c"]
    permHelper("",a)

main()
