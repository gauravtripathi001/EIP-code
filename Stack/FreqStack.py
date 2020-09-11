class FreqStack:

    def __init__(self):
        self.stack=[]
        self.dictionary={}
        self.count={}
        self.max=0

    def push(self, x: int) -> None:
        if(x in self.dictionary):
            #Update the count in dictionary
            #print(self.count)
            #print(x)
            self.count[self.dictionary[x]].remove(x)
            self.dictionary[x]+=1
            
        else:
            self.dictionary[x]=1

        
        #Update the highest frequency element
        self.max=max(self.max,self.dictionary[x])
            
        #Add the element to stack
        self.stack.append((x,self.dictionary[x]))
            
        #If count not in dictionary
        if(self.dictionary[x] not in self.count):
        #Add the count and the one element list
            self.count[self.dictionary[x]]=[x]
        #Else append the element to corresponding count value
        else:
            self.count[self.dictionary[x]].append(x)
        
    def pop(self) -> int:
        if(len(self.stack)==0):
            return
        
        result=self.count[self.max][0]
        
        #Update the stack
        pop_element=self.stack.pop()
        #Update the dictionary
        self.dictionary[pop_element[0]]-=1
        #Update the count dictionary
        self.count[pop_element[1]].remove(pop_element[0])
        
        if(len(self.count[pop_element[1]])==0):
            self.count.pop(pop_element[1])

        #print(pop_element[1]-1)
        if((pop_element[1]-1) not in self.count):
            self.count[pop_element[1]-1]=[pop_element[0]]
        else:
            self.count[pop_element[1]-1].append(pop_element[0])

        if(self.max not in self.count):
            self.max-=1
        
        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
def main():
    s=FreqStack()
    arr=[5,7,5,7,4,5]
    
    for i in arr:
        s.push(i)
    print(s.stack)
    #for i in range(len(arr)):
        
    #    print("stack",s.stack,"count dictionary",s.count,"popped",s.pop())
main()    
