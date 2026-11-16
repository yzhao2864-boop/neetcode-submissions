# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max_so):
            if not node:
                return 0
            count=0
            if node.val>=max_so:
                count=1
                max_so=node.val
            count+=dfs(node.left,max_so)
            count+=dfs(node.right,max_so)
            return count
        return dfs(root,root.val)