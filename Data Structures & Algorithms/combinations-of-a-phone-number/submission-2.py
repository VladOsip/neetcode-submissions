class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mapping = {'2':'abc', '3':'def', '4':'ghi','5':'jkl','6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}
        result = []

        def backtrack(i, currstr):
            if i == len(digits):
                result.append(currstr)
                return
            
            for char in mapping[digits[i]]:
                backtrack(i + 1, currstr + char)
        
        backtrack(0, "")
        return result