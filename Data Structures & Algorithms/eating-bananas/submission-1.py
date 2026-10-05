class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def time_needed(k: int) -> int:
            return sum((p + k - 1) // k for p in piles)

        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            
            if time_needed(mid) <= h:
                ans = mid       
                right = mid - 1 
            else:
                left = mid + 1  

        return ans