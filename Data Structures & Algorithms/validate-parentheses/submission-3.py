class Solution:
    def isValid(self, s: str) -> bool:
        stack_map = {'}': '{', ']': '[', ')': '('}
        stack = []

        for c in s:
            if c not in stack_map:
                stack.append(c)
            else:
                if stack and stack[-1] == stack_map[c]:
                    stack.pop()
                else:
                    return False
        
        return not stack  