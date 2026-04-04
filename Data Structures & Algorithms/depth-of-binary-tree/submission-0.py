# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        direita = self.maxDepth(root.right)
        esquerda = self.maxDepth(root.left)

        if direita > esquerda:
            return direita + 1
        else:
            return esquerda + 1