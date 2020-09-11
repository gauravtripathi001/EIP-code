# Complete the function below.
class Stack:
        def __init__(self):
            self.list=[]
        def push(self,x):
            self.list.append(x)
        def pop(self):
            if(len(self.list)==0):
                return
            return self.list.pop()
        def is_empty(self):
            return len(self.list)==0


def find_max_length_of_matching_parentheses(brackets):
    '''1. You can use the check balanced parantheses algorithm here with a slight modification
    2. Use check balanced parantheses upto length k. 
    Store the length of balanced parantheses upto this point as curr.
    Compare this with the maximum length of balanced parentheses section.
    '''
    stack=Stack();max_length1=0;l=0
    for k in brackets:
        if(k=='('):
            stack.push(')')
        elif(k==')'):
            top=stack.pop()
            if(top==')'):
                l+=2
                max_length1=max(l,max_length1)
            else:
                stack=Stack()
                l=0

    stack=Stack();max_length2=0;l=0
    for k in brackets[::-1]:
        if(k==')'):
            stack.push('(')
        elif(k=='('):
            top=stack.pop()
            if(top=='('):
                l+=2
                max_length2=max(l,max_length2)
            else:
                stack=Stack()
                l=0
    
    return min(max_length1,max_length2)

def find_max_length_of_matching_parentheses_ik(brackets):
    # Indices of the opening parentheses will be pushed into the stack and popped back out
    # once the matching closing parenthesis found. The latest not-yet-closed '(' is always
    # at the top of the stack, that is where current substring with balanced parentheses begins.
    stack = []

    # Starting index of the current substring with balanced parentheses when the stack is empty.
    valid_from = 0

    # The longest substring with balanced parentheses we found so far:
    max_length = 0

    for i, bracket in enumerate(brackets):
        if bracket == '(':
            stack.append(i)
        else:
            if not stack:
                # We found a closing parenthesis with no matching opening one.
                # It means that the substring until and including current index DOES NOT have
                # balanced parentheses and we must "forget about" it until the end of the string.
                valid_from = i + 1
            else:
                # We found a closing parenthesis with a matching opening one.
                # It means that the substring ending at the current index i DOES have balanced parentheses.
                # Let us see if it is longer than max_length.
                print(stack.pop())
                substring_start = valid_from - 1 if not stack else stack[-1]
                substring_length = i - substring_start
                max_length = max(substring_length, max_length)
                print("stack",stack,"valid_from",valid_from,"substring start",substring_start,"substring_length",substring_length,"max_length",max_length)
        print(stack,i)

    return max_length
       
def main():
    #x="((((())(((()"
    #x=")))))()"
    x="()()"
    print(find_max_length_of_matching_parentheses_ik(x))

main()

