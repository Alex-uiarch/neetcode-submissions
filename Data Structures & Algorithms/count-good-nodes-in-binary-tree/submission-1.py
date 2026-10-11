# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        if root is  None:
            return 0
        return self.dfs(root.val, root)


    def dfs(self, max_val: int, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        if node.val >= max_val:
            good = 1
        else:
            good = 0

        max_val = max(max_val, node.val)
        left_count = self.dfs(max_val, node.left)
        right_count = self.dfs(max_val, node.right)

        return good + left_count + right_count

        


        