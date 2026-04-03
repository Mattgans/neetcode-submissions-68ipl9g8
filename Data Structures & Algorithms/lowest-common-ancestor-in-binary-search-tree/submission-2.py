# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        prev = root
        while self.find(root,p.val) and self.find(root,q.val):
            prev = root
            root = root.left
        root = prev
        while self.find(root,p.val) and self.find(root,q.val):
            prev = root
            root = root.right
        return prev

    def find(self,root: TreeNode, target: int) -> bool:
        if not root:
            return False
        if root.val == target:
            return True
        else:
            return self.find(root.left,target) or self.find(root.right, target)