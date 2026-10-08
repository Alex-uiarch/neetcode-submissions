# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        uns = self.dfs(root)
        if uns == -1:
            return False
        return True
    
    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left = self.dfs(node.left)
        if left == -1:
            return -1
        
        right = self.dfs(node.right)
        if right == -1:
            return -1

        if abs(right - left) <= 1:
            return 1 + max(right, left)

        return -1

