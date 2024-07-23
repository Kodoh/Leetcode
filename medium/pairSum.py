# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hashmap = {}

        current = head

        n = 0
        while current:
            hashmap[n] = current.val
            n += 1
            current = current.next
        
        n -= 1
        maxPair = 0
        for i in range(ceil(n/2)):
            maxPair = max(maxPair,hashmap[i] + hashmap[n-i])
        
        return maxPair
