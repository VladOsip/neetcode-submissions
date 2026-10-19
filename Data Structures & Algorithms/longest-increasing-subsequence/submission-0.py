class Solution:
    def lengthOfLIS(self, nums: Lista[int]) -> int:
        if not nums:
            return 0
    
        length = 0
        for num in nums:
            left, right = 0, length
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            

            nums[left] = num
            
            if left == length:
                length += 1
                
        return length