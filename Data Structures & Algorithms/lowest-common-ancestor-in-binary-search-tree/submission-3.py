class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode | None", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode | None":
        if p.val > q.val:
            p, q = q, p

        cur = root
        while cur:
            if q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val:
                cur = cur.right
            else:
                return cur

        return None