class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = [0] * 26
        for task in tasks:
            task_freq[ord(task)-ord('A')]+=1
        task_freq.sort()
        max_freq = task_freq[-1]

        partitions = max_freq-1
        idle_slots = partitions*n

        for i in range(24,-1,-1):
            idle_slots-=min(partitions,task_freq[i])
        
        return len(tasks) + max(0, idle_slots)