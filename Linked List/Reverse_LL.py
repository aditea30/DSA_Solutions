class Node:
    def __init__ (self,data=0,next_node=None):
        self.data=data
        self.next=next_node
class Solution:
    def reverseList(self,head):
        prev=None
        temp=head
        while temp is not None:
            front=temp.next #ie 2 becomes front
            temp.next=prev #temp.next =1 points to null
            prev=temp # 2 becomes temp
            temp=front # temp is now 2
        return prev
        
#print the linked list
def print_LL(head):
    temp=head
    while temp is not None:
        print(temp.data,end="")
        temp=temp.next
    print()
head=Node(1)
head.next=Node(2)  
head.next.next=Node(3)
head.next.next.next=Node(4)
print("Original linked list is :",end="")
print_LL(head)

#reversing the list
sol=Solution()
head =sol.reverseList(head)
print("Reverse linked List is :",end="")
print_LL(head)

    