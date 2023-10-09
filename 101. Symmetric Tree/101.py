# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_reflection(root.left, root.right)
    
    def is_reflection(self, left, right):
        if not right and not left: return True
        if (not right and left) or (not left and right): return False
        if right.val != left.val: return False

        ans = self.is_reflection(left.left, right.right)
        if ans == False: return False
        ans = self.is_reflection(left.right, right.left)
        if ans == False: return False

        return True
        
        