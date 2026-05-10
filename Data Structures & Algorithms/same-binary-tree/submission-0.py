# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        
        if (not p and q) or (p and not q):
            return False
       
        stackP = [p]
        stackQ = [q]
        
        while stackP and stackQ:
            nodeP = stackP.pop()
            nodeQ = stackQ.pop()

            if (not nodeP and nodeQ) or (nodeP and not nodeQ):
                return False
            
            if not nodeP and not nodeQ:
                continue

            if nodeP.val != nodeQ.val:
                return False
            
            stackP.append(nodeP.right)
            stackQ.append(nodeQ.right)
            stackP.append(nodeP.left)
            stackQ.append(nodeQ.left)

        return True