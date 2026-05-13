# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = [float('-inf')]
        
        def dfs(node):
            if not node:
                return 0
            
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            
            current_path_sum = node.val + left_max + right_max
            
            max_sum[0] = max(max_sum[0], current_path_sum)
            
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return max_sum[0]
