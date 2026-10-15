class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        current_min = 1
        current_max = 1

        for num in nums:
            tmp = current_max * num
            current_max = max(num * current_max, num * current_min, num)
            current_min = min(tmp, num * current_min, num)
            result = max(result,current_max)
        return result