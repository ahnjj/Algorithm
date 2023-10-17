# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        l = []
        def Inorder(root):
            if root:
                Inorder(root.left)
                if root.val >= low and root.val <= high:
                    l.append(root.val)
                Inorder(root.right)
            
        Inorder(root)
        return sum(l)