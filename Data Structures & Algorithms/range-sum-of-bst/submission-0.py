class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
            
        BFSTree = deque([root])
        result = 0
        
        while BFSTree: 
            temp = BFSTree.popleft()
            
            if low <= temp.val <= high:
                result += temp.val
                
            if temp.left:
                BFSTree.append(temp.left)
            if temp.right:
                BFSTree.append(temp.right)
                
        return result