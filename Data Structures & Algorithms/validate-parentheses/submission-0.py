class Solution:
    def isValid(self, s: str) -> bool:
        stack_map = {'}' : '{', ']' : '[', ')' : '('}
        stack = []
        
        for par in s:
            if par in stack_map:
                top = stack.pop() if stack else '#'
                if stack_map[par] != top:
                    return False
            else:
                stack.append(par)
        return not stack