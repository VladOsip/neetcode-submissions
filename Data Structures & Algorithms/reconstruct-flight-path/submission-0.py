class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        target = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            target[src].append(dst)
            
        route = []
        
        def dfs(airport):
            while target[airport]:
                dfs(target[airport].pop())
            route.append(airport)
            
        dfs("JFK")
        return route[::-1]
