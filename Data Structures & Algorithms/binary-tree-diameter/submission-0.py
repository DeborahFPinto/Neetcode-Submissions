# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diame = 0
        
        def altura(node):
            if not node:
                return 0
            
            esq = altura(node.left)
            dire = altura(node.right)
            
            self.max_diame = max(self.max_diame, esq + dire)
            
            return max(esq, dire) + 1
        
        altura(root)
        return self.max_diame