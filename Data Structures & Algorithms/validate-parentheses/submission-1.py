class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Early exit: odd lengths are never valid
        if len(s) % 2 != 0:
            return False
            
        stack = []
        # 2. Localize variables or use simple mapping
        # Maps closing bracket directly to opening bracket
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # 3. Use stack[-1] check instead of pop() before verification
                # This avoids unnecessary pops/pushes in some error cases
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
                
        return not stack
