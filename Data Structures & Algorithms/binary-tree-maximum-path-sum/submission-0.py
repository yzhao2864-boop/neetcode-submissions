# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=float("-inf")
        def gain(root):
            if not root:
                return 0
            left=max(gain(root.left),0)
            right=max(gain(root.right),0)
            self.ans=max(self.ans,root.val+left+right)
            return root.val+max(left,right)
        gain(root)
        return self.ans
        