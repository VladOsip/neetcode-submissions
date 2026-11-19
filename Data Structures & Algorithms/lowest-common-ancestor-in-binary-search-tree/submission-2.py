class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode | None", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode | None":
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right