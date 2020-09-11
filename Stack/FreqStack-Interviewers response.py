# Implement FreqStack, a class which simulates the operation of a
# stack-like data structure.

# FreqStack has two functions:
#   - push(int x), which pushes an integer x onto the stack.
#   - pop(), which removes and returns the most frequent element in the stack.
#       If there is a tie for most frequent element, the element closest to
#       the top of the stack is removed and returned.




# { 5: 3 } five has been used three times
# { 3: [5], 2: [5, 7], 1: [5, 7, 4] } groups
# self.current_max ---> 3

# pop
#    go to self.groups[self.current_max].pop(), update the count dictionary

# push
#    check the current count the int being added, add 1, push that onto the groups stack
#    if that number+1 is greater than current max, update that



class FreqStack():
    def __init__(self):
        #Element: (x,count)
        self.stack=[]
        self.count_dictionary={}
        return

    def push(self, x):
        #{5:3, 7:2, 4:1}
        ##{3:5,2:7,1:4}
        if(x in self.count_dictionary):
            #[(5,1),(7,1),(5,2)]
            self.stack.append((x,self.count_dictionary[x]+1))
            #{5:2,7:1}
            self.count_dictionary[x]=self.count_dictionary[x]+1
        else:
            #[(5,1),(7,1)]
            self.stack.append((x,1))
            #{5:1,7:1}
            self.count_dictionary[x]=1
        return
        

    def pop(self):
        element=self.stack.pop()
        #Update the count of the popped element
        self.count_dictionary[element]-=1
        
        result=self.count_dictionary[max(self.count_dictionary)]
        return result[0]
    
freqStack = FreqStack()

freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)

print(freqStack.pop(), 5)
print(freqStack.pop(), 7)
print(freqStack.pop(), 5)
print(freqStack.pop(), 4)

##
#[5,7,5,7,4,5]
#[(5,1),(7,1),(5,2),(7,2),(4,1),(5,3)]


#If I get a 5
#{5:3, 7:2, 4:1}

#{3:5, 2:7, 1:4}
#{2:(7,5),1:4}


#If I get 5 again
#Check in dictionary
#Increment the count
#{5:2}
#[(),(5,2),(7,2),(5,3)]

#{key:value}, {count:[elements]}
#{1:}
