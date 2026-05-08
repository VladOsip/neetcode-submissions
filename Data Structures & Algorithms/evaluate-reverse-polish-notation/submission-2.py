import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # Map operators to their functional equivalents
        # operator.truediv is used to handle the 'truncate toward zero' requirement
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda l, r: int(l / r)
        }
        
        stack = []
        # Localize methods to avoid repeated attribute lookups
        push = stack.append
        pop = stack.pop
        
        for t in tokens:
            if t in ops:
                r = pop()
                l = pop()
                push(ops[t](l, r))
            else:
                push(int(t))
                
        return stack[0]