class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        curr=self.head
        while(curr):
            print(curr.data)
            curr=curr.next

    def reverse(self):
        prev=None;curr=self.head;next=curr.next

        while(next):
            curr.next=prev
            prev=curr
            curr=next
            next=next.next

        curr.next=prev
        self.head=curr
        return self

    def insert_list(self,l):
        self.head=Node(l[0])
        curr=self.head
        for i in l[1:]:
            curr.next=Node(i)
            curr=curr.next
        

def main():
    ll=LinkedList()
    elements=[1,5,2,7,3,6,4,10,9,8]
    ll.insert_list(elements)

    ll.reverse().print()

main()
    
            
