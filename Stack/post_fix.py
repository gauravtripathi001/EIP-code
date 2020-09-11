class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[];operations=["+","-","*","/"]
        for i in tokens:
            if i in operations:
                operand_2=stack.pop()
                operand_1=stack.pop()
                stack.append(self.operation(i,operand_1,operand_2))
            else:
                stack.append(int(i))
        return stack[0]
    
    def operation(self,operator,operand_1,operand_2):
        if(operator=="+"):
            return (operand_1+operand_2)
        elif(operator=="-"):
            return (operand_1-operand_2)
        elif(operator=="*"):
            return (operand_1*operand_2)
        elif(operator=="/"):
            return (int)(operand_1/operand_2)
                
            
             return (operand_1//operand_2)

def main():
    sol=Solution()
    tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN(tokens))

main()
