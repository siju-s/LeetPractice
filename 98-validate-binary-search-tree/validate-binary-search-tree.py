# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, left=float("-inf"), right=float("inf")):
            if not node:
                return True

            value = node.val
            if value <= left or value >= right:
                return False

            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)

        return isValid(root)
        
        