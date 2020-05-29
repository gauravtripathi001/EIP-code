def combHelper(slate,bag):
    if(len(bag)==0):
        print(slate)
    else:
        #exclude
        combHelper(slate,bag[1:])
        #include
        combHelper(slate+bag[0],bag[1:])
def main():
    a=["a","b","c"]
    combHelper("",a)

main()
