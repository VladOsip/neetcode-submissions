class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                # The second operand is the one most recently pushed
                r = stack.pop()
                l = stack.pop()
                
                if t == '+':
                    stack.append(l + r)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(l * r)
                else:
                    stack.append(int(l / r))
                    
        return stack[0]
