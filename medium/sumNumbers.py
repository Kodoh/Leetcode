class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node,res):
            if not node:
                return 0

            if (not node.left) and (not node.right):
                return int(str(res) + str(node.val))
            
            res = int(str(res) + str(node.val))
            
            return dfs(node.left,res) + dfs(node.right,res)
