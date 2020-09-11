#Program to detect cycles
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.visited=False

class LinkedList:
    def __init__(self):
        self.head = None
        
    def cycle_detection_brute_force1(self):
        curr=self.head
        while(curr is not None):
            if(curr.visited==True):
                return True
            curr.visited=True
            curr=curr.next
        return False
        
    def cycle_detection_brute_force2(self):
        curr=self.head
        s=set()
        while(curr is not None):
            if(curr in s):
                return True
            s.add(curr)
            curr=curr.next
        return False

    def cycle_detection_two_pointers(self):
        fast=self.head
        slow=self.head

        while(fast is not None and fast.next is not None):
            fast=fast.next.next
            slow=slow.next
            if(fast==slow):
                return True
        return False

    def length_loop(self):
        fast=self.head;slow=self.head

        while(fast is not None and fast.next is not None):
            fast=fast.next.next;slow=slow.next
            if(fast==slow):
                ptr=slow;slow=slow.next;count_len=1
                while(slow is not ptr):
                    slow=slow.next
                    count_len+=1
                return count_len
        return 0

    def find_loop_start(self):
        loop_length=self.length_loop()

        curr=self.head
        while(curr is not None):
            ptr=curr
            for i in range(loop_length):
                ptr=ptr.next
            if(ptr==curr):
                return ptr
            curr=curr.next
        return None
                
                    

def main():
    l=LinkedList()
    element_list=[Node(1),Node(2),Node(3),Node(4),Node(5)]
    l.head=element_list[0]
    
    l.head.next=element_list[1];l.head.next.next=element_list[2];l.head.next.next.next=element_list[3];l.head.next.next.next.next=element_list[4];l.head.next.next.next.next.next=element_list[1]

    print(l.cycle_detection_brute_force1())
    print(l.cycle_detection_brute_force2())
    print(l.cycle_detection_two_pointers())
    print(l.length_loop())
    print(l.find_loop_start().data)

main()
        
