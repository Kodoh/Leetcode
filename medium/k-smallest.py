# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = set()
        def brute(root):
            if root:
                if root.val not in vals:
                    vals.add(root.val)
                
                brute(root.left)
                brute(root.right)
        brute(root)
        return list(vals)[k-1]