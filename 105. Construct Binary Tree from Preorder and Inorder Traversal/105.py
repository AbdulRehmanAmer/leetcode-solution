from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, inorder):
        if not inorder or not self.preorder: return None
        node = TreeNode(self.preorder[0])

        mid = inorder.index(self.preorder[0])
        self.preorder.popleft()
        node.left = self.solve(inorder[ : mid])
        node.right = self.solve(inorder[mid + 1 : ])

        return node

    def buildTree(self, preorder, inorder):
        self.preorder = deque(preorder)
        return self.solve(inorder)
         