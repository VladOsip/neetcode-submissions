class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n]+=1

        for key, val in count.items():
            freq[val].append(key)
        
        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
            