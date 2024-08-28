# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        current = head
        while current:
            vals.append(current)
            current = current.next
        if vals:
            vals[0].next = None
        else:
            return None
        for i in range(1,len(vals)):
            vals[i].next = vals[i-1]
        
        return vals[-1]
