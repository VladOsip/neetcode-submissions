class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        parent = {}
        size = {}
        max_len = 0
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) 
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                size[root_j] += size[root_i]
                return size[root_j]
            return size[root_i]

        for num in nums:
            if num in parent:
                continue 
            
            parent[num] = num
            size[num] = 1
            max_len = max(max_len, 1)
            
            if num + 1 in parent:
                sz = union(num, num + 1)
                max_len = max(max_len, sz)
                
            if num - 1 in parent:
                sz = union(num, num - 1)
                max_len = max(max_len, sz)
                
        return max_len