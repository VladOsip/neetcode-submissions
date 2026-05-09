class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            i = abs(num) - 1
            if nums[i] < 0:
                return abs(num)
            nums[i] *= -1
        return -1