class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        topK = []

        for num in nums:
            if len(topK) < k:
                heapq.heappush(topK, num)
            else:
                heapq.heappushpop(topK, num)
        
        return topK[0]