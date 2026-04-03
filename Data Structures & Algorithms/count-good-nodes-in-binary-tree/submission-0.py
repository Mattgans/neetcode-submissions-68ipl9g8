# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        return 1 + self.maxseen(root.left,root.val) + self.maxseen(root.right,root.val)
    
    def maxseen(self,root: TreeNode, maxv: int):
        if not root:
            return 0
        if root.val >= maxv:
            return 1 + self.maxseen(root.left, root.val) + self.maxseen(root.right, root.val)
        else:
            return self.maxseen(root.left,maxv) + self.maxseen(root.right,maxv)