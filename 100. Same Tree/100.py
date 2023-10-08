# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        return self.working(p, q)

    def working(self, tree1, tree2):
        if not tree1 and not tree2: return True
        if not tree1 or not tree2: return False
        if tree1.val != tree2.val:
            return False
        
        ans = self.working(tree1.left, tree2.left)
        if not ans:
            return False
        ans = self.working(tree1.right, tree2.right)
        if not ans:
            return False
        
        return True
        