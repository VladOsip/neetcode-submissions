class Solution:
    def rob(self, nums: List[int]) -> int:
        val1 = 0
        val2 = 0

        for num in nums:
            temp = max(num+val1,val2)
            val1 = val2
            val2 = temp
        return val2