class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.array=[-1]*k
        self.head=-1
        self.tail=-1
        self.capacity=k
        self.size=0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if(self.size==self.capacity):
            return False
        if(self.size==0):
            self.head=0 
        self.tail=(self.tail+1)%self.capacity
        self.array[self.tail]=value
        self.size+=1
        return True
            

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if(self.size==0):
            return False
        if(self.size==1):
            self.array[self.head]=-1
            self.head=-1
            self.tail=-1
            self.size=0
        else:
            self.array[self.head]=-1
            self.head=(self.head+1)%self.capacity
            self.size-=1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.array[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.array[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size==0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size==self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
