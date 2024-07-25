# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0

    
        def zigZag(node,direc,current):
            if not node:
                return 
            

            self.res = max(current,self.res)
            if direc == 'R':
                zigZag(node.right,'L',current + 1) 
                zigZag(node.right,'R',0) 
            elif direc == 'L':
                zigZag(node.left,'R',current + 1) 
                zigZag(node.left,'L',0) 



        zigZag(root,'L',0)
        zigZag(root,'R',0)

        return self.res
