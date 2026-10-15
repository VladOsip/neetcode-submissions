class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = 1 << 60
        k = min(k, n - 1)               

        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))

        dist = [INF] * n
        dist[src] = 0
        front = [src]

        for _ in range(k + 1):
            new = dist[:]                
            cap = dist[dst]
            changed = []
            push = changed.append
            for u in front:
                du = dist[u]
                for v, w in adj[u]:
                    nd = du + w
                    if nd < new[v] and nd < cap:
                        if new[v] == dist[v]:   
                            push(v)             
                        new[v] = nd
            if not changed:
                break
            dist = new
            front = changed

        return dist[dst] if dist[dst] < INF else -1