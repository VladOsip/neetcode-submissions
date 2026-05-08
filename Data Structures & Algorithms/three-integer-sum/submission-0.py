class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            low, high = i + 1, len(nums) - 1
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                
                if total == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1

                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                elif total < 0:
                    low += 1
                else:
                    high -= 1
                    
        return res