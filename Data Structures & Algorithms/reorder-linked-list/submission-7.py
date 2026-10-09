# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head:
        #     return 
        # res=[]
        # current=head
        # while current:
        #     res.append(current)
        #     current=current.next
        # i,j=0,len(res)-1
        # while i<j:
        #     res[i].next=res[j]
        #     i+=1
        #     if i>=j:
        #         break
        #     res[j].next=res[i]
        #     j-=1
        # res[i].next=None


        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        slow.next=None    

        current=second
        prev=None
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

        first,second=head,prev
        while second:
            temp1,temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first,second=temp1,temp2    















