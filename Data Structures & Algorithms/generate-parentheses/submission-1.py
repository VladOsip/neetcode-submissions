class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_rem, close_rem, path):
            if open_rem == 0 and close_rem == 0:
                res.append("".join(path))
                return
            
            if open_rem > 0:
                path.append('(')
                backtrack(open_rem - 1, close_rem, path)
                path.pop()
                
            if close_rem > open_rem:
                path.append(')')
                backtrack(open_rem, close_rem - 1, path)
                path.pop()

        backtrack(n, n, [])
        return res