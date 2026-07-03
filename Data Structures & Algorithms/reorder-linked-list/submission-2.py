# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        res=[]
        current=head
        while current:
            res.append(current)
            current=current.next
        i,j=0,len(res)-1
        while i<j:
            res[i].next=res[j]
            i+=1
            if i>=j:
                break
            res[j].next=res[i]
            j-=1
        res[i].next=None
                    