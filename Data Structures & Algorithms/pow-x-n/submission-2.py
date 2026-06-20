class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        k = 1
        num = 1

        power = abs(n)

        while power:
            if power % 2 == 1:
                num *= x
            x *= x
            power //= 2
            

        return num if n >= 0 else 1 / num
        