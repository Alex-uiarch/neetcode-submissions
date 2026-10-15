class Solution:
    def __init__(self):
        self.dct = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(preorder) == 0 or len(inorder) == 0:
            return None

        self.dct = {}
        for i in range(len(inorder)):
            self.dct[inorder[i]] = i

        def build(pre_start, in_start, in_end):
            if in_start >= in_end:
                return None

            root = TreeNode()
            root.val = preorder[pre_start]

            mid = self.dct[root.val]
            L = mid - in_start
            R = in_end - mid - 1

            root.left = build(pre_start + 1, in_start, mid)
            root.right = build(pre_start + L + 1, mid + 1, in_end)

            return root

        return build(0, 0, len(inorder))