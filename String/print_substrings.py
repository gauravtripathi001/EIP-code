def print_substrings(str):
    l=len(str)
    for i in range(l):
        for j in range(i+1,l+1):
            print(str[i:j])
            print(i,j)

def print_substrings2(str):
    length=len(str)
    for l in range(1,length+1):
        for i in range(0,length-l+1):
            print(str[i:i+l])
            print(i,i+l)
def main():
    #inp="helloworld"
    inp="abc"
    print_substrings2(inp)

main()
