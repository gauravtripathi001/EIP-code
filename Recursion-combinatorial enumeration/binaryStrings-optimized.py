def binaryStrings(slate,n):
    if(n==0):
        print(slate)
    else:
        binaryStrings(slate+"0",n-1)
        binaryStrings(slate+"1",n-1)

def main():
    binaryStrings("",2)

main()
