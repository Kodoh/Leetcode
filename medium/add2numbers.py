# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        n2 = ''
        current = l1
        while current:
            n1 += str(current.val)
            current = current.next
        
        n1 = n1[::-1]

        current = l2
        while current: 
            n2 += str(current.val)
            current = current.next
        
        n2 = n2[::-1]

        n3 = str(int(n1) + int(n2))[::-1]
        

        first = ListNode(int(n3[0]))

        current = first
        for i in range(1,len(n3)):
            new = ListNode(int(n3[i]))
            current.next = new
            current = new

        return (first)
    

# O(n) time and space