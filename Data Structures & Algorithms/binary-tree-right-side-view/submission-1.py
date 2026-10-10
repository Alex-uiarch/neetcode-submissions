# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        result = []

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lst = self.levelOrder(root)
        lst1 = []
        for x in lst:
            lst1.append(x[-1])

        return lst1
        
        
        