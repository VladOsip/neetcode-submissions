class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1

        while low < high:
            current_sum = numbers[low] + numbers[high]
            
            if current_sum == target:
                return [low + 1, high + 1]
            elif current_sum < target:
                low += 1
            else:
                high -= 1
        
        return []