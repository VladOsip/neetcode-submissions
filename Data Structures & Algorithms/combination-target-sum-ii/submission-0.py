class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        temp = []
        candidates.sort()
        n = len(candidates)
        def backtrack(i, total):
            if total == target:
                result.append(temp.copy())
                return
            
            if total > target or i == n:
                return
            
            temp.append(candidates[i])
            backtrack(i+1,total+candidates[i])
            temp.pop()

            j = i+1
            while j < n and candidates[j] == candidates[i]:
                j+=1
            backtrack(j,total)

        backtrack(0,0)
        return result