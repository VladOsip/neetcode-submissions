class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            l, h = (m + 1, h) if nums[m] > nums[h] else (l, m)
        return nums[l]