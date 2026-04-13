# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node, left_interval, right_interval):
            if not node:
                return True
            
            if not (left_interval < node.val < right_interval):
                return False

            return dfs(node.left, left_interval, node.val) and dfs(node.right, node.val, right_interval)



        return dfs(root, float("-inf"), float("inf"))