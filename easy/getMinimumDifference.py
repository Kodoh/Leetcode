# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.prev = None
        self.minDiff = float('inf')

        def inorder_traversal(root):
            if root:
                inorder_traversal(root.left)
                if (self.prev is not None):
                    self.minDiff = min(self.minDiff, abs(root.val-self.prev))
                
                self.prev = root.val
                inorder_traversal(root.right)

        inorder_traversal(root)
        return self.minDiff
