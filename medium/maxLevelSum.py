# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.res = [1,root.val]

        def bfs(nodes,level):
            if not nodes:
                return
            
            sum_nodes = 0
            next_level_nodes = []
            for node in nodes:
                sum_nodes += (node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            if sum_nodes > self.res[1]:
                self.res = [level,sum_nodes]

            bfs(next_level_nodes,level+1)

        def start_bfs(root):
            if root:
                bfs([root],1)

        start_bfs(root)

        return self.res[0]
