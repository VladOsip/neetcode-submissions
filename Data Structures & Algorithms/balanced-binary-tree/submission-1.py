# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_balance(head):
            if not head:
                return 0
            
            left = check_balance(head.left)
            if left == -1:
                return -1
            
            right = check_balance(head.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1

            return 1 + max(left,right)
        
        return check_balance(root) != -1
        
