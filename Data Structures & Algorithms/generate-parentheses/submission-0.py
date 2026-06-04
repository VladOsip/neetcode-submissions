class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []


        def backtrack(open_rem, close_rem, current_path):
            if open_rem == 0 and close_rem == 0:
                result.append("".join(current_path))
                return

            if open_rem > 0:
                current_path.append('(')
                backtrack(open_rem - 1, close_rem, current_path)
                current_path.pop()  

            if close_rem > open_rem:
                current_path.append(')')
                backtrack(open_rem, close_rem - 1, current_path)
                current_path.pop()  

        backtrack(n, n, [])
        return result