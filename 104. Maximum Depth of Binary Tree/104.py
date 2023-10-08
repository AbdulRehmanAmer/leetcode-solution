# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        self.max_depth = 1
        return self.aux(root)

    def aux(self, node, level = 0):
        if not node: return level
        self.max_depth = max(self.max_depth, self.aux(node.left, level + 1))
        self.max_depth = max(self.max_depth, self.aux(node.right, level + 1))

        return self.max_depth




        