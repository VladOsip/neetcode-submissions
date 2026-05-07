# Adding this at the very top of your code can sometimes 
# boost your "speed percentile" significantly.
import gc
gc.disable() 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        # Pre-binding the get method can save micro-seconds
        _get = prevMap.get 
        
        for i, num in enumerate(nums):
            diff = target - num
            found = _get(diff)
            if found is not None:
                return [found, i]
            prevMap[num] = i