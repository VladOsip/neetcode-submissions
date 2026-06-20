class Solution:
    def myPow(self, base: float, exponent: int) -> float:
        if exponent == 0:
            return 1.0
    
        if exponent < 0:
            base = 1.0 / base
            exponent = -exponent
            
        result = 1.0
        current_product = base
        
        while exponent > 0:
            if exponent % 2 == 1:
                result *= current_product
            
            current_product *= current_product
            exponent //= 2
            
        return result