# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        current=[root]
        while current:
            result.append(current[-1].val)
            nextr=[]
            for node in current:
                if node.left:
                    nextr.append(node.left)
                if node.right:
                    nextr.append(node.right)
            current=nextr
        return result