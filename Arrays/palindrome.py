def is_palindromic(s):
    return all(s[i]==s[~i] for i in range(len(s)//2))

def main():
    print(is_palindromic("nitain"))

main()
