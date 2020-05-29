def decimalStrings(slate,n):
    if(n==0):
        print(slate)
    else:
        for i in range(0,10):
            decimalStrings(slate+str(i),n-1)
        

def main():
    decimalStrings("",3)

main()
