class Node:
    def __init__(self,data=0,next_node=None):
        self.data=data
        self.next=next_node
class Solution:
    def remove(self,head,n):
        slow=head
        fast=head

        for i in range(n):
            fast=fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            slow=slow.next
            fast=fast.next

        dead_node=slow.next
        slow.next=slow.next.next
        dead_node=None
        return head
    def printLL(self,head):
        while head is not None:
            print(head.data, end=' ')
            head = head.next
arr=[1,2,3,4,5]
n=3
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

sol=Solution()    
# Delete the Nth node from the end and print the modified linked list
head = sol.remove(head, n)
print("Removed head : ",end="")
sol.printLL(head)

