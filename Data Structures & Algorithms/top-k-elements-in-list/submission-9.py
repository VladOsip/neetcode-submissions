class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = defaultdict(int)
        solution = []
        for num in nums:
            counter[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        
        for idx, val in counter.items():
            buckets[val].append(idx)
        
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i]:  # 
                continue
            
            for j in range(len(buckets[i]) - 1, -1, -1):
                solution.append(buckets[i][j])
                k -= 1
                if k == 0:
                    return solution  
        
        return solution