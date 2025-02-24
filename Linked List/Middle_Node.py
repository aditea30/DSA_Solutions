class Node:
    def __init__(self,data=0,next_node=None):
        self.data=data
        self.next=next_node
#Tortoise and hare method
class Solution:
    def middleNode(self, head):
        slow=head
        fast=head
        while fast and fast.next and slow:#checking if fast or fast.next or slow is not None
            fast=fast.next.next
            slow=slow.next
        return slow
#Print the Linked List
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
sol=Solution()
middle_node=sol.middleNode(head)
print("Middle element is :",middle_node.data)