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
            
            for i in range(len(buckets) - 1, -1, -1):
                for num in buckets[i]:
                    solution.append(num)
                    if len(solution) == k:
                        return solution
        
        return solution