
class Solution:


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mmx = float('-inf')
        self.helper(root)
        return self.mmx

    def helper(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        A_right = self.helper(node.right)
        A_left = self.helper(node.left)

        A_node = node.val + max(0, A_right, A_left)
        B_node = node.val + max(0, A_right) + max(0, A_left)

        self.mmx = max(self.mmx, B_node)

        return A_node
