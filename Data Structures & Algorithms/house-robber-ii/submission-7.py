class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            first, second = 0, 0
            for val in arr:
                total = max(first + val, second)
                first = second
                second = total
            return second  
        return max(helper(nums[1:]), helper(nums[:-1]))