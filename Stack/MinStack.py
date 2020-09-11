#Create a stack class which can return minimum element in constant time
import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list=[]        

    def push(self, x: int) -> None:
        if(len(self.list)==0):
            self.list.append((x,x))
        else:
            self.list.append((x,min(x,self.list[-1][1])))

    def pop(self) -> None:
        self.list.pop()

    def top(self) -> int:
        return self.list[-1][0]

    def getMin(self) -> int:
        if(len(self.list)==0):
            return
        return self.list[-1][1]
        
