def binaryStrings(n):
    result=["0","1"]
    for i in range(1,n):
        newresult=[]
        for s in result:
            newresult.append(s+"0")
            newresult.append(s+"1")
        result=newresult
    return result

def main():
    print(binaryStrings(3))

main()
