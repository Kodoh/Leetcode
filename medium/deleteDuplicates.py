# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = {}

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        current = head
        while current:
            if current.val in seen:
                seen[current.val] += 1
            else:
                seen[current.val] = 1

            current = current.next

        
        current = head

        while current:
            if seen[current.val] > 1:
                prev.next = current.next
            else:
                prev = current  

            current = current.next  

        return dummy.next
        
