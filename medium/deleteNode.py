# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        current = root

        parent = None
        found = False

        while current:
            if current.val == key:
                found = True
                break
            if key > current.val:
                parent = current
                current = current.right
            
            elif key < current.val:
                parent = current
                current = current.left


        todel = current



        current = None
        
        if parent and todel:
            if todel.val < parent.val:
                if todel.right:
                    parent.left = todel.right
                    temp = todel.left
                    todel = todel.right
                    while todel.left:
                        todel = todel.left
                    todel.left = temp
                else:
                    parent.left = todel.left

            else:
                if todel.left:
                    parent.right = todel.left
                    temp = todel.right
                    todel = todel.left
                    while todel.right:
                        todel = todel.right
                    todel.right = temp
                else:
                    parent.right = todel.right
        
        elif not parent and todel:
            temp = todel
            todel = None
            if temp.right:
                root = temp.right
                temp2 = temp.left
                temp3 = temp.right
                while temp3.left:
                    temp3 = temp3.left
                temp3.left = temp2
            else:
                return temp.left

        return root
