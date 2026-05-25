class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            first, second = 0,0

            for i in range(len(arr)):
                total = max(first+arr[i],second)
                first = second
                second = total
            
            return total

        return max(helper(nums[1:]),helper(nums[:-1]))       
