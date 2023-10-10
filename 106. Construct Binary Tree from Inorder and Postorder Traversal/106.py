# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, inorder):
        if not inorder or not self.postorder: return None
        node = TreeNode(self.postorder[-1])

        mid = inorder.index(self.postorder[-1])
        self.postorder.pop()
        node.right = self.solve(inorder[mid + 1 : ])
        node.left = self.solve(inorder[ : mid])

        return node
    

    def buildTree(self, inorder, postorder):
        self.postorder = postorder
        return self.solve(inorder)