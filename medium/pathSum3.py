# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0

        def helper(root,targetSum):
            if not root:
                return False
            
            def dfs(root,targetSum,current):
            
                if not root:
                    return False

                current += root.val
                if current == targetSum:
                    nonlocal res
                    res += 1

                dfs(root.left,targetSum,current)
                dfs(root.right,targetSum,current)
            dfs(root,targetSum,0)
            helper(root.left,targetSum)
            helper(root.right,targetSum)

        helper(root,targetSum)
        return res
        

