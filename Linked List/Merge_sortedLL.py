class Node:
    def __init__(self,val=0,next_node=None):
        self.val=val
        self.next=next_node
class Solution:
    
    def merge_sortedLL(self,List1,List2):
        dummy_node=Node(-1)
        temp=dummy_node
        while List1 is not None and List2 is not None:
            if List1.val<=List2.val:
                temp.next=List1
                List1=List1.next
            else:
                temp.next=List2
                List2=List2.next
            temp=temp.next
        if List1 is not None:
            temp.next=List1
        else:
            temp.next=List2
        return dummy_node.next
    def printLL(self,head):
        temp=head
        while(temp is not None):
            print(temp.val,end="")
            temp=temp.next
        print()

if __name__=="__main__":
    List1=Node(1)
    List1.next=Node(2)
    List1.next.next=Node(3)

    List2=Node(1)
    List2.next=Node(4)
    List2.next.next=Node(5)

    sol=Solution()

    print("First sorted Linked List : ",end="")
    sol.printLL(List1)
    print("Second sorted Linked List :",end="")
    sol.printLL(List2)
    merged_head=sol.merge_sortedLL(List1,List2)
    print("Merged List is :", end="")
    sol.printLL(merged_head)
        
            



