class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1

        path_through_root = depth(root.left) + depth(root.right)
        
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(path_through_root, left_diameter, right_diameter)