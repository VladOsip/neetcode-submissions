class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getNext(n)
        
        while fast != 1 and slow != fast:
            slow = self.getNext(slow)           
            fast = self.getNext(self.getNext(fast))  
            
        return fast == 1

    def getNext(self, n: int) -> int:
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum