def binaryStrings(n):
    if(n==1):
        return ["0","1"]
    else:
        prev=binaryStrings(n-1)
        result=[]
        for s in prev:
            result.append(s+"0")
            result.append(s+"1")
        return result

def main():
    print(binaryStrings(100))

main()
        
