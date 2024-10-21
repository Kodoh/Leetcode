"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return 
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []  
            
            for i in range(level_size):
                current = queue.popleft()
                current_level.append(current)  
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            for i in range(len(current_level)-1):
                current_level[i].next = current_level[i+1]

        
        return root
            
