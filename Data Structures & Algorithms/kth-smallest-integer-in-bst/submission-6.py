# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.lst = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while root:
            stack.append(root)
            root = root.left



        while stack:
            numb = stack.pop()
            self.lst.append(numb.val)
            self.lst += self.help(numb)

        return self.lst[k - 1]

    def help(self, node: Optional[TreeNode]) -> list[int]:
        if node.right is None:
            return []

        stack = []
        result = []

        node = node.right
        

        while node:
            stack.append(node)
            node = node.left



        while stack:
            numb = stack.pop()
            result.append(numb.val)
            result += self.help(numb)

        return result            




        