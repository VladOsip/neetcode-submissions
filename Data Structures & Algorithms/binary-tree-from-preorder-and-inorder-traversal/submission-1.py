# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        
        def helper(in_left: int, in_right: int) -> TreeNode | None:
            nonlocal pre_idx
            
            if in_left > in_right:
                return None
            
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            root_idx = inorder_map[root_val]
            
            root.left = helper(in_left, root_idx - 1)
            root.right = helper(root_idx + 1, in_right)
            
            return root
            
        return helper(0, len(inorder) - 1)