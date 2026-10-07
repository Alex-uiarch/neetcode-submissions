# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.diametr = 0


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0


        if self.diametr < (self.height(root.left) + self.height(root.right)):
            self.diametr = self.height(root.left) + self.height(root.right) 

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)


        


        return self.diametr




    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0


        return 1 + max(self.height(node.left), self.height(node.right)) 
