class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        
        def backtrack(remain, current_combination, start):
            if remain == 0:
                result.append(list(current_combination))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                
                current_combination.append(candidates[i])
                backtrack(remain - candidates[i], current_combination, i)
                current_combination.pop()

        backtrack(target, [], 0)
        return result