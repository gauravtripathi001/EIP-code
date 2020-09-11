class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def dutch_sort(self,x):
        if(self.head==None):
            return
        #Divide the LL into three lists that are 
        p1_head=Node(0);p1_tail=p1_head
        p2_head=Node(0);p2_tail=p2_head
        p3_head=Node(0);p3_tail=p3_head
        curr=self.head

        while(curr):
            if(curr.data<x):
                    p1_tail.next=curr
                    p1_tail=p1_tail.next
                    curr=curr.next
                    
            elif(curr.data>x):
                    p3_tail.next=curr
                    p3_tail=p3_tail.next
                    curr=curr.next

            else:
                    p2_tail.next=curr
                    p2_tail=p2_tail.next
                    curr=curr.next

        #Attach three lists
        p1_tail.next=(p2_head.next) if(p2_head.next) else (p3_head.next)

        p2_tail.next=p3_head.next

        p3_tail.next=None

        #Updated head
        head=p1_head.next

        return head

def main():
    ll=LinkedList()
    ll.head=Node(0)
    elements=[1,5,2,7,3,6,4,10,9,8]
    curr=ll.head
    for i in elements:
        curr.next=Node(i)
        curr=curr.next

    ll.dutch_sort(5)
    curr=ll.head

    while(curr):
        print(curr.data)
        curr=curr.next
        
    
main()
        

        

        
        
        
