# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    ans = 0
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
         self.count = k
         def dfs(node):
            if not node:
                return

            dfs(node.left)

            if self.count == 1:
                self.ans = node.val

            self.count = self.count - 1

            if self.count > 0:
                dfs(node.right)

         dfs(root)
         return self.ans



    
        