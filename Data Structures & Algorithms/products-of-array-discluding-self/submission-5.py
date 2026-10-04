class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        solution = [1] * length
        
        arr_counter = 1
        for i in range(length):
            solution[i] = arr_counter
            arr_counter *= nums[i]
        
        arr_counter = 1
        for i in range(length - 1, -1, -1):
            solution[i] *= arr_counter
            arr_counter *= nums[i]
        
        return solution