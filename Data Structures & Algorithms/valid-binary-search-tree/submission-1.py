# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.



        

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(float('inf'), float('-inf'), root)

    def dfs(self, right: int, left: int, node: Optional[TreeNode]) -> int:
        if node is None:
            return True

        if node.val >= right or node.val <= left:
            return False

        return (self.dfs(right, node.val, node.right) and self.dfs(node.val, left, node.left)) 
        
        
        


        