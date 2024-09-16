# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        current = head
        while current:
            l.append(current.val)
            current = current.next
        
        l.sort()
        
        start = ListNode()
        current = start
        for i in l:
            new = ListNode(val=i)
            current.next = new
            current = current.next
        
        return start.next
