class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1

        while low <= high:
            mid = (high+low) // 2
            if nums[mid] < target:
                low = mid+1
                continue
            elif nums[mid] > target:
                high = mid-1
                continue
            else:
                return mid
        return -1
