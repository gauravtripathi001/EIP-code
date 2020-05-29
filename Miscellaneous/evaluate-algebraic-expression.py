#Write your own eval function for algebraic expressions
def evaluate(s):
    if(len(s)==0):
        return 0
    #Create list based on *
    a=s.split("+")
    sum=0
    for i in range(len(a)):
        m=a[i].split("*")
        res=1
        for j in range(len(m)):
            res*=(int)(m[j])
        sum+=res
    return sum

def main():
    s="2*2+2*22"
    print(evaluate(s))
main()
