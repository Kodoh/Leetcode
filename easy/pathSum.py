# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        current = 0
        def dfs(current,root,targetSum):
            if root:
                current += root.val
                if current == targetSum and not (root.left or root.right):
                    return True
                
                return dfs(current,root.left,targetSum) or dfs(current,root.right,targetSum)

            else:
                return False
            
        return dfs(current,root,targetSum)
