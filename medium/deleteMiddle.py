# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        current = head
        while current.next:
            n += 1
            current = current.next

        count = 0
        current = head
        while count < n//2 - 1:
            current = current.next
            count += 1

        if current.next:
            temp = current.next.next
            current.next = None
            current.next = temp 
        else:
            head = None

        return (head)
