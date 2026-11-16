# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        current=[root]
        while current:
            val=[]
            nextr=[]
            for node in current:
                val.append(node.val)
                if node.left:
                    nextr.append(node.left)
                if node.right:
                    nextr.append(node.right)
            result.append(val)
            current=nextr
        return result